#!/usr/bin/env python
from __future__ import annotations

"""Episode staging / dataset writing utilities for FactoryIL.

This module writes simulator-native observations/actions to disk (no extra frame transforms).

On-disk layout for a single episode directory:
  episodeXX/
    rgb_cam/0000.png
    depth_cam/0000.npy (+ optional 0000.png visualization)
    rgb_tactile_left/0000.png
    rgb_tactile_right/0000.png
    pc/0000.npy                        (optional)
    timestamps_robot.csv
    env_id.txt                         (optional)
    env_origin.txt                     (optional)
"""

import os
from typing import Optional

import numpy as np
import torch
from PIL import Image


def _alloc_next_episode_dir(root: str) -> str:
    """Return a new episode directory path filling the lowest missing index."""
    os.makedirs(root, exist_ok=True)
    existing = [
        d
        for d in os.listdir(root)
        if os.path.isdir(os.path.join(root, d)) and d.startswith("episode")
    ]
    used: set[int] = set()
    for d in existing:
        try:
            idx = int(d.replace("episode", ""))
            used.add(idx)
        except Exception:
            continue
    next_idx = 0
    while next_idx in used:
        next_idx += 1
    return os.path.join(root, f"episode{next_idx:02d}")


def _tensor_to_uint8_img(chw: torch.Tensor) -> np.ndarray:
    """Convert CHW float tensor in [0,1] to HWC uint8 numpy image."""
    t = chw
    if t.ndim != 3:
        raise ValueError(f"Expected CHW tensor, got shape {tuple(t.shape)}")
    t = torch.clamp(t, 0.0, 1.0)
    return (t.permute(1, 2, 0) * 255.0).round().to(torch.uint8).cpu().numpy()


