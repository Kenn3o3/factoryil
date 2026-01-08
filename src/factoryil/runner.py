#!/usr/bin/env python
"""
Pick an agent and a task and run it in the FactoryIL environment.

- Agent:
  - ILPolicyAgent (DP / EquiBot / Drift-DP)
  - ExpertAgent (analytic controller)
  - ReplayAgent (replay from a stored episode)
- Task:
  - PegInsertion
  - GearMesh
  - NutThreading
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import time
import torch
from typing import Tuple
from isaaclab.app import AppLauncher

from factoryil import config as C
from factoryil.utils.seed import FACTORYIL_FIXED_SEED, seed_everything
from factoryil.episode_manager import (
    EpisodeStager,
    success_mask,
)
from factoryil.utils.data.observations import build_obs_dict
from factoryil.utils.data.tactile import get_tactile_batch
from factoryil.utils.data.vision import get_object_pointclouds

from factoryil.cli import build_factoryil_runner_parser
from factoryil.agents.expert_agents import ExpertAgent
from factoryil.agents.replay_agents import ReplayAgent

import time

# -----------------------------------------------------------------------------#
# DEBUG helpers (easy to remove): write EEF pose traces + a quick PNG plot.    #
# Enable/disable via env var: FACTORYIL_DEBUG_EEF=1/0 (defaults to 0).         #
# -----------------------------------------------------------------------------#

_DEBUG_EEF_PLOTS = os.environ.get("FACTORYIL_DEBUG_EEF", "0").lower() not in ("0", "false", "no")


def _parse_semicolon_floats(s: str) -> list[float]:
    try:
        return [float(x) for x in str(s).split(";") if x != ""]
    except Exception:
        return []


def _write_eef_debug_artifacts(episode_dir: str) -> None:
    """Write `eef_debug.csv` and `eef_debug.png` into an episode directory."""
    csv_path = os.path.join(episode_dir, "timestamps_robot.csv")
    if not os.path.exists(csv_path):
        return

    steps: list[int] = []
    eef_z: list[float] = []
    yx: list[float] = []
    yy: list[float] = []
    yz: list[float] = []

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                pose = _parse_semicolon_floats(row.get("eef_pose_w", ""))
                # eef_pose_w is [pos(3), x_axis(3), y_axis(3)] -> total 9 floats.
                if len(pose) < 9:
                    continue
                try:
                    steps.append(int(row.get("frame", len(steps))))
                except Exception:
                    steps.append(len(steps))
                eef_z.append(float(pose[2]))
                yx.append(float(pose[6]))
                yy.append(float(pose[7]))
                yz.append(float(pose[8]))
    except Exception:
        return

    if len(steps) < 2:
        return

    # 1) Write a small CSV for quick inspection.
    try:
        out_csv = os.path.join(episode_dir, "eef_debug.csv")
        with open(out_csv, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["step", "eef_z", "eef_yx", "eef_yy", "eef_yz"])
            for i in range(len(steps)):
                w.writerow([steps[i], eef_z[i], yx[i], yy[i], yz[i]])
    except Exception:
        pass

    # 2) Write a quick plot as a PNG using PIL (no matplotlib dependency).
    try:
        from PIL import Image, ImageDraw, ImageFont

        W, H = 1100, 650
        margin = 60
        gap = 40
        panel_h = (H - 2 * margin - gap) // 2
        panel_w = W - 2 * margin

        img = Image.new("RGB", (W, H), "white")
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.load_default()
        except Exception:
            font = None

        def _draw_panel(
            rect: tuple[int, int, int, int],
            series: list[tuple[str, list[float], tuple[int, int, int]]],
            title: str,
        ) -> None:
            x0, y0, x1, y1 = rect
            draw.rectangle(rect, outline=(0, 0, 0), width=1)

            # X scaling from step indices (use min/max).
            xmin = float(min(steps))
            xmax = float(max(steps))
            if abs(xmax - xmin) < 1e-9:
                xmax = xmin + 1.0

            # Y scaling across all series in this panel.
            all_vals: list[float] = []
            for _, vals, _ in series:
                all_vals.extend(vals)
            ymin = float(min(all_vals))
            ymax = float(max(all_vals))
            if abs(ymax - ymin) < 1e-9:
                ymax = ymin + 1e-6
            pad = 0.05 * (ymax - ymin)
            ymin -= pad
            ymax += pad

            def _pt(x: float, y: float) -> tuple[int, int]:
                px = x0 + int(round((x - xmin) / (xmax - xmin) * (x1 - x0)))
                py = y1 - int(round((y - ymin) / (ymax - ymin) * (y1 - y0)))
                return px, py

            # Title + legend.
            draw.text((x0 + 6, y0 + 6), title, fill=(0, 0, 0), font=font)
            legend_y = y0 + 24
            for name, _, color in series:
                draw.line([(x0 + 6, legend_y + 6), (x0 + 26, legend_y + 6)], fill=color, width=3)
                draw.text((x0 + 32, legend_y), name, fill=(0, 0, 0), font=font)
                legend_y += 14

            # Lines.
            for _, vals, color in series:
                pts = [_pt(float(steps[i]), float(vals[i])) for i in range(len(steps))]
                draw.line(pts, fill=color, width=2)

        top = (margin, margin, margin + panel_w, margin + panel_h)
        bot = (margin, margin + panel_h + gap, margin + panel_w, margin + panel_h + gap + panel_h)

        _draw_panel(top, [("eef_z", eef_z, (30, 90, 220))], "EEF z (position) vs step")
        _draw_panel(
            bot,
            [
                ("y_axis.x", yx, (220, 50, 50)),
                ("y_axis.y", yy, (50, 160, 60)),
                ("y_axis.z", yz, (230, 140, 40)),
            ],
            "EEF y-axis (world) components vs step",
        )

        img.save(os.path.join(episode_dir, "eef_debug.png"))
    except Exception:
        # If PIL isn't available or something goes wrong, skip silently.
        pass

def _tensor_like_to_list(x):
    """Convert torch tensors / numpy arrays / lists to plain python lists."""
    try:
        if torch.is_tensor(x):
            return x.detach().to("cpu").tolist()
    except Exception:
        pass
    try:
        import numpy as np  # local import (optional)

        if isinstance(x, np.ndarray):
            return x.tolist()
    except Exception:
        pass
    return x

def _to_jsonable(x):
    """Best-effort convert arbitrary objects into JSON-serializable values."""
    try:
        json.dumps(x)
        return x
    except Exception:
        return str(x)

def _args_to_json_dict(args) -> dict:
    """Convert argparse Namespace to a JSON-serializable dict."""
    out = {}
    try:
        items = vars(args).items()
    except Exception:
        items = []
    for k, v in items:
        out[str(k)] = _to_jsonable(v)
    return out

def _atomic_json_dump(path: str, payload: dict) -> None:
    """Write JSON atomically to avoid partial files if the process is killed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp_path = f"{path}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=False)
    os.replace(tmp_path, path)

