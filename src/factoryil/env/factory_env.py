"""FactoryIL DirectRLEnv with differential IK control for teleoperation.

Key properties:
- 7D action space: 6D relative EE pose (dx, dy, dz, droll, dpitch, dyaw) + 1D gripper
  command (negative = close, positive = open).
- Uses :class:`isaaclab.controllers.DifferentialIKController` to convert SE(3)
  deltas into joint position targets for the Franka arm.
- Deterministic task initialization: fixed asset and held asset start from their
  default USD poses (configurable via the underlying TacEx FactoryTask configs).
- Preserves TacEx GelSight Mini sensors and an overhead static camera; these can
  be accessed directly from the env (for use with the existing tacex_runner
  observation utilities).
"""

from __future__ import annotations

from typing import Sequence, Tuple

import numpy as np
import torch
import isaacsim.core.utils.torch as torch_utils

import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation
from isaaclab.controllers import DifferentialIKController, DifferentialIKControllerCfg
from isaaclab.envs import DirectRLEnv
from isaaclab.sim.spawners.from_files import GroundPlaneCfg, spawn_ground_plane
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

from tacex import GelSightSensor

from .factory_task_cfg import FactoryILEnvCfg


def _axis_angle_to_quat(axis_angle: torch.Tensor) -> torch.Tensor:
    """Convert axis-angle vectors (..., 3) to unit quaternions (..., 4).

    The axis-angle vector encodes axis * angle (radians). This matches the
    convention used by Isaac Lab's DifferentialIKController (6D twist where
    the last 3 entries are an axis-angle rotation vector).
    """
    # axis_angle: (..., 3)
    angles = torch.linalg.vector_norm(axis_angle, dim=-1, keepdim=True)  # (..., 1)
    # Avoid division by zero: for very small angles we simply treat the axis
    # as arbitrary, and the resulting quaternion will be ~identity anyway.
    angles_safe = torch.where(
        angles > 1e-8,
        angles,
        torch.ones_like(angles),
    )
    axis = axis_angle / angles_safe
    half = 0.5 * angles
    sin_half = torch.sin(half)
    cos_half = torch.cos(half)

    quat = torch.zeros(axis_angle.shape[:-1] + (4,), device=axis_angle.device, dtype=axis_angle.dtype)
    quat[..., 0] = cos_half.squeeze(-1)
    quat[..., 1:] = axis * sin_half
    quat = quat / (torch.linalg.vector_norm(quat, dim=-1, keepdim=True) + 1e-8)
    return quat


