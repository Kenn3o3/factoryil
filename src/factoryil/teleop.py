"""Teleoperate FactoryIL environments (Franka + GelSight Mini gripper).

This mirrors the Isaac Lab teleop SE(3) agent but targets FactoryIL's direct env:
  - Tasks: peg_insert, gear_mesh, nut_thread
  - Action space: 7D = [dx, dy, dz, dRx, dRy, dRz, gripper]
    where dR* is axis-angle (radians) and gripper is in [-1, 1]
    (-1 = close, +1 = open).

The goal is to keep CLI usage clean: only task + device are typically specified.
If you want to tune teleop behaviour (step size, clamps, camera on/off), edit the
global variables below.
"""

from __future__ import annotations

import argparse

from isaaclab.app import AppLauncher

# --------------------------------------------------------------------------------------
# User-tweakable defaults (edit these instead of passing long CLI commands)
# --------------------------------------------------------------------------------------

# **Which FactoryIL task to start**
DEFAULT_TASK: str = "peg_insert"  # one of: peg_insert | gear_mesh | nut_thread

# **Which input device to use**
DEFAULT_TELEOP_DEVICE: str = "keyboard"  # one of: keyboard | spacemouse | gamepad

# **How many envs to run**
# Teleop is usually single-env. If >1, the same device command is broadcast to all envs.
DEFAULT_NUM_ENVS: int = 1

# **Teleop device step size**
# These are passed into Isaac Lab's teleop devices.
#
# For keyboard, the command is applied as a per-frame delta when a key is held.
# For SpaceMouse / gamepad, these scale the analog input.
POS_SENSITIVITY: float = 0.05  # meters per step / unit
ROT_SENSITIVITY: float = 0.05  # radians per step / unit
SENSITIVITY_MULT: float = 1.0  # global multiplier on both pos + rot sensitivities

# **Env-side scaling / clamps**
# FactoryILEnv internally scales and clamps the incoming delta pose. These defaults
# match `FactoryILEnvCfg.ctrl` but can be reduced for "slower" teleop.
ENV_POS_SCALE: tuple[float, float, float] = (0.75, 0.75, 0.75)
ENV_ROT_SCALE: tuple[float, float, float] = (0.75, 0.75, 0.75)
ENV_MAX_POS_DELTA: tuple[float, float, float] = (0.50, 0.50, 0.50)  # meters (per env step)
ENV_MAX_ROT_DELTA: tuple[float, float, float] = (1.00, 1.00, 1.00)  # radians (per env step)

# **Avoid automatic timeouts**
# Teleop sessions are typically long-running; use R to reset instead.
DISABLE_EPISODE_TIMEOUT: bool = True
EPISODE_LENGTH_S: float = 3600.0  # only used when DISABLE_EPISODE_TIMEOUT is True

# **Overhead camera sensor**
# Note: to get camera tensors in headless mode, you still need AppLauncher `--enable_cameras`.
ENABLE_OVERHEAD_CAMERA: bool = True
CAMERA_HEIGHT: int = 480
CAMERA_WIDTH: int = 640

# **Rendering cadence**
# Lower render_interval => more frequent rendering (useful for teleop responsiveness).
RENDER_INTERVAL: int = 1

