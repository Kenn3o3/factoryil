"""Configuration for FactoryIL teleoperation environments.

This module mirrors the TacEx factory task configuration but is simplified and
retargeted for imitation learning / teleoperation:

- Uses a high-PD Franka + GelSight Mini gripper configuration suitable for
  differential IK control.
- Reuses TacEx factory assets (peg/hole, gears, nut/bolt) via
  :mod:`tacex_factory_core.factory_tasks_cfg`.
- Adds a small IK control config (:class:`IKCtrlCfg`) for SE(3) delta actions.
"""

from __future__ import annotations

from typing import Optional

import isaaclab.sim as sim_utils
import isaacsim.core.utils.torch as torch_utils
import numpy as np
import torch
from isaaclab.actuators.actuator_cfg import ImplicitActuatorCfg  # noqa: F401  (kept for future extensions)
from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import PhysxCfg, SimulationCfg
from isaaclab.sim.spawners.materials.physics_materials_cfg import RigidBodyMaterialCfg
from isaaclab.sensors.camera import CameraCfg
from isaaclab.sim.spawners.sensors import PinholeCameraCfg
from isaaclab.utils import configclass
from tacex_assets.sensors.gelsight_mini.gsmini_cfg import GelSightMiniCfg
from tacex_assets.robots.franka.franka_gsmini_gripper_rigid import (
    FRANKA_PANDA_ARM_GSMINI_GRIPPER_HIGH_PD_RIGID_CFG,
)
from tacex_factory_core.factory_tasks_cfg import FactoryTask, GearMesh, NutThread, PegInsert


@configclass
class IKCtrlCfg:
    """High-level control parameters for differential IK teleoperation."""

    # Per-step scaling for SE(3) delta actions (delta from Se3Keyboard).
    # Match the official stack IK-rel env, which uses `scale=0.5` on the 6D
    # pose command inside DifferentialInverseKinematicsActionCfg.
    pos_scale: list[float] = [0.75, 0.75, 0.75]
    rot_scale: list[float] = [0.75, 0.75, 0.75]
    # Safety clamps on commanded deltas (meters / radians).
    max_pos_delta: list[float] = [0.5, 0.5, 0.5]
    max_rot_delta: list[float] = [1.0, 1.0, 1.0]
    # Gripper limits in joint-position units (meters of finger travel).
    gripper_open_pos: float = 0.04
    gripper_close_pos: float = -0.3


def _default_camera_cfg() -> CameraCfg:
    """Static overhead pinhole camera matching the TacEx factory setup."""

    cam_pos = (1.9, 0.0, 0.2)
    roll_deg, pitch_deg, yaw_deg = 90.0, 00.0, 90.0
    cam_euler_rad = torch.tensor(
        [np.deg2rad(roll_deg), np.deg2rad(pitch_deg), np.deg2rad(yaw_deg)],
        dtype=torch.float32,
    )
    cam_quat_wxyz = torch_utils.quat_from_euler_xyz(
        cam_euler_rad[0], cam_euler_rad[1], cam_euler_rad[2]
    )
    cam_quat_list = cam_quat_wxyz.tolist()

    return CameraCfg(
        prim_path="/World/envs/env_.*/camera",
        update_period=0.0,
        height=480,
        width=640,
        data_types=[
            "rgb",
            "distance_to_image_plane",
            "distance_to_camera",
            "instance_id_segmentation_fast",
        ],
        colorize_instance_id_segmentation=False,
        spawn=PinholeCameraCfg(focal_length=24.0, horizontal_aperture=20.955),
        offset=CameraCfg.OffsetCfg(pos=cam_pos, rot=cam_quat_list, convention="local"),
    )


@configclass
class InitAssetsCfg:
    """Configurable initial poses for fixed and held assets (world frame)."""

    fixed_pos: list[float] = [0.6, 0.0, 0.05]
    fixed_rot: list[float] = [1.0, 0.0, 0.0, 0.0]
    held_pos: list[float] = [0.6, 0.0, 0.05]
    held_rot: list[float] = [1.0, 0.0, 0.0, 0.0]
    # If True, override held_pos/held_rot and spawn the held asset already
    # grasped in the robot gripper in the current EE pose (peg-in-gripper
    # behaviour like TacEx).
    spawn_in_gripper: bool = True


@configclass
class InitRobotCfg:
    """Configurable initial joint pose for the Franka arm + gripper."""

    # Arm joints: match official stack IK-rel teleop pose.
    joint_pos: list[float] = [
        0.0444,
        -0.1894,
        -0.1107,
        -2.5148,
        0.0044,
        2.3775,
        0.6952,
    ]
    # Symmetric finger opening (meters).
    gripper_width: float = 0.04


