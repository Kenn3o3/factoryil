from __future__ import annotations

from typing import Tuple


def make_env_and_cfg(
    task: str,
    num_envs: int,
    device: str,
    need_camera: bool,
    rgb_h: int,
    rgb_w: int,
    success_frac: float | None = None,
    success_xy_tol_mm: float | None = None,
    render_rgb_array: bool = False,
    deterministic_init: bool = False,
) -> Tuple[object, object]:
    """Convenience helper to create a FactoryIL environment + cfg.

    Returns:
      (env, env_cfg)
    """
    from factoryil.env.factory_env import FactoryILEnv
    from factoryil.env.factory_task_cfg import (
        FactoryILGearMeshCfg,
        FactoryILNutThreadCfg,
        FactoryILPegInsertCfg,
    )

    task_l = str(task).lower()
    if "peg" in task_l:
        env_cfg = FactoryILPegInsertCfg()
    elif "gear" in task_l:
        env_cfg = FactoryILGearMeshCfg()
    elif "nut" in task_l:
        env_cfg = FactoryILNutThreadCfg()
    else:
        raise ValueError(f"Unknown FactoryIL task id: {task!r}")

    env_cfg.scene.num_envs = int(num_envs)
    env_cfg.sim.device = str(device)

    # Optional success criteria overrides.
    if success_frac is not None:
        try:
            env_cfg.task.success_threshold = float(success_frac)
        except Exception:
            pass
    if success_xy_tol_mm is not None:
        try:
            env_cfg.task.xy_success_tol_m = float(success_xy_tol_mm) / 1000.0
        except Exception:
            pass

    if need_camera:
        # Ensure frequent rendering so camera frames update every sim step.
        try:
            env_cfg.sim.render_interval = 1
        except Exception:
            pass
        # Adjust configured camera resolution (best-effort).
        try:
            env_cfg.camera_cfg.height = max(int(rgb_h), 64)
            env_cfg.camera_cfg.width = max(int(rgb_w), 64)
        except Exception:
            pass
    else:
        # Disable camera sensor entirely.
        try:
            env_cfg.camera_cfg = None  # type: ignore[assignment]
        except Exception:
            pass

    if deterministic_init:
        try:
            env_cfg.fixed_init_pos_noise = [0.0, 0.0, 0.0]
            env_cfg.held_init_pos_noise = [0.0, 0.0, 0.0]
            env_cfg.eef_init_pos_noise = [0.0, 0.0, 0.0]
        except Exception:
            pass

    env = FactoryILEnv(env_cfg, render_mode=("rgb_array" if render_rgb_array else None))
    return env, env_cfg


__all__ = ["make_env_and_cfg"]