def _pre_process_actions(teleop_data, num_envs: int, device: str):
    """Convert Isaac Lab teleop device output into FactoryIL's 7D action tensor."""

    import numpy as np
    import torch

    delta_pose, gripper_command = teleop_data  # (6,), bool

    # Convert to torch (broadcast to all envs).
    delta_pose_t = torch.tensor(np.asarray(delta_pose), dtype=torch.float32, device=device).view(1, 6)
    delta_pose_t = delta_pose_t.repeat(int(num_envs), 1)

    # IsaacLab devices expose the gripper state as a bool, but their *default* state
    # is typically "open". In FactoryIL tasks the robot starts by holding the asset,
    # so we map the device's default state to "closed" to avoid dropping the object
    # on the first teleop step.
    #
    # FactoryIL convention: -1 = close, +1 = open.
    gripper_t = torch.full(
        (int(num_envs), 1),
        -1.0 if (not gripper_command) else 1.0,
        device=device,
        dtype=torch.float32,
    )

    return torch.cat([delta_pose_t, gripper_t], dim=1)

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Teleoperation for FactoryIL tasks.")
    parser.add_argument(
        "--task",
        type=str,
        default=DEFAULT_TASK,
        choices=["peg_insert", "gear_mesh", "nut_thread"],
        help="FactoryIL task to teleoperate.",
    )
    parser.add_argument(
        "--teleop_device",
        type=str,
        default=DEFAULT_TELEOP_DEVICE,
        choices=["keyboard", "spacemouse", "gamepad"],
        help="Teleop device (keyboard/spacemouse/gamepad).",
    )
    parser.add_argument(
        "--num_envs",
        type=int,
        default=DEFAULT_NUM_ENVS,
        help="Number of parallel FactoryIL envs (device command is broadcast).",
    )
    parser.add_argument(
        "--sensitivity",
        type=float,
        default=SENSITIVITY_MULT,
        help="Multiplier for POS_SENSITIVITY and ROT_SENSITIVITY.",
    )

    # Isaac app args (device, headless, enable_cameras, etc.)
    AppLauncher.add_app_launcher_args(parser)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    # Launch Isaac Sim / Isaac Lab first.
    app_launcher = AppLauncher(vars(args))
    simulation_app = app_launcher.app

    # Delayed imports that require simulation to be running.
    import torch
    from isaaclab.devices import Se3Gamepad, Se3Keyboard, Se3SpaceMouse

    from factoryil.env.factory_env import FactoryILEnv
    from factoryil.env.factory_task_cfg import (
        FactoryILGearMeshCfg,
        FactoryILNutThreadCfg,
        FactoryILPegInsertCfg,
    )

    # ------------------------
    # Configure environment
    # ------------------------
    if args.task == "peg_insert":
        env_cfg = FactoryILPegInsertCfg()
    elif args.task == "gear_mesh":
        env_cfg = FactoryILGearMeshCfg()
    elif args.task == "nut_thread":
        env_cfg = FactoryILNutThreadCfg()
    else:
        raise ValueError(f"Unknown task: {args.task!r}")

    env_cfg.scene.num_envs = int(args.num_envs)
    env_cfg.sim.device = str(args.device)

    # Rendering
    try:
        env_cfg.sim.render_interval = int(max(1, RENDER_INTERVAL))
    except Exception:
        pass

    # Episode timeout
    if DISABLE_EPISODE_TIMEOUT:
        env_cfg.episode_length_s = float(EPISODE_LENGTH_S)

    # Env-side scaling / clamps
    try:
        env_cfg.ctrl.pos_scale = [float(x) for x in ENV_POS_SCALE]
        env_cfg.ctrl.rot_scale = [float(x) for x in ENV_ROT_SCALE]
        env_cfg.ctrl.max_pos_delta = [float(x) for x in ENV_MAX_POS_DELTA]
        env_cfg.ctrl.max_rot_delta = [float(x) for x in ENV_MAX_ROT_DELTA]
    except Exception:
        pass

    # Camera sensor toggle + resolution
    if not ENABLE_OVERHEAD_CAMERA:
        try:
            env_cfg.camera_cfg = None  # type: ignore[assignment]
        except Exception:
            pass
    else:
        try:
            env_cfg.camera_cfg.height = int(max(64, CAMERA_HEIGHT))
            env_cfg.camera_cfg.width = int(max(64, CAMERA_WIDTH))
        except Exception:
            pass

    env = FactoryILEnv(env_cfg)

    # ------------------------
    # Configure teleop device
    # ------------------------
    pos_sens = float(POS_SENSITIVITY) * float(args.sensitivity)
    rot_sens = float(ROT_SENSITIVITY) * float(args.sensitivity)

    if args.teleop_device.lower() == "keyboard":
        teleop = Se3Keyboard(pos_sensitivity=pos_sens, rot_sensitivity=rot_sens)
    elif args.teleop_device.lower() == "spacemouse":
        teleop = Se3SpaceMouse(pos_sensitivity=pos_sens, rot_sensitivity=rot_sens)
    elif args.teleop_device.lower() == "gamepad":
        teleop = Se3Gamepad(pos_sensitivity=pos_sens, rot_sensitivity=rot_sens)
    else:
        raise ValueError(f"Invalid teleop device: {args.teleop_device!r}")

    should_reset = False

    def _request_reset():
        nonlocal should_reset
        should_reset = True

    # Add reset callback for all devices.
    teleop.add_callback("R", _request_reset)

    print(teleop)

    # Reset environment and teleop state.
    env.reset()
    teleop.reset()

    # ------------------------
    # Main loop
    # ------------------------
    try:
        while simulation_app.is_running():
            with torch.inference_mode():
                teleop_data = teleop.advance()
                actions = _pre_process_actions(teleop_data, env.num_envs, env.device)
                env.step(actions)

                if should_reset:
                    env.reset()
                    teleop.reset()
                    should_reset = False
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


