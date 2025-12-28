#!/usr/bin/env python3
from __future__ import annotations

"""Convert FactoryIL episode folders into per-frame `.npz` files for IL training.

Input layout (written by `factoryil.runner` via `EpisodeStager`):
  episodeXX/
    rgb_cam/0000.png
    depth_cam/0000.npy
    rgb_tactile_left/0000.png
    rgb_tactile_right/0000.png
    pc/0000.npy                      (optional)
    timestamps_robot.csv             (frame,is_first,is_last,proprio,action,eef_pose_w)
    env_id.txt / env_origin.txt      (optional)

Output layout:
  <out_dir>/episodeXX_tYYYY.npz

Each NPZ may contain (depending on what exists on disk):
  - rgb_cam: (H, W, 3) uint8
  - depth_cam: (H, W) float32 (raw depth)
  - rgb_tactile_left/right: (H, W, 3) uint8
  - pc: (P, 3) float32 (optionally sampled to `--pc_num_points`)
  - action: (7,) float32 (pads/clamps; last dim reserved for gripper, set to 0.0)
  - eef_pose_w: (10,) float32 (pads/clamps; last dim reserved for gripper, set to 0.0)
"""

import argparse
import concurrent.futures
import csv
import glob
import multiprocessing
import os
from collections import OrderedDict
from typing import Dict, List, Optional, Sequence, Set, Tuple

import numpy as np
from PIL import Image


def _read_uint8_png(path: str) -> np.ndarray:
    with Image.open(path) as im:
        im = im.convert("RGB")
        return np.asarray(im, dtype=np.uint8)


def _read_depth_npy(path: str) -> np.ndarray:
    arr = np.load(path)
    if arr.ndim == 3 and arr.shape[0] == 1:
        arr = arr[0]
    return arr.astype(np.float32, copy=False)


def _parse_semicolon_floats(s: str) -> List[float]:
    s = (s or "").strip()
    if not s:
        return []
    out: List[float] = []
    for p in [p.strip() for p in s.split(";") if p.strip()]:
        try:
            out.append(float(p))
        except Exception:
            continue
    return out


def _list_episode_dirs(root: str) -> List[str]:
    return sorted([d for d in glob.glob(os.path.join(root, "episode*")) if os.path.isdir(d)])


def _read_csv_rows(csv_path: str) -> List[Dict[str, str]]:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    rows: List[Dict[str, str]] = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def _frame_has_any_modalities(ep_dir: str, frame: int) -> bool:
    fname = f"{frame:04d}"
    if os.path.isfile(os.path.join(ep_dir, "rgb_cam", f"{fname}.png")):
        return True
    if os.path.isfile(os.path.join(ep_dir, "depth_cam", f"{fname}.npy")):
        return True
    if os.path.isfile(os.path.join(ep_dir, "rgb_tactile_left", f"{fname}.png")):
        return True
    if os.path.isfile(os.path.join(ep_dir, "rgb_tactile_right", f"{fname}.png")):
        return True
    if os.path.isfile(os.path.join(ep_dir, "pc", f"{fname}.npy")):
        return True
    return False


def _sample_rows_fixed(n_rows: int, n: int, rng: np.random.Generator):
    """Return indices to sample `n_rows` rows to exactly `n` rows."""
    if n is None or n <= 0:
        return slice(None)
    if n_rows <= 0:
        return np.arange(0, dtype=np.int64)
    if n_rows >= n:
        idx = rng.choice(n_rows, size=n, replace=False)
    else:
        idx = rng.choice(n_rows, size=n, replace=True)
    return idx.astype(np.int64)