class EpisodeStager:
    """Per-env staging writer that writes frames to a temp directory."""

    def __init__(self, staging_root: str):
        import csv
        import uuid

        self.tmp_dir = os.path.join(staging_root, f"env_{uuid.uuid4().hex[:8]}")
        self.rgb_dir = os.path.join(self.tmp_dir, "rgb_cam")
        self.depth_dir = os.path.join(self.tmp_dir, "depth_cam")
        self.tl_dir = os.path.join(self.tmp_dir, "rgb_tactile_left")
        self.tr_dir = os.path.join(self.tmp_dir, "rgb_tactile_right")
        self.pc_dir = os.path.join(self.tmp_dir, "pc")
        for d in (self.tmp_dir, self.rgb_dir, self.depth_dir, self.tl_dir, self.tr_dir, self.pc_dir):
            os.makedirs(d, exist_ok=True)

        self.csv_path = os.path.join(self.tmp_dir, "timestamps_robot.csv")
        self.csv_file = open(self.csv_path, "w", newline="", encoding="utf-8")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(
            ["frame", "is_first", "is_last", "proprio", "action", "eef_pose_w"]
        )

        self.frame_idx = 0
        self.closed = False

    def add_frame(
        self,
        rgb_chw: Optional[torch.Tensor],
        depth_chw: Optional[torch.Tensor],
        tact_left_chw: Optional[torch.Tensor],
        tact_right_chw: Optional[torch.Tensor],
        proprio_1d: torch.Tensor,
        action_1d: torch.Tensor,
        eef_pose_1d: torch.Tensor,
        is_first: bool,
        is_last: bool,
        pc_xyz: Optional[torch.Tensor] = None,
        **_: object,
    ) -> None:
        """Append a frame to the staged episode.

        Extra keyword args are ignored for backwards compatibility.
        """
        if self.closed:
            return

        fname = f"{self.frame_idx:04d}"

        if rgb_chw is not None:
            try:
                Image.fromarray(_tensor_to_uint8_img(rgb_chw)).save(os.path.join(self.rgb_dir, f"{fname}.png"))
            except Exception:
                pass

        # Depth (raw .npy + optional normalized .png for quick inspection).
        depth_hw = None
        if depth_chw is not None:
            try:
                depth_np = depth_chw.detach().to("cpu").numpy()
                if depth_np.ndim == 3 and depth_np.shape[0] == 1:
                    depth_hw = depth_np[0]
                elif depth_np.ndim == 2:
                    depth_hw = depth_np
                else:
                    depth_hw = np.squeeze(depth_np)
                depth_hw = depth_hw.astype(np.float32, copy=False)
                np.save(os.path.join(self.depth_dir, f"{fname}.npy"), depth_hw)
            except Exception:
                depth_hw = None

            if depth_hw is not None:
                try:
                    finite = np.isfinite(depth_hw) & (depth_hw > 0.0)
                    if np.any(finite):
                        dmin = float(np.nanpercentile(depth_hw[finite], 5.0))
                        dmax = float(np.nanpercentile(depth_hw[finite], 95.0))
                        if not np.isfinite(dmin):
                            dmin = 0.0
                        if not np.isfinite(dmax) or dmax <= dmin:
                            dmax = dmin + 1e-6
                        norm = np.clip((depth_hw - dmin) / (dmax - dmin), 0.0, 1.0)
                    else:
                        norm = np.zeros_like(depth_hw, dtype=np.float32)
                    Image.fromarray((norm * 255.0).astype(np.uint8)).save(
                        os.path.join(self.depth_dir, f"{fname}.png")
                    )
                except Exception:
                    pass

        if tact_left_chw is not None:
            try:
                Image.fromarray(_tensor_to_uint8_img(tact_left_chw)).save(os.path.join(self.tl_dir, f"{fname}.png"))
            except Exception:
                pass
        if tact_right_chw is not None:
            try:
                Image.fromarray(_tensor_to_uint8_img(tact_right_chw)).save(os.path.join(self.tr_dir, f"{fname}.png"))
            except Exception:
                pass

        if pc_xyz is not None:
            try:
                np.save(
                    os.path.join(self.pc_dir, f"{fname}.npy"),
                    pc_xyz.detach().to("cpu").numpy().astype(np.float32, copy=False),
                )
            except Exception:
                pass

        proprio_str = ";".join(f"{float(x):.6f}" for x in proprio_1d.detach().cpu().tolist())
        action_str = ";".join(f"{float(x):.6f}" for x in action_1d.detach().cpu().tolist())
        eef_pose_str = ";".join(f"{float(x):.6f}" for x in eef_pose_1d.detach().cpu().tolist())

        self.csv_writer.writerow(
            [self.frame_idx, int(is_first), int(is_last), proprio_str, action_str, eef_pose_str]
        )
        self.frame_idx += 1

    def finalize(self, dataset_root: str, env_id: int, env_origin: Optional[torch.Tensor] = None) -> str:
        """Move staged data to a new episode directory under `dataset_root`."""
        if self.closed:
            return ""

        self.csv_file.flush()
        self.csv_file.close()
        self.closed = True

        import shutil

        dest = _alloc_next_episode_dir(dataset_root)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(self.tmp_dir, dest)

        # Save env id.
        try:
            with open(os.path.join(dest, "env_id.txt"), "w", encoding="utf-8") as f:
                f.write(f"{int(env_id)}\n")
        except Exception:
            pass

        # Save env origin (for aligning world coordinates).
        if env_origin is not None:
            try:
                origin_np = env_origin.detach().to("cpu").numpy().astype(float).tolist()
                with open(os.path.join(dest, "env_origin.txt"), "w", encoding="utf-8") as f:
                    f.write(f"{origin_np[0]} {origin_np[1]} {origin_np[2]}\n")
            except Exception:
                pass

        return dest

    def discard(self) -> None:
        if self.closed:
            return
        try:
            self.csv_file.close()
        except Exception:
            pass
        self.closed = True
        try:
            import shutil

            shutil.rmtree(self.tmp_dir, ignore_errors=True)
        except Exception:
            pass


def success_mask(env) -> torch.Tensor:
    """Per-env success boolean for peg insertion (peg inserted & centered w.r.t. hole)."""
    task = env.cfg.task
    fixed_cfg = getattr(task, "fixed_asset_cfg", None)
    fixed_height = float(getattr(fixed_cfg, "height", 0.0) or 0.0)

    fixed_pos = env._fixed_asset.data.root_pos_w - env.scene.env_origins  # (N, 3)
    held_pos = env._held_asset.data.root_pos_w - env.scene.env_origins  # (N, 3)

    xy_tol = float(getattr(task, "xy_success_tol_m", 0.0025))
    xy_dist = torch.linalg.vector_norm(held_pos[:, 0:2] - fixed_pos[:, 0:2], dim=1)
    xy_ok = xy_dist < xy_tol

    # Insertion depth: how far peg base is below hole base.
    z_disp = held_pos[:, 2] - fixed_pos[:, 2]  # < 0 means below.
    success_threshold = float(getattr(task, "success_threshold", 0.04))
    height_threshold = fixed_height * success_threshold
    z_ok = z_disp < height_threshold

    return xy_ok & z_ok


__all__ = ["EpisodeStager", "success_mask", "_tensor_to_uint8_img"]