@configclass
class FactoryILEnvCfg(DirectRLEnvCfg):
    """Base configuration for FactoryIL environments."""

    # Core settings (DirectRLEnv expects these fields).
    decimation: int = 2
    action_space: int = 7  # 6D EE delta pose + 1D gripper
    # The exact observation dimension is finalized in the env constructor, but
    # we set a sane default here (joint pos/vel + EE pose + gripper width).
    observation_space: int = 22
    state_space: Optional[int] = None

    # Task definition (reused from TacEx).
    task_name: str = "peg_insert"
    task: FactoryTask = FactoryTask()

    # High-level IK control knobs.
    ctrl: IKCtrlCfg = IKCtrlCfg()

    # Episode length (seconds).
    episode_length_s: float = 10.0

    # Simulation configuration: align with official teleop timing (StackEnvCfg).
    sim: SimulationCfg = SimulationCfg(
        device="cuda:0",
        dt=0.01,  # 100 Hz physics like StackEnvCfg
        gravity=(0.0, 0.0, -9.81),
        physx=PhysxCfg(
            # solver_type=1,
            # max_position_iteration_count=192,
            # max_velocity_iteration_count=1,
            # bounce_threshold_velocity=0.2,
            # friction_offset_threshold=0.01,
            # friction_correlation_distance=0.00625,
            # gpu_max_rigid_contact_count=2**25,
            # gpu_max_rigid_patch_count=2**25,
            # gpu_max_num_partitions=8,
            # gpu_heap_capacity=512 * 1024 * 1024,
            # gpu_temp_buffer_capacity=256 * 1024 * 1024,
            # gpu_collision_stack_size=128 * 1024 * 1024,
            # gpu_found_lost_pairs_capacity=2**26,
            # gpu_found_lost_aggregate_pairs_capacity=2**24,
            # gpu_total_aggregate_pairs_capacity=2**24,
            solver_type=1,
            max_position_iteration_count=192,  # Important to avoid interpenetration.
            max_velocity_iteration_count=1,
            bounce_threshold_velocity=0.2,
            friction_offset_threshold=0.01,
            friction_correlation_distance=0.00625,
            gpu_max_rigid_contact_count=2**23,
            gpu_max_rigid_patch_count=2**23,
            gpu_max_num_partitions=1,  # Important for stable simulation.
        ),
        physics_material=RigidBodyMaterialCfg(
            static_friction=1.0,
            dynamic_friction=1.0,
        ),
    )

    # Scene layout: single-robot teleop by default, but num_envs can be overridden.
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=1, env_spacing=2.0)

    # High-PD Franka with GelSight Mini gripper (suitable for DIK control).
    robot: ArticulationCfg = FRANKA_PANDA_ARM_GSMINI_GRIPPER_HIGH_PD_RIGID_CFG.replace(
        prim_path="/World/envs/env_.*/Robot",
    )

    # GelSight Mini sensors (same as TacEx FactoryEnvCfg).
    gsmini_left: GelSightMiniCfg = GelSightMiniCfg(
        prim_path="/World/envs/env_.*/Robot/gelsight_mini_case_left",
        sensor_camera_cfg=GelSightMiniCfg.SensorCameraCfg(
            prim_path_appendix="/Camera",
            update_period=0,
            resolution=(32, 32),
        ),
        device="cuda",
        debug_vis=True,
        marker_motion_sim_cfg=None,
        data_types=["tactile_rgb"],
    )

    # Apply optical-sim overrides (copied from TacEx).
    gsmini_left.optical_sim_cfg = gsmini_left.optical_sim_cfg.replace(
        with_shadow=False,
        device="cuda",
        tactile_img_res=(32, 32),
    )

    gsmini_right: GelSightMiniCfg = gsmini_left.replace(
        prim_path="/World/envs/env_.*/Robot/gelsight_mini_case_right",
    )

    # Static overhead camera (for RGB/Depth/segmentation + pointclouds).
    camera_cfg: CameraCfg = _default_camera_cfg()

    # Initial pose configuration for assets and robot (deterministic base pose).
    init_assets: InitAssetsCfg = InitAssetsCfg()
    init_robot: InitRobotCfg = InitRobotCfg()

    # Reset-time initialization noise.
    #
    # Position noise (meters) — max absolute translation noise applied per-axis:
    # - fixed_init_pos_noise: world-frame noise added to the initial hole pose.
    # - held_init_pos_noise:  noise for the initial peg pose; when spawn_in_gripper
    #   is True this is applied in the gripper/fingertip frame, otherwise in world.
    # - eef_init_pos_noise:   world-frame noise applied to the initial end-effector
    #   pose via a single Differential IK step.
    #
    # Orientation noise (radians) — max absolute local axis-angle noise applied
    # per-axis to the held asset (peg) at reset:
    # - held_init_rot_noise:  small random rotation of the peg around its local
    #   axes, either in world frame (spawn_in_gripper=False) or gripper frame
    #   (spawn_in_gripper=True).
    #
    # All defaults are zero so that existing runs remain bitwise-deterministic.
    fixed_init_pos_noise: list[float] = [0.0, 0.0, 0.0]
    held_init_pos_noise: list[float] = [0.0, 0.0, 0.0]
    eef_init_pos_noise: list[float] = [0.0, 0.0, 0.0]
    held_init_rot_noise: list[float] = [0.0, 0.0, 0.0]
    # hole_init_pos_noise: list[float] = [0.0, 0.0, 0.0]
    # hole_init_rot_noise: list[float] = [1.57, 0.0, 0.0]

    def __post_init__(self):
        """Align render interval with teleop settings."""
        # Match StackEnvCfg: render every 2 sim steps by default.
        try:
            self.sim.render_interval = 2
        except Exception:
            pass


@configclass
class FactoryILPegInsertCfg(FactoryILEnvCfg):
    """Peg-insertion variant of the FactoryIL environment."""

    task_name: str = "peg_insert"
    task: FactoryTask = PegInsert()
    episode_length_s: float = 10.0


@configclass
class FactoryILGearMeshCfg(FactoryILEnvCfg):
    """Gear-meshing variant of the FactoryIL environment."""

    task_name: str = "gear_mesh"
    task: FactoryTask = GearMesh()
    episode_length_s: float = 20.0


@configclass
class FactoryILNutThreadCfg(FactoryILEnvCfg):
    """Nut-threading variant of the FactoryIL environment."""

    task_name: str = "nut_thread"
    task: FactoryTask = NutThread()
    episode_length_s: float = 30.0


__all__ = [
    "IKCtrlCfg",
    "FactoryILEnvCfg",
    "FactoryILPegInsertCfg",
    "FactoryILGearMeshCfg",
    "FactoryILNutThreadCfg",
]