def _collect_modalities_for_frame(ep_dir: str, frame: int, include_images: bool) -> Dict[str, object]:
    fname = f"{frame:04d}"
    out: Dict[str, object] = {}
    if not include_images:
        return out

    rgb_path = os.path.join(ep_dir, "rgb_cam", f"{fname}.png")
    if os.path.isfile(rgb_path):
        try:
            out["rgb_cam"] = _read_uint8_png(rgb_path)
        except Exception:
            pass

    depth_path = os.path.join(ep_dir, "depth_cam", f"{fname}.npy")
    if os.path.isfile(depth_path):
        try:
            out["depth_cam"] = _read_depth_npy(depth_path)
        except Exception:
            pass

    tl_path = os.path.join(ep_dir, "rgb_tactile_left", f"{fname}.png")
    if os.path.isfile(tl_path):
        try:
            out["rgb_tactile_left"] = _read_uint8_png(tl_path)
        except Exception:
            pass
    tr_path = os.path.join(ep_dir, "rgb_tactile_right", f"{fname}.png")
    if os.path.isfile(tr_path):
        try:
            out["rgb_tactile_right"] = _read_uint8_png(tr_path)
        except Exception:
            pass

    return out


def _ensure_action7(action_vals: Sequence[float]) -> np.ndarray:
    arr = np.asarray(action_vals, dtype=np.float32).reshape(-1)
    if arr.size >= 7:
        out = arr[:7].astype(np.float32, copy=True)
        out[-1] = 0.0
        return out
    pad = np.zeros((7 - arr.size,), dtype=np.float32)
    out = np.concatenate([arr, pad], axis=0).astype(np.float32)
    out[-1] = 0.0
    return out


def _ensure_eef_pose10(eef_vals: Sequence[float]) -> np.ndarray:
    arr = np.asarray(eef_vals, dtype=np.float32).reshape(-1)
    if arr.size >= 10:
        out = arr[:10].astype(np.float32, copy=True)
        out[-1] = 0.0
        return out
    pad = np.zeros((10 - arr.size,), dtype=np.float32)
    out = np.concatenate([arr, pad], axis=0).astype(np.float32)
    out[-1] = 0.0
    return out


def _get_already_converted_episodes(out_dir: str) -> Set[str]:
    pattern = os.path.join(out_dir, "episode*_t*.npz")
    files = glob.glob(pattern)
    episodes: Set[str] = set()
    for f in files:
        base = os.path.basename(f)
        if "_t" in base:
            episodes.add(base.split("_t", 1)[0])
    return episodes


def _convert_single_episode(
    ep_dir: str,
    out_dir: str,
    pc_num_points: int,
    seed: int,
    compress: bool,
    pc_only: bool,
) -> None:
    ep_name = os.path.basename(os.path.normpath(ep_dir))
    csv_path = os.path.join(ep_dir, "timestamps_robot.csv")

    try:
        rows = _read_csv_rows(csv_path)
    except Exception as e:
        print(f"[Skip] {ep_name}: failed to read CSV: {e}")
        return

    rng = np.random.default_rng(seed)

    for row in rows:
        try:
            frame_idx = int(float(row.get("frame", "0")))
        except Exception:
            continue

        if not _frame_has_any_modalities(ep_dir, frame_idx):
            continue

        save_dict: Dict[str, object] = OrderedDict()
        save_dict.update(_collect_modalities_for_frame(ep_dir, frame_idx, include_images=not pc_only))

        pc_path = os.path.join(ep_dir, "pc", f"{frame_idx:04d}.npy")
        if os.path.isfile(pc_path):
            try:
                pc_xyz = np.load(pc_path).astype(np.float32, copy=False)
                if pc_xyz.ndim == 2 and pc_xyz.shape[1] >= 3:
                    pc_xyz = pc_xyz[:, :3]
                    if pc_num_points and pc_num_points > 0:
                        idx = _sample_rows_fixed(pc_xyz.shape[0], pc_num_points, rng)
                        pc_xyz = pc_xyz[idx, :] if not isinstance(idx, slice) else pc_xyz
                    save_dict["pc"] = pc_xyz.astype(np.float32, copy=False)
            except Exception:
                pass

        action_vals = _parse_semicolon_floats(row.get("action", ""))
        eef_vals = _parse_semicolon_floats(row.get("eef_pose_w", ""))
        save_dict["action"] = _ensure_action7(action_vals)
        save_dict["eef_pose_w"] = _ensure_eef_pose10(eef_vals)

        out_name = f"{ep_name}_t{frame_idx:04d}.npz"
        out_path = os.path.join(out_dir, out_name)
        if compress:
            np.savez_compressed(out_path, **save_dict)
        else:
            np.savez(out_path, **save_dict)