def _maybe_write_camera_params_json(env, data_root: str, failed_root: str) -> None:
    """
    Save the *actual* camera parameters used during collection to:
      - <data_root>/camera_params.json
      - <failed_root>/camera_params.json

    `episode_to_video` can then auto-discover these to project the EEF marker.
    """
    out_path = os.path.join(data_root, "camera_params.json")
    out_failed = os.path.join(failed_root, "camera_params.json")

    cam = getattr(env.unwrapped, "camera", None)
    if cam is None:
        return

    # Ensure sensors have produced at least one update (best-effort).
    try:
        env.unwrapped.sim.render()
    except Exception:
        pass

    # Env origins are the per-env "world origin" offsets used across the scene.
    env_origins = None
    try:
        env_origins = _tensor_like_to_list(env.scene.env_origins)
    except Exception:
        env_origins = None

    # Camera pose/intrinsics are typically per-env (N, ...).
    pos_w = None
    quat_w_ros = None
    quat_w_world = None
    Ks = None
    try:
        pos_w = _tensor_like_to_list(cam.data.pos_w)
    except Exception:
        pass
    try:
        quat_w_ros = _tensor_like_to_list(cam.data.quat_w_ros)
    except Exception:
        pass
    # Some IsaacLab versions also expose quat_w (world convention).
    try:
        quat_w_world = _tensor_like_to_list(getattr(cam.data, "quat_w", None))
    except Exception:
        quat_w_world = None
    try:
        Ks = _tensor_like_to_list(cam.data.intrinsic_matrices)
    except Exception:
        pass

    # Determine the camera's native output image shape (H, W).
    image_shape = None
    try:
        rgb = cam.data.output.get("rgb", None)
        if rgb is not None and hasattr(rgb, "shape") and len(rgb.shape) >= 3:
            image_shape = [int(rgb.shape[1]), int(rgb.shape[2])]
    except Exception:
        image_shape = None
    if image_shape is None:
        # Fall back to configured camera resolution.
        try:
            image_shape = [int(env.cfg.camera_cfg.height), int(env.cfg.camera_cfg.width)]
        except Exception:
            image_shape = [int(C.RGB_H), int(C.RGB_W)]

    meta = {
        "generated_by": "factoryil.runner",
        "generated_at_unix_s": time.time(),
        "num_envs": int(getattr(env.unwrapped, "num_envs", 0) or 0),
        "env_origins": env_origins if env_origins is not None else [],
        "camera": {
            "pos_w": pos_w if pos_w is not None else [],
            "quat_w_ros": quat_w_ros if quat_w_ros is not None else [],
            "quat_w_world": quat_w_world if quat_w_world is not None else [],
            "intrinsic_matrices": Ks if Ks is not None else [],
            "image_shape": image_shape,
            "orientation_convention": "ros",
        },
    }

    # Backup existing file if it differs (keeps old datasets reproducible).
    try:
        if os.path.exists(out_path):
            existing = None
            try:
                with open(out_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
            except Exception:
                existing = None
            if existing != meta:
                ts = time.strftime("%Y%m%d_%H%M%S")
                shutil.copy2(out_path, f"{out_path}.bak_{ts}")
    except Exception:
        pass

    try:
        _atomic_json_dump(out_path, meta)
    except Exception:
        return

    # Keep a copy under FAILED/ so offline tooling works there too.
    try:
        _atomic_json_dump(out_failed, meta)
    except Exception:
        pass

def _alloc_roots_for_expert(args) -> Tuple[str, str, str, str]:
    """Return (dataset_root, success_root, failed_root, staging_root) for writing episodes."""
    dataset_root = os.path.abspath(args.data_dir)
    success_root = os.path.join(dataset_root, "SUCCESS")
    failed_root = os.path.join(dataset_root, "FAILED")
    staging_root = os.path.join(dataset_root, ".staging")
    for p in (dataset_root, success_root, failed_root, staging_root):
        os.makedirs(p, exist_ok=True)
    return dataset_root, success_root, failed_root, staging_root

@torch.no_grad()
def _run_peg_insert_with_agent(args, env, agent) -> dict | None:
    """Shared peg-insertion rollout for any agent."""
    device = env.device
    num_envs: int = env.unwrapped.num_envs
    action_dim: int = env.unwrapped.cfg.action_space

    mode = str(getattr(args, "mode", "collect")).lower().strip()
    if mode not in ("collect", "evaluate"):
        mode = "collect"

    dataset_root, success_root, failed_root, staging_root = _alloc_roots_for_expert(args)
    wrote_cam_params = False

    zero_action = torch.zeros((num_envs, action_dim), device=device)
    discard_timeouts = bool(getattr(args, "discard_timeouts", False))
    # Evaluate mode always counts failures; keep them on disk for inspection.
    if mode == "evaluate":
        discard_timeouts = False

    target_episodes = int(args.episodes)
    total_success = 0
    episodes_ended = 0
    episodes_succeeded = 0

    batch_idx = 0

    def _should_stop() -> bool:
        if mode == "collect":
            return total_success >= target_episodes
        # evaluate: run exactly N total episodes (success + fail)
        return episodes_ended >= target_episodes

    def _accept_episode() -> bool:
        """Whether we should save/count another episode given the current budget."""
        if mode == "evaluate":
            return episodes_ended < target_episodes
        # collect: once we have enough successes, stop saving anything else
        return total_success < target_episodes
    tt0 = time.time()
    while not _should_stop():
        batch_idx += 1
        if mode == "collect":
            print(
                f"[FACTORYIL] Starting batch {batch_idx} | "
                f"successes={total_success}/{target_episodes}",
                flush=True,
            )
        else:
            print(
                f"[FACTORYIL] Starting batch {batch_idx} | "
                f"episodes={episodes_ended}/{target_episodes} successes={total_success}",
                flush=True,
            )

        # ------------------------------------------------------------------ #
        # 1) Episode start: reset buffers.                                   #
        # ------------------------------------------------------------------ #
        # Re-seed at the start of each batch so that reset-time randomization
        # (which uses torch.rand internally) is deterministic across runs, and
        # so IL policy sampling (diffusion) is deterministic per batch.
        batch_seed = int(FACTORYIL_FIXED_SEED + batch_idx)
        seed_everything(batch_seed, deterministic=True)
        raw_obs, _ = env.reset(seed=batch_seed)
        if not wrote_cam_params:
            # Persist camera params once per dataset root for offline video tooling.
            _maybe_write_camera_params_json(
                env, data_root=dataset_root, failed_root=failed_root
            )
            wrote_cam_params = True
        # IMPORTANT: each env.reset() starts a fresh episode batch, so reset the
        # agent's per-episode/buffer state as well (IL agents keep history).
        try:
            agent.reset(num_envs)
        except Exception:
            pass

        env._compute_intermediate_values()
        step_idx = 0

        # One stager per env.
        stagers = [EpisodeStager(staging_root) for _ in range(num_envs)]
        env_done = torch.zeros(num_envs, dtype=torch.bool, device=device)
        env_first = torch.ones(num_envs, dtype=torch.bool, device=device)

        # Determine step cap from env's configured episode length.
        max_len = int(getattr(env.unwrapped, "max_episode_length", 0))
        if max_len <= 0:
            max_len = 1000
        step_cap = max_len

        modality_cfg = C.ModalityConfig(
            use_rgb=True,
            use_depth=True,
            use_tactile=True,
            use_pc=False,
            stack_rgb=C.STACK_RGB,
        )

        while True:
            try:
                env.unwrapped.sim.render()
            except Exception:
                pass

            if step_idx % 10 == 0:
                active_envs = int((~env_done).sum().item())
                if mode == "collect":
                    print(
                        f"[FACTORYIL] batch={batch_idx} step={step_idx} "
                        f"active_envs={active_envs} successes={total_success}/{target_episodes}",
                        flush=True,
                    )
                else:
                    print(
                        f"[FACTORYIL] batch={batch_idx} step={step_idx} "
                        f"active_envs={active_envs} episodes={episodes_ended}/{target_episodes} successes={total_success}",
                        flush=True,
                    )

            # ------------------------------------------------------------------
            # 2) Pre-step observations in world frames.                        #
            # ------------------------------------------------------------------
            obs_pre = build_obs_dict(
                env,
                raw_obs,
                modality_cfg,
                device,
            )

            rgb_pre = obs_pre.get("rgb_camera", None)
            depth_pre = obs_pre.get("depth_camera", None)
            proprio_pre = obs_pre["proprio"]
            eef_pose_pre = obs_pre["eef_pose_w"]

            # Tactile images.
            try:
                tl_pre, tr_pre = get_tactile_batch(
                    env,
                    tact_h=C.TACT_H,
                    tact_w=C.TACT_W,
                    device=device,
                )
            except Exception:
                tl_pre, tr_pre = (None, None)

            # Optional per-frame point clouds: env/world frames.
            pc_env_pre = [None for _ in range(num_envs)]
            # Compute per-frame PCs when:
            #   - explicit --save_pc is requested (for logging), or
            #   - the agent itself uses point clouds (obs_mode startswith "pc").
            wants_pc = bool(getattr(args, "save_pc", False))
            if hasattr(agent, "obs_mode"):
                try:
                    if str(getattr(agent, "obs_mode", "")).startswith("pc"):
                        wants_pc = True
                except Exception:
                    pass
            if wants_pc:
                try:
                    pcs_fixed_world, _ = get_object_pointclouds(
                        env,
                        max_points=int(getattr(args, "pc_max_points", 4096)),
                        device=device,
                    )
                except Exception:
                    pcs_fixed_world = None
                if pcs_fixed_world is not None:
                    try:
                        env_origins = env.scene.env_origins.to(device)
                        for i in range(num_envs):
                            pc_i = pcs_fixed_world[i]
                            if pc_i is None or pc_i.numel() == 0:
                                continue
                            # Per-env frame: subtract this env's origin.
                            pc_env_i = pc_i.to(device) - env_origins[i].unsqueeze(0)
                            pc_env_pre[i] = pc_env_i
                    except Exception:
                        pc_env_pre = [None for _ in range(num_envs)]

            # ------------------------------------------------------------------
            # 3) Agent control in world frame.                                 #
            # ------------------------------------------------------------------
            # Build per-env rich observation dicts; agents decide which
            # modalities to use (ILPolicyAgent keeps its own history).
            is_pc_agent = bool(
                hasattr(agent, "obs_mode")
                and str(getattr(agent, "obs_mode", "")).startswith("pc")
            )

            obs_batch = []
            for i in range(num_envs):
                obs_i = {}

                # State for IL / generic agents: always world-frame.
                state_i = eef_pose_pre[i]
                obs_i["state"] = state_i

                # Optional point cloud (env frame) for PC-mode IL agents.
                pc_i = None
                if is_pc_agent or wants_pc:
                    pc_i = pc_env_pre[i]
                if pc_i is not None:
                    obs_i["pc"] = pc_i

                # RGB / tactile views (as RGB images).
                rgb_views = {}
                if rgb_pre is not None and rgb_pre[i] is not None:
                    rgb_views["rgb_cam"] = rgb_pre[i]
                if tl_pre is not None and tl_pre[i] is not None:
                    rgb_views["rgb_tactile_left"] = tl_pre[i]
                if tr_pre is not None and tr_pre[i] is not None:
                    rgb_views["rgb_tactile_right"] = tr_pre[i]
                if rgb_views:
                    obs_i["rgb"] = rgb_views

                # Low-level proprio / poses kept for potential future agents.
                obs_i["proprio"] = proprio_pre[i]
                obs_i["eef_pose_w"] = eef_pose_pre[i]

                obs_batch.append(obs_i)

            done_mask_np = env_done.detach().to("cpu").numpy().astype(bool)
            
            # t0 = time.time()
            actions = agent.act(obs_batch, done_mask_np, env, t_step=step_idx)
            # t1 = time.time()
            # time_used = t1 - t0
            # print(f"Execution time: {time_used} seconds")
            
            # ------------------------------------------------------------------
            # 4) Logging at time t.                                            #
            # ------------------------------------------------------------------
            for i in range(num_envs):
                if bool(env_done[i].item()):
                    continue
                stagers[i].add_frame(
                    rgb_chw=(rgb_pre[i] if rgb_pre is not None else None),
                    depth_chw=(depth_pre[i] if depth_pre is not None else None),
                    tact_left_chw=(tl_pre[i] if tl_pre is not None else None),
                    tact_right_chw=(tr_pre[i] if tr_pre is not None else None),
                    proprio_1d=proprio_pre[i],
                    action_1d=actions[i],
                    eef_pose_1d=eef_pose_pre[i],
                    is_first=bool(env_first[i].item()),
                    is_last=False,
                    pc_xyz=pc_env_pre[i],
                )
                env_first[i] = False

            # Step environment.
            raw_obs, _, terminated, truncated, _ = env.step(actions)
            # Success signal.
            succ = success_mask(env)
            ended_flags = (terminated.to(torch.bool) | truncated.to(torch.bool))

            # For envs that have just succeeded or ended, append a final zero-action frame.
            if bool((succ | ended_flags).any().item()):
                obs_post = build_obs_dict(
                    env,
                    raw_obs,
                    modality_cfg,
                    device,
                )
                rgb_post = obs_post.get("rgb_camera", None)
                depth_post = obs_post.get("depth_camera", None)
                proprio_post = obs_post["proprio"]
                eef_pose_post = obs_post["eef_pose_w"]

                try:
                    tl_post, tr_post = get_tactile_batch(
                        env,
                        tact_h=C.TACT_H,
                        tact_w=C.TACT_W,
                        device=device,
                    )
                except Exception:
                    tl_post, tr_post = (None, None)

                pc_env_post = [None for _ in range(num_envs)]
                if getattr(args, "save_pc", False):
                    try:
                        pcs_fixed_world_post, _ = get_object_pointclouds(
                            env,
                            max_points=int(getattr(args, "pc_max_points", 4096)),
                            device=device,
                        )
                    except Exception:
                        pcs_fixed_world_post = None
                    if pcs_fixed_world_post is not None:
                        try:
                            env_origins = env.scene.env_origins.to(device)
                            for i in range(num_envs):
                                pc_i = pcs_fixed_world_post[i]
                                if pc_i is None or pc_i.numel() == 0:
                                    continue
                                pc_env_i = pc_i.to(device) - env_origins[i].unsqueeze(0)
                                pc_env_post[i] = pc_env_i
                        except Exception:
                            pc_env_post = [None for _ in range(num_envs)]

                for i in range(num_envs):
                    if bool(env_done[i].item()):
                        continue

                    is_succ = bool(succ[i].item())
                    ended = bool(ended_flags[i].item())

                    if is_succ:
                        if not _accept_episode():
                            stagers[i].discard()
                            env_done[i] = True
                            continue
                        stagers[i].add_frame(
                            rgb_chw=(rgb_post[i] if rgb_post is not None else None),
                            depth_chw=(depth_post[i] if depth_post is not None else None),
                            tact_left_chw=(tl_post[i] if tl_post is not None else None),
                            tact_right_chw=(tr_post[i] if tr_post is not None else None),
                            proprio_1d=proprio_post[i],
                            action_1d=zero_action[i],
                            eef_pose_1d=eef_pose_post[i],
                            is_first=False,
                            is_last=True,
                            pc_xyz=pc_env_post[i],
                        )
                        origin_i = None
                        try:
                            origin_i = env.scene.env_origins[i]
                        except Exception:
                            origin_i = None
                        dest = stagers[i].finalize(
                            success_root, env_id=i, env_origin=origin_i
                        )
                        if _DEBUG_EEF_PLOTS and isinstance(agent, ExpertAgent):
                            _write_eef_debug_artifacts(dest)

                        total_success += 1
                        episodes_ended += 1
                        episodes_succeeded += 1
                        env_done[i] = True

                        sr = episodes_succeeded / max(1, episodes_ended)
                        print(
                            f"[FACTORYIL] SUCCESS env={i} -> {dest} | "
                            f"success_rate={episodes_succeeded}/{episodes_ended} ({sr:.2%})",
                            flush=True,
                        )

                    elif ended:
                        if not _accept_episode():
                            stagers[i].discard()
                            env_done[i] = True
                            continue
                        if discard_timeouts:
                            stagers[i].discard()
                        else:
                            stagers[i].add_frame(
                                rgb_chw=(rgb_post[i] if rgb_post is not None else None),
                                depth_chw=(depth_post[i] if depth_post is not None else None),
                                tact_left_chw=(tl_post[i] if tl_post is not None else None),
                                tact_right_chw=(tr_post[i] if tr_post is not None else None),
                                proprio_1d=proprio_post[i],
                                action_1d=zero_action[i],
                                eef_pose_1d=eef_pose_post[i],
                                is_first=False,
                                is_last=True,
                                pc_xyz=(pc_env_post[i] if pc_env_post is not None else None),
                            )
                            origin_i = None
                            try:
                                origin_i = env.scene.env_origins[i]
                            except Exception:
                                origin_i = None
                            dest = stagers[i].finalize(
                                failed_root, env_id=i, env_origin=origin_i
                            )
                            if _DEBUG_EEF_PLOTS and isinstance(agent, ExpertAgent):
                                _write_eef_debug_artifacts(dest)

                        episodes_ended += 1
                        env_done[i] = True
                        sr = episodes_succeeded / max(1, episodes_ended)
                        if discard_timeouts:
                            print(
                                f"[FACTORYIL] TIMEOUT env={i} -> discarded | "
                                f"success_rate={episodes_succeeded}/{episodes_ended} ({sr:.2%})",
                                flush=True,
                            )
                        else:
                            print(
                                f"[FACTORYIL] TIMEOUT env={i} -> {dest} | "
                                f"success_rate={episodes_succeeded}/{episodes_ended} ({sr:.2%})",
                                flush=True,
                            )

            step_idx += 1

            if _should_stop():
                break
            if bool(env_done.all().item()):
                break
            if step_idx >= step_cap:
                # Force all unfinished envs to be marked as failed for this batch.
                for i in range(num_envs):
                    if not bool(env_done[i].item()):
                        if not _accept_episode():
                            stagers[i].discard()
                            env_done[i] = True
                            continue
                        if discard_timeouts:
                            stagers[i].discard()
                            dest = None
                        else:
                            origin_i = None
                            try:
                                origin_i = env.scene.env_origins[i]
                            except Exception:
                                origin_i = None
                            dest = stagers[i].finalize(
                                failed_root, env_id=i, env_origin=origin_i
                            )
                        episodes_ended += 1
                        env_done[i] = True
                        sr = episodes_succeeded / max(1, episodes_ended)
                        if discard_timeouts:
                            print(
                                f"[FACTORYIL] STEP_CAP TIMEOUT env={i} -> discarded | "
                                f"success_rate={episodes_succeeded}/{episodes_ended} ({sr:.2%})",
                                flush=True,
                            )
                        else:
                            print(
                                f"[FACTORYIL] STEP_CAP TIMEOUT env={i} -> {dest} | "
                                f"success_rate={episodes_succeeded}/{episodes_ended} ({sr:.2%})",
                                flush=True,
                            )
                break

        # Discard any partially written episodes (should be none, but keep robust).
        for i in range(num_envs):
            if not bool(env_done[i].item()):
                stagers[i].discard()
        tt1 = time.time()
        tt_time_used = tt1 - tt0
    print(
        f"[FACTORYIL DONE] mode={mode} successes_saved={total_success} "
        f"episodes_ended={episodes_ended} | out={dataset_root}, time used={tt_time_used}",
        flush=True,
    )
    if mode == "evaluate":
        failures = max(0, int(episodes_ended) - int(episodes_succeeded))
        sr = float(episodes_succeeded) / float(max(1, episodes_ended))
        summary = {
            "mode": "evaluate",
            "episodes_requested": int(target_episodes),
            "episodes_total": int(episodes_ended),
            "successes": int(episodes_succeeded),
            "failures": int(failures),
            "success_rate": float(sr),
            "args": _args_to_json_dict(args),
            "data_dir": str(dataset_root),
            "success_dir": str(success_root),
            "failed_dir": str(failed_root),
        }
        # Persist alongside the saved episodes for experiment tooling.
        try:
            _atomic_json_dump(os.path.join(dataset_root, "eval_summary.json"), summary)
        except Exception:
            pass
        return summary
    return None


@torch.no_grad()
def run(args, env) -> None:
    """Top-level runner selecting agent and task."""
    print("[FACTORYIL] Starting FactoryIL runner...", flush=True)
    device = env.device
    mode = str(getattr(args, "mode", "collect")).lower().strip()
    if mode not in ("collect", "evaluate"):
        mode = "collect"
    if mode == "evaluate":
        # Machine-readable: print args as JSON at the beginning of evaluation.
        try:
            print(json.dumps(_args_to_json_dict(args)), flush=True)
        except Exception:
            pass

    # Instantiate agent based on CLI.
    agent_name = getattr(args, "agent", "expert")
    if agent_name == "expert":
        agent = ExpertAgent(device=device, expert_cfg=args)
    elif agent_name == "replay":
        if not getattr(args, "episode_dir", None):
            raise ValueError("--episode_dir is required when --agent=replay")
        agent = ReplayAgent(
            device=device,
            episode_dir=args.episode_dir,
        )
    elif agent_name == "il":
        if not getattr(args, "il_config", None):
            raise ValueError("--il_config is required when --agent=il")
        if not getattr(args, "il_ckpt", None):
            raise ValueError("--il_ckpt is required when --agent=il")
        # Optional dependency: IL is only required when actually used.
        from factoryil.agents.il_agents import ILPolicyAgent  # noqa: E402

        agent = ILPolicyAgent(
            il_cfg=args.il_config,
            il_checkpoint=args.il_ckpt,
            device=device,
            args=args,
        )
        # Optional ac_horizon override from CLI (clamped to pred_horizon).
        ac_h_override = getattr(args, "ac_horizon", None)
        if ac_h_override is not None:
            try:
                ac_h_candidate = int(ac_h_override)
                if ac_h_candidate > 0:
                    agent.ac_horizon = min(ac_h_candidate, agent.pred_horizon)
            except Exception:
                pass
    else:
        raise NotImplementedError(
            f"Agent type '{agent_name}' is not yet supported in FactoryIL runner."
        )

    num_envs: int = env.unwrapped.num_envs
    agent.reset(num_envs)

    if args.task != "peg_insert":
        raise NotImplementedError(
            f"Unified runner currently supports only peg_insert, got task={args.task!r}."
        )

    summary = _run_peg_insert_with_agent(args, env, agent)
    if mode == "evaluate" and isinstance(summary, dict):
        # Machine-readable: emit evaluation summary as JSON.
        try:
            print(json.dumps(summary), flush=True)
        except Exception:
            pass

def parse_args() -> argparse.Namespace:
    parser = build_factoryil_runner_parser()
    args = parser.parse_args()
    return args


def main() -> None:
    # Hardcoded deterministic seed for the entire runner process.
    # We also re-apply a derived seed per episode-batch during env.reset.
    seed_everything(FACTORYIL_FIXED_SEED, deterministic=True)

    args = parse_args()

    # Launch Isaac Sim / Isaac Lab.
    app_launcher = AppLauncher(vars(args))
    simulation_app = app_launcher.app

    # Delayed imports that require simulation to be running.
    from factoryil.env.factory_env import FactoryILEnv  # noqa: E402
    from factoryil.env.factory_task_cfg import (  # noqa: E402
        FactoryILPegInsertCfg,
        FactoryILGearMeshCfg,
        FactoryILNutThreadCfg,
    )

    # Configure environment.
    if args.task == "peg_insert":
        env_cfg = FactoryILPegInsertCfg()
    elif args.task == "gear_mesh":
        env_cfg = FactoryILGearMeshCfg()
    elif args.task == "nut_thread":
        env_cfg = FactoryILNutThreadCfg()
    else:
        raise ValueError(f"Unknown task '{args.task}'")
    env_cfg.scene.num_envs = int(args.num_envs)
    # Timeout: either explicit timesteps (preferred for deterministic datasets)
    # or a seconds-based time limit.
    timeout_steps = getattr(args, "timeout_steps", None)
    if timeout_steps is not None:
        # One env step corresponds to dt * decimation seconds.
        step_dt_s = float(env_cfg.sim.dt) * float(getattr(env_cfg, "decimation", 1))
        env_cfg.episode_length_s = float(int(timeout_steps)) * step_dt_s
    else:
        env_cfg.episode_length_s = float(args.timeout_s)
    try:
        env_cfg.sim.render_interval = 1
    except Exception:
        pass

    # Apply initialization noise from CLI (zero by default for deterministic runs).
    if hasattr(args, "rand_eef") and float(args.rand_eef) != 0.0:
        val = abs(float(args.rand_eef))
        env_cfg.eef_init_pos_noise = [val, val, 0.0]
    if hasattr(args, "rand_peg") and float(args.rand_peg) != 0.0:
        val = abs(float(args.rand_peg))
        env_cfg.held_init_pos_noise = [val, 0.0, 0.0]
    if hasattr(args, "rand_hole") and float(args.rand_hole) != 0.0:
        val = abs(float(args.rand_hole))
        env_cfg.fixed_init_pos_noise = [val, val, 0.0]

    env = FactoryILEnv(env_cfg)

    try:
        run(args, env)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            env.close()
        except Exception:
            pass
        try:
            simulation_app.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()