class FactoryILEnv(DirectRLEnv):
    """DirectRLEnv for factory peg/gear/nut tasks with DIK-based SE(3) control."""

    cfg: FactoryILEnvCfg

    # --------------------------------------------------------------------- #
    # Initialization & scene setup                                          #
    # --------------------------------------------------------------------- #

    def __init__(self, cfg: FactoryILEnvCfg, render_mode: str | None = None, **kwargs):
        # Finalize observation dimension before calling base constructor:
        # proprio = joint_pos(7) + joint_vel(7) + ee_pos(3) + ee_quat(4) + gripper_width(1)
        cfg.observation_space = 7 + 7 + 3 + 4 + 1
        super().__init__(cfg, render_mode, **kwargs)

        # Internal buffers and indices (require scene & robot to be created).
        self._init_indices_and_buffers()
        self._set_contact_friction()
        self._init_ik_controller()
        self._compute_intermediate_values()

    def _setup_scene(self):
        """Create ground, table, robot, assets, and sensors."""
        # Ground plane and table (copied from TacEx factory_env).
        spawn_ground_plane(
            prim_path="/World/ground",
            cfg=GroundPlaneCfg(),
            translation=(0.0, 0.0, -1.05),
        )

        table_cfg = sim_utils.UsdFileCfg(
            usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Mounts/SeattleLabTable/table_instanceable.usd"
        )
        table_cfg.func(
            "/World/envs/env_.*/Table",
            table_cfg,
            translation=(0.55, 0.0, 0.0),
            orientation=(0.70711, 0.0, 0.0, 0.70711),
        )

        # Robot and task assets.
        self._robot = Articulation(self.cfg.robot)
        self._fixed_asset = Articulation(self.cfg.task.fixed_asset)
        self._held_asset = Articulation(self.cfg.task.held_asset)

        # Optional extra gears for the gear-mesh task.
        if self.cfg.task.name == "gear_mesh":
            # TacEx GearMesh task defines additional small / large gears.
            self._small_gear_asset = Articulation(self.cfg.task.small_gear_cfg)
            self._large_gear_asset = Articulation(self.cfg.task.large_gear_cfg)

        # Clone environments and register assets.
        self.scene.clone_environments(copy_from_source=False)

        if self.device == "cpu":
            self.scene.filter_collisions()

        self.scene.articulations["robot"] = self._robot
        self.scene.articulations["fixed_asset"] = self._fixed_asset
        self.scene.articulations["held_asset"] = self._held_asset
        if self.cfg.task.name == "gear_mesh":
            self.scene.articulations["small_gear"] = self._small_gear_asset
            self.scene.articulations["large_gear"] = self._large_gear_asset

        # GelSight sensors (identical to TacEx configuration).
        self.gsmini_left = GelSightSensor(self.cfg.gsmini_left)
        self.scene.sensors["gsmini_left"] = self.gsmini_left

        self.gsmini_right = GelSightSensor(self.cfg.gsmini_right)
        self.scene.sensors["gsmini_right"] = self.gsmini_right

        # Optional overhead camera for RGB/Depth/segmentation.
        if getattr(self.cfg, "camera_cfg", None) is not None:
            from isaaclab.sensors.camera import Camera

            self.camera = Camera(self.cfg.camera_cfg)
            self.scene.sensors["camera"] = self.camera

        # Dome light for basic illumination.
        light_cfg = sim_utils.DomeLightCfg(intensity=2000.0, color=(0.75, 0.75, 0.75))
        light_cfg.func("/World/Light", light_cfg)

    # --------------------------------------------------------------------- #
    # Internal helpers                                                      #
    # --------------------------------------------------------------------- #

    def _set_contact_friction(self):
        """Set material friction for robot and assets to match TacEx factory tasks."""
        task_cfg = self.cfg.task

        def _set_friction(asset: Articulation, value: float):
            materials = asset.root_physx_view.get_material_properties()
            materials[..., 0] = value  # static friction
            materials[..., 1] = value  # dynamic friction
            env_ids = torch.arange(self.scene.num_envs, device="cpu")
            asset.root_physx_view.set_material_properties(materials, env_ids)

        try:
            _set_friction(self._held_asset, task_cfg.held_asset_cfg.friction)
        except Exception:
            pass
        try:
            _set_friction(self._fixed_asset, task_cfg.fixed_asset_cfg.friction)
        except Exception:
            pass
        try:
            _set_friction(self._robot, task_cfg.robot_cfg.friction)
        except Exception:
            pass

    def _step_sim_no_action(self, num_steps: int = 1):
        """Step the simulation without applying new actions (used during resets).

        This mirrors the behaviour of the TacEx / IsaacLab factory environments:
        write the current scene state to PhysX, advance physics, update cached
        tensors such as fingertip pose and jacobians.
        """
        for _ in range(int(max(num_steps, 1))):
            self.scene.write_data_to_sim()
            # `render=False` is implicit for DirectRLEnv-managed sims.
            self.sim.step()
            # Use the env's physics dt for updating derived quantities.
            try:
                dt = self.physics_dt
            except AttributeError:
                dt = self.cfg.sim.dt
            # Recompute intermediate values (EE pose, jacobian, etc.).
            self._compute_intermediate_values()

    def _get_handheld_asset_relative_pose(self, env_ids: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Return pose of held asset relative to fingertip when grasped.

        Currently implemented for the peg-insertion task: the peg is aligned
        along the gripper -Z axis and positioned so that its top is roughly
        flush with the finger pads, matching TacEx's factory env.
        """
        n = env_ids.shape[0]
        device = self.device
        task = self.cfg.task

        rel_pos = torch.zeros((n, 3), device=device)
        rel_quat = self.identity_quat[env_ids].clone()

        if task.name == "peg_insert":
            # Same logic as TacEx FactoryEnv.get_handheld_asset_relative_pose for peg_insert.
            height = float(task.held_asset_cfg.height)
            finger_len = float(task.robot_cfg.franka_fingerpad_length)
            rel_pos[:, 2] = height - finger_len
        else:
            # For other tasks we default to no offset; can be extended later.
            rel_pos[:, 2] = 0.0

        return rel_pos, rel_quat

    def _init_indices_and_buffers(self):
        """Resolve body / joint indices and allocate control buffers."""
        self.identity_quat = (
            torch.tensor([1.0, 0.0, 0.0, 0.0], device=self.device)
            .unsqueeze(0)
            .repeat(self.num_envs, 1)
        )

        # Joint indexing: first 7 are the arm; remaining are gripper fingers.
        self._arm_joint_ids = list(range(7))
        self._gripper_joint_ids = list(range(7, self._robot.num_joints))

        # Fingertip / finger body indices (from TacEx factory_env).
        self.left_finger_body_idx = self._robot.body_names.index("panda_leftfinger")
        self.right_finger_body_idx = self._robot.body_names.index("panda_rightfinger")
        self.fingertip_body_idx = self._robot.body_names.index("panda_fingertip_centered")

        # Action buffers (7D actions).
        self.actions = torch.zeros((self.num_envs, 7), device=self.device)
        self.prev_actions = torch.zeros_like(self.actions)

        # Gripper target width (scalar per env).
        self._gripper_target = torch.full(
            (self.num_envs,),
            float(self.cfg.ctrl.gripper_open_pos),
            device=self.device,
        )

        # Reward buffer (always zero for IL).
        self.reward_buf = torch.zeros(self.num_envs, device=self.device)

    def _init_ik_controller(self):
        """Instantiate a DifferentialIKController for the robot arm."""
        ik_cfg = DifferentialIKControllerCfg(
            command_type="pose",
            use_relative_mode=True,
            ik_method="dls",
        )
        self._ik_controller: DifferentialIKController = DifferentialIKController(
            ik_cfg, num_envs=self.num_envs, device=self.device
        )

        # Precompute scale and clamp tensors for SE(3) deltas.
        self._pos_scale = torch.tensor(self.cfg.ctrl.pos_scale, device=self.device).view(1, 3)
        self._rot_scale = torch.tensor(self.cfg.ctrl.rot_scale, device=self.device).view(1, 3)
        self._max_pos_delta = torch.tensor(self.cfg.ctrl.max_pos_delta, device=self.device).view(1, 3)
        self._max_rot_delta = torch.tensor(self.cfg.ctrl.max_rot_delta, device=self.device).view(1, 3)

    def _compute_intermediate_values(self):
        """Update EE pose, jacobian, and joint state tensors from sim buffers."""
        # EE pose in **per-env local frame**: world pose minus env origin.
        self.fingertip_pos_w = (
            self._robot.data.body_pos_w[:, self.fingertip_body_idx] - self.scene.env_origins
        )
        self.fingertip_quat_w = self._robot.data.body_quat_w[:, self.fingertip_body_idx]

        # Jacobian for fingertip (average of left/right finger, as in TacEx).
        jacobians = self._robot.root_physx_view.get_jacobians()
        left_jac = jacobians[:, self.left_finger_body_idx - 1, 0:6, 0:7]
        right_jac = jacobians[:, self.right_finger_body_idx - 1, 0:6, 0:7]
        self.fingertip_jacobian = 0.5 * (left_jac + right_jac)

        # Joint positions / velocities (all DOFs).
        self.joint_pos = self._robot.data.joint_pos.clone()
        self.joint_vel = self._robot.data.joint_vel.clone()

    # --------------------------------------------------------------------- #
    # DirectRLEnv interface                                                 #
    # --------------------------------------------------------------------- #

    def _reset_idx(self, env_ids: Sequence[int]):
        """Reset assets and robot, with optional initialization noise."""
        super()._reset_idx(env_ids)

        env_ids_t = torch.as_tensor(env_ids, device=self.device, dtype=torch.long)
        origins = self.scene.env_origins[env_ids_t]
        num_reset = env_ids_t.shape[0]

        # ------------------------------------------------------------------ #
        # Assets: use configurable initial poses (world frame)               #
        # ------------------------------------------------------------------ #
        fixed_state = self._fixed_asset.data.default_root_state.clone()[env_ids_t]
        held_state = self._held_asset.data.default_root_state.clone()[env_ids_t]

        # Fixed asset pose
        fixed_pos_cfg = torch.tensor(self.cfg.init_assets.fixed_pos, device=self.device).view(1, 3)
        fixed_rot_cfg = torch.tensor(self.cfg.init_assets.fixed_rot, device=self.device).view(1, 4)

        # Optional world-frame position noise on the hole asset.
        fixed_noise = torch.tensor(self.cfg.fixed_init_pos_noise, device=self.device).view(1, 3)
        if torch.any(fixed_noise != 0.0):
            # Uniform per-axis noise in [-noise[i], +noise[i]].
            low = -fixed_noise
            high = fixed_noise
            delta_fixed = low + (high - low) * torch.rand(
                (num_reset, 3), device=self.device, dtype=torch.float32
            )
        else:
            delta_fixed = torch.zeros((num_reset, 3), device=self.device, dtype=torch.float32)

        fixed_state[:, 0:3] = fixed_pos_cfg.expand(num_reset, 3) + origins + delta_fixed
        fixed_state[:, 3:7] = fixed_rot_cfg.expand_as(fixed_state[:, 3:7])
        fixed_state[:, 7:] = 0.0
        self._fixed_asset.write_root_pose_to_sim(fixed_state[:, 0:7], env_ids=env_ids_t)
        self._fixed_asset.write_root_velocity_to_sim(fixed_state[:, 7:], env_ids=env_ids_t)
        self._fixed_asset.reset(env_ids=env_ids_t)

        # Held asset pose
        held_pos_cfg = torch.tensor(self.cfg.init_assets.held_pos, device=self.device).view(1, 3)
        held_rot_cfg = torch.tensor(self.cfg.init_assets.held_rot, device=self.device).view(1, 4)

        # For the non-grasped case (spawn_in_gripper=False), apply world-frame *position*
        # noise only. We intentionally do not randomize the peg's orientation here.
        held_noise_world = torch.tensor(self.cfg.held_init_pos_noise, device=self.device).view(1, 3)

        if not self.cfg.init_assets.spawn_in_gripper:
            if torch.any(held_noise_world != 0.0):
                low_h = -held_noise_world
                high_h = held_noise_world
                delta_held_w = low_h + (high_h - low_h) * torch.rand(
                    (num_reset, 3), device=self.device, dtype=torch.float32
                )
            else:
                delta_held_w = torch.zeros((num_reset, 3), device=self.device, dtype=torch.float32)
            held_quat_w = held_rot_cfg.expand(num_reset, 4)
        else:
            # When spawn_in_gripper=True, world-frame noise on the held asset is not
            # applied here; we apply local position noise only in the gripper frame.
            delta_held_w = torch.zeros((num_reset, 3), device=self.device, dtype=torch.float32)
            held_quat_w = held_rot_cfg.expand(num_reset, 4)

        held_state[:, 0:3] = held_pos_cfg.expand(num_reset, 3) + origins + delta_held_w
        held_state[:, 3:7] = held_quat_w
        held_state[:, 7:] = 0.0
        self._held_asset.write_root_pose_to_sim(held_state[:, 0:7], env_ids=env_ids_t)
        self._held_asset.write_root_velocity_to_sim(held_state[:, 7:], env_ids=env_ids_t)
        self._held_asset.reset(env_ids=env_ids_t)

        # ------------------------------------------------------------------ #
        # Robot: configurable initial joint pose (IK-rel teleop friendly)    #
        # ------------------------------------------------------------------ #
        joint_pos = self._robot.data.default_joint_pos[env_ids_t].clone()
        # Overwrite arm joints from cfg.init_robot.joint_pos
        arm_init = torch.tensor(self.cfg.init_robot.joint_pos, device=self.device).view(1, 7)
        joint_pos[:, self._arm_joint_ids] = arm_init.expand_as(joint_pos[:, self._arm_joint_ids])
        # Set fingers closed initially so the held asset is grasped.
        if self._gripper_joint_ids:
            joint_pos[:, self._gripper_joint_ids] = float(self.cfg.ctrl.gripper_close_pos)
        joint_vel = torch.zeros_like(joint_pos)
        joint_effort = torch.zeros_like(joint_pos)

        self._robot.write_joint_state_to_sim(joint_pos, joint_vel, env_ids=env_ids_t)
        self._robot.set_joint_position_target(joint_pos, env_ids=env_ids_t)
        self._robot.set_joint_effort_target(joint_effort, env_ids=env_ids_t)
        self._robot.reset(env_ids=env_ids_t)

        # Reset action-related buffers.
        self.actions[env_ids_t] = 0.0
        self.prev_actions[env_ids_t] = 0.0
        # Start with gripper closed to hold the asset.
        self._gripper_target[env_ids_t] = float(self.cfg.ctrl.gripper_close_pos)

        # Push state to sim and refresh caches.
        self.scene.write_data_to_sim()
        self.sim.forward()
        self._compute_intermediate_values()

        # ------------------------------------------------------------------ #
        # Optional EE initialization noise (world frame, via DIK).          #
        # This is applied *before* spawning the held asset in the gripper   #
        # so that once the peg is grasped there is no additional motion     #
        # until the policy / controller issues actions.                     #
        # ------------------------------------------------------------------ #
        eef_noise = torch.tensor(self.cfg.eef_init_pos_noise, device=self.device).view(1, 3)
        if torch.any(eef_noise != 0.0):
            # Refresh kinematics & jacobians after any asset/robot updates.
            self._compute_intermediate_values()

            # Build per-env delta pose: only translation, in meters.
            delta_pos = torch.zeros((self.num_envs, 3), device=self.device, dtype=torch.float32)
            low_e = -eef_noise
            high_e = eef_noise
            delta_eef = low_e + (high_e - low_e) * torch.rand(
                (num_reset, 3), device=self.device, dtype=torch.float32
            )
            # Clamp against max per-step DIK translation for safety.
            delta_eef = torch.clamp(delta_eef, -self._max_pos_delta, self._max_pos_delta)
            delta_pos[env_ids_t] = delta_eef

            delta_rot = torch.zeros_like(delta_pos)
            delta_pose_all = torch.cat([delta_pos, delta_rot], dim=-1)

            # One-shot DIK step to realize the desired EE translation.
            self._ik_controller.set_command(
                delta_pose_all,
                ee_pos=self.fingertip_pos_w,
                ee_quat=self.fingertip_quat_w,
            )

            joint_pos_arm = self.joint_pos[:, self._arm_joint_ids]
            joint_pos_des = self._ik_controller.compute(
                ee_pos=self.fingertip_pos_w,
                ee_quat=self.fingertip_quat_w,
                jacobian=self.fingertip_jacobian,
                joint_pos=joint_pos_arm,
            )

            # Apply new arm joint targets for the reset envs only.
            full_joint_pos = self.joint_pos.clone()
            full_joint_pos[:, self._arm_joint_ids] = joint_pos_des
            full_joint_vel = torch.zeros_like(full_joint_pos)
            full_joint_effort = torch.zeros_like(full_joint_pos)

            self._robot.write_joint_state_to_sim(full_joint_pos, full_joint_vel, env_ids=env_ids_t)
            self._robot.set_joint_position_target(full_joint_pos, env_ids=env_ids_t)
            self._robot.set_joint_effort_target(full_joint_effort, env_ids=env_ids_t)
            self._robot.reset(env_ids=env_ids_t)

            # Push to sim and refresh EE pose for downstream code.
            self.scene.write_data_to_sim()
            self.sim.forward()
            self._compute_intermediate_values()

        # Optionally spawn the held asset already grasped in the gripper.
        if self.cfg.init_assets.spawn_in_gripper:
            # Flip fingertip frame so gripper -Z points "down" into the asset.
            flip_z_quat = torch.tensor([0.0, 0.0, 1.0, 0.0], device=self.device).unsqueeze(0)
            flip_z_quat = flip_z_quat.repeat(self.num_envs, 1)
            zeros = torch.zeros((self.num_envs, 3), device=self.device)

            # Fingertip pose in world frame.
            fingertip_pos_world = self.fingertip_pos_w + self.scene.env_origins
            fingertip_flipped_quat, fingertip_flipped_pos = torch_utils.tf_combine(
                q1=self.fingertip_quat_w,
                t1=fingertip_pos_world,
                q2=flip_z_quat,
                t2=zeros,
            )

            # Desired pose of held asset relative to fingertip.
            rel_pos, rel_quat = self._get_handheld_asset_relative_pose(env_ids_t)

            # Optional local (gripper-frame) *position* noise on the held asset pose.
            held_noise_local = torch.tensor(
                self.cfg.held_init_pos_noise, device=self.device
            ).view(1, 3)

            if torch.any(held_noise_local != 0.0):
                low_l = -held_noise_local
                high_l = held_noise_local
                delta_local = low_l + (high_l - low_l) * torch.rand(
                    (num_reset, 3), device=self.device, dtype=torch.float32
                )
                rel_pos = rel_pos + delta_local

            asset_in_hand_quat, asset_in_hand_pos = torch_utils.tf_inverse(rel_quat, rel_pos)

            # World pose of held asset such that it is in the gripper.
            translated_quat, translated_pos = torch_utils.tf_combine(
                q1=fingertip_flipped_quat[env_ids_t],
                t1=fingertip_flipped_pos[env_ids_t],
                q2=asset_in_hand_quat,
                t2=asset_in_hand_pos,
            )

            # `translated_pos` is already in world coordinates, so we should not
            # add the per-env origin again (doing so would push the peg far away
            # for env_ids > 0). Just write the world pose directly.
            held_state = self._held_asset.data.default_root_state.clone()[env_ids_t]
            held_state[:, 0:3] = translated_pos
            held_state[:, 3:7] = translated_quat
            held_state[:, 7:] = 0.0
            self._held_asset.write_root_pose_to_sim(held_state[:, 0:7], env_ids=env_ids_t)
            self._held_asset.write_root_velocity_to_sim(held_state[:, 7:], env_ids=env_ids_t)
            self._held_asset.reset(env_ids=env_ids_t)

            # ------------------------------------------------------------------ #
            # Grasp stabilization: close gripper in place for a short duration #
            # so that the peg settles firmly between the finger pads before   #
            # the episode starts.                                              #
            # ------------------------------------------------------------------ #
            try:
                # Cache original gravity so we can restore it.
                sim_ctx = sim_utils.SimulationContext.instance()
                physics_sim_view = sim_ctx.physics_sim_view
                orig_gravity = physics_sim_view.get_gravity()

                # Temporarily disable gravity to avoid the peg sliding out while
                # the fingers settle on it.
                physics_sim_view.set_gravity(type(orig_gravity)(0.0, 0.0, 0.0))

                # Ensure gripper target is fully closed for these envs.
                close_pos = float(self.cfg.ctrl.gripper_close_pos)
                if self._gripper_joint_ids:
                    # Keep existing arm joints; only enforce finger closure.
                    joint_pos = self.joint_pos.clone()
                    joint_pos[env_ids_t.unsqueeze(-1), torch.tensor(self._gripper_joint_ids, device=self.device)] = close_pos
                    joint_vel = torch.zeros_like(joint_pos)
                    joint_effort = torch.zeros_like(joint_pos)
                    self._robot.write_joint_state_to_sim(joint_pos, joint_vel, env_ids=env_ids_t)
                    self._robot.set_joint_position_target(joint_pos, env_ids=env_ids_t)
                    self._robot.set_joint_effort_target(joint_effort, env_ids=env_ids_t)

                # Step the simulation for a short horizon (~0.25s) so the grasp stabilizes.
                grasp_time_s = 0.25
                n_steps = int(max(1, grasp_time_s / float(self.cfg.sim.dt)))
                self._step_sim_no_action(num_steps=n_steps)

                # Restore original gravity.
                physics_sim_view.set_gravity(orig_gravity)
            except Exception:
                # If anything goes wrong, fall back to a single forward() so we at
                # least have consistent cached tensors.
                self.scene.write_data_to_sim()
                self.sim.forward()
                self._compute_intermediate_values()

    def _pre_physics_step(self, actions: torch.Tensor):
        """Pre-process high-level SE(3)+gripper commands into DIK inputs."""
        # Handle resets.
        env_ids = self.reset_buf.nonzero(as_tuple=False).squeeze(-1)
        if env_ids.numel() > 0:
            self._reset_idx(env_ids.tolist())

        # Clamp to [-1, 1] for safety and store.
        actions = torch.clamp(actions, -1.0, 1.0)
        self.prev_actions = self.actions.clone()
        self.actions = actions.clone()

        # Split into SE(3) delta and gripper command.
        delta_se3 = actions[:, 0:6]
        grip_cmd = actions[:, 6]

        # Scale and clamp SE(3) deltas.
        delta_pos = delta_se3[:, 0:3] * self._pos_scale
        delta_rot = delta_se3[:, 3:6] * self._rot_scale
        delta_pos = torch.clamp(delta_pos, -self._max_pos_delta, self._max_pos_delta)
        delta_rot = torch.clamp(delta_rot, -self._max_rot_delta, self._max_rot_delta)
        delta_pose = torch.cat([delta_pos, delta_rot], dim=-1)

        # Refresh EE pose & jacobian for the current step.
        self._compute_intermediate_values()

        # Set DIK target from relative pose command.
        self._ik_controller.set_command(
            delta_pose,
            ee_pos=self.fingertip_pos_w,
            ee_quat=self.fingertip_quat_w,
        )

        # Map gripper command in [-1, 1] to [close, open] joint targets.
        alpha = 0.5 * (grip_cmd + 1.0)  # [-1, 1] -> [0, 1]
        alpha = torch.clamp(alpha, 0.0, 1.0)
        open_pos = float(self.cfg.ctrl.gripper_open_pos)
        close_pos = float(self.cfg.ctrl.gripper_close_pos)
        self._gripper_target = (1.0 - alpha) * close_pos + alpha * open_pos

    def _apply_action(self):
        """Apply DIK-computed joint targets to the PhysX articulation."""
        # Ensure caches are current at physics rate.
        self._compute_intermediate_values()

        # Current arm joint positions (7 DOFs).
        joint_pos_arm = self.joint_pos[:, self._arm_joint_ids]

        # Compute desired joint positions from DIK.
        joint_pos_des = self._ik_controller.compute(
            ee_pos=self.fingertip_pos_w,
            ee_quat=self.fingertip_quat_w,
            jacobian=self.fingertip_jacobian,
            joint_pos=joint_pos_arm,
        )

        # Build full joint target vector (arm + gripper).
        full_target = self.joint_pos.clone()
        full_target[:, self._arm_joint_ids] = joint_pos_des
        if self._gripper_joint_ids:
            full_target[:, self._gripper_joint_ids] = self._gripper_target.view(-1, 1).repeat(
                1, len(self._gripper_joint_ids)
            )

        # Send position targets to articulations (PD control handled by ImplicitActuators).
        self._robot.set_joint_position_target(full_target)

    def _get_observations(self):
        """Return proprioceptive state and EE pose in world frame.

        Obs dict keys:
        - ``policy``: (N, 22) proprio vector (joint pos/vel, EE pose, gripper width)
        - ``eef_pose_w``: (N, 9) [ee_pos(3), ee_rot_6d(6)] for downstream logging / PC projection.
        """
        self._compute_intermediate_values()

        # Joint state.
        joint_pos = self.joint_pos[:, :7]
        joint_vel = self.joint_vel[:, :7]

        # Gripper width = mean of finger joints (if present).
        if self._gripper_joint_ids:
            grip_width = self.joint_pos[:, self._gripper_joint_ids].mean(dim=1, keepdim=True)
        else:
            grip_width = torch.zeros((self.num_envs, 1), device=self.device)

        # EE position already in world frame; orientation as quaternion.
        ee_pos = self.fingertip_pos_w
        ee_quat = self.fingertip_quat_w

        # 6D rotation representation (two rotated basis vectors), as in TacEx.
        N = self.num_envs
        zeros_N3 = torch.zeros((N, 3), device=self.device)
        basis_x = zeros_N3.clone()
        basis_y = zeros_N3.clone()
        basis_x[:, 0] = 1.0
        basis_y[:, 1] = 1.0
        _, eef_x_axis_w = torch_utils.tf_combine(ee_quat, zeros_N3, self.identity_quat, basis_x)
        _, eef_y_axis_w = torch_utils.tf_combine(ee_quat, zeros_N3, self.identity_quat, basis_y)
        eef_rot_cols = torch.cat([eef_x_axis_w, eef_y_axis_w], dim=-1)  # (N, 6)

        # Proprio vector used as "policy" observation.
        proprio = torch.cat(
            [joint_pos, joint_vel, ee_pos, ee_quat, grip_width],
            dim=-1,
        )

        eef_pose_w = torch.cat([ee_pos, eef_rot_cols], dim=-1)

        return {"policy": proprio, "eef_pose_w": eef_pose_w}

    def _get_rewards(self) -> torch.Tensor:
        """No-task reward for imitation learning (always zeros)."""
        self.reward_buf[:] = 0.0
        return self.reward_buf

    def _get_dones(self) -> Tuple[torch.Tensor, torch.Tensor]:
        """Episode termination on time-out only."""
        time_out = self.episode_length_buf >= self.max_episode_length - 1
        terminated = torch.zeros_like(time_out)
        return terminated, time_out

    def _set_debug_vis_impl(self, debug_vis: bool):
        """No-op debug visualization hook (required by DirectRLEnv)."""
        return


__all__ = ["FactoryILEnv"]