def convert_episodes(
    episodes_root: str,
    out_dir: str,
    pc_num_points: int,
    pc_random_seed: int,
    num_workers: int = 0,
    compress: bool = True,
    pc_only: bool = False,
    start_from: Optional[str] = None,
) -> None:
    os.makedirs(out_dir, exist_ok=True)
    episode_dirs = _list_episode_dirs(episodes_root)
    if not episode_dirs:
        raise FileNotFoundError(f"No episode* directories under: {episodes_root}")

    start_from_index: Optional[int] = None
    if start_from:
        for idx, ep_dir in enumerate(episode_dirs):
            if os.path.basename(os.path.normpath(ep_dir)) == start_from:
                start_from_index = idx
                break

    already = _get_already_converted_episodes(out_dir)

    tasks: List[Tuple[str, str, int, int, bool, bool]] = []
    for i, ep_dir in enumerate(episode_dirs):
        ep_name = os.path.basename(os.path.normpath(ep_dir))
        force = start_from_index is not None and i >= start_from_index

        if not force and ep_name in already:
            continue

        if force and ep_name in already:
            for f in glob.glob(os.path.join(out_dir, f"{ep_name}_t*.npz")):
                try:
                    os.remove(f)
                except OSError:
                    pass

        tasks.append((ep_dir, out_dir, pc_num_points, pc_random_seed + i, compress, pc_only))

    if not tasks:
        print("[convert_to_npz] Nothing to do (all episodes already converted).")
        return

    max_workers = int(num_workers) if int(num_workers) > 0 else multiprocessing.cpu_count()
    print(f"[convert_to_npz] Converting {len(tasks)} episodes with {max_workers} worker(s)...")

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as ex:
        futs = [ex.submit(_convert_single_episode, *t) for t in tasks]
        for fut in concurrent.futures.as_completed(futs):
            fut.result()

    print("[convert_to_npz] Done.")


def main() -> None:
    ap = argparse.ArgumentParser(description="Convert FactoryIL episodes to per-frame NPZ files.")
    ap.add_argument("--episodes_root", "-i", required=True, help="Root directory containing episodeXX folders.")
    ap.add_argument("--out_dir", "-o", required=True, help="Output directory for episodeXX_tYYYY.npz files.")
    ap.add_argument("--pc_num_points", type=int, default=0, help="If >0, sample PCs to exactly this many points.")
    ap.add_argument("--pc_random_seed", type=int, default=0, help="Random seed for point sampling.")
    ap.add_argument("--num_workers", "-n", type=int, default=0, help="Parallel workers (0=all CPUs).")
    ap.add_argument(
        "--uncompressed",
        action="store_true",
        help="Save NPZ without compression (faster I/O, larger files).",
    )
    ap.add_argument(
        "--pc_only",
        action="store_true",
        help="Only include pc + (action,eef_pose_w) in NPZs (skip images).",
    )
    ap.add_argument(
        "--start_from",
        type=str,
        default=None,
        help="Re-convert episodes from this episodeXX onward (overwriting existing NPZs).",
    )
    args = ap.parse_args()

    convert_episodes(
        episodes_root=os.path.abspath(args.episodes_root),
        out_dir=os.path.abspath(args.out_dir),
        pc_num_points=int(args.pc_num_points),
        pc_random_seed=int(args.pc_random_seed),
        num_workers=int(args.num_workers),
        compress=not bool(args.uncompressed),
        pc_only=bool(args.pc_only),
        start_from=args.start_from,
    )


if __name__ == "__main__":
    main()


