from __future__ import annotations

from typing import TYPE_CHECKING
import torch

from .factory_agent import FactoryAgent

if TYPE_CHECKING:
    from factoryil.env.factory_env import FactoryILEnv


# --------------------------------------------------------------------------- #
# Homework                                                                    #
# --------------------------------------------------------------------------- #
#
# This file contains a simple analytic expert for debugging/plumbing:
# - Translation is driven by a vectorized pure-pursuit controller over a short
#   waypoint polyline.
# - Rotation is intentionally disabled in this homework variant because we
#   assume the peg is always vertical and aligned with the hole.
#
# Fake physics note:
# - If the hole axis is perfectly vertical and the "tip" of the hole is at z=0
#   in the env frame, a *fake* contact height might be:
#       z_touch_fake = 0.012  # meters
#   This is NOT a calibrated value; it is just a placeholder number for testing.

Z_TOUCH_FAKE_M: float = 0.012


def _clip_norm(x: torch.Tensor, max_norm: torch.Tensor | float, eps: float = 1e-9) -> torch.Tensor:
    """Scale vectors down to have norm <= max_norm (supports broadcasting)."""
    if not torch.is_tensor(max_norm):
        max_norm_t = torch.tensor(float(max_norm), device=x.device, dtype=x.dtype)
    else:
        max_norm_t = max_norm.to(device=x.device, dtype=x.dtype)
    n = torch.linalg.vector_norm(x, dim=-1, keepdim=True)
    scale = torch.clamp(max_norm_t / (n + eps), max=1.0)
    return x * scale


def _pure_pursuit_lookahead(
    p: torch.Tensor,
    waypoints: torch.Tensor,
    lookahead_m: float,
    eps: float = 1e-9,
) -> torch.Tensor:
    """
    Vectorized closest-point + lookahead on a per-env polyline.

    Args:
      p: (N,3) current position.
      waypoints: (N,M,3) polyline waypoints.
      lookahead_m: scalar lookahead distance along arclength.
    Returns:
      p_L: (N,3) lookahead point.
    """
    N, M, _ = waypoints.shape
    S = M - 1
    if S <= 0:
        return waypoints[:, -1, :]

    seg_a = waypoints[:, :-1, :]  # (N,S,3)
    seg_b = waypoints[:, 1:, :]   # (N,S,3)
    v = seg_b - seg_a             # (N,S,3)
    v_norm2 = torch.sum(v * v, dim=-1)  # (N,S)
    v_len = torch.sqrt(v_norm2 + eps)   # (N,S)

    # Closest point on each segment.
    w = p[:, None, :] - seg_a  # (N,S,3)
    t = torch.sum(w * v, dim=-1) / (v_norm2 + eps)  # (N,S)
    t = torch.clamp(t, 0.0, 1.0)
    proj = seg_a + t[..., None] * v  # (N,S,3)
    d2 = torch.sum((p[:, None, :] - proj) ** 2, dim=-1)  # (N,S)

    # Select closest segment.
    seg_idx = torch.argmin(d2, dim=1)  # (N,)
    idx_expand = seg_idx.view(N, 1)

    # Prefix arclengths.
    prefix = torch.zeros((N, S + 1), device=p.device, dtype=p.dtype)
    prefix[:, 1:] = torch.cumsum(v_len, dim=1)
    total_len = prefix[:, -1]  # (N,)

    # s_star = prefix[idx] + t_star * len[idx]
    t_star = torch.gather(t, 1, idx_expand).squeeze(1)           # (N,)
    len_star = torch.gather(v_len, 1, idx_expand).squeeze(1)     # (N,)
    pref_star = torch.gather(prefix[:, :-1], 1, idx_expand).squeeze(1)  # (N,)
    s_star = pref_star + t_star * len_star

    # Lookahead arclength.
    s_L = torch.clamp(s_star + float(lookahead_m), min=0.0)
    s_L = torch.minimum(s_L, total_len)

    # Find segment containing s_L.
    # j = number of prefix segment ends <= s_L, clamped to [0, S-1]
    ends = prefix[:, 1:]  # (N,S)
    j = torch.sum((s_L[:, None] >= ends).to(torch.long), dim=1)  # (N,)
    j = torch.clamp(j, 0, S - 1)
    j_expand = j.view(N, 1)

    s0 = torch.gather(prefix[:, :-1], 1, j_expand).squeeze(1)   # (N,)
    len_j = torch.gather(v_len, 1, j_expand).squeeze(1)         # (N,)
    # Param along segment j.
    u = (s_L - s0) / (len_j + eps)
    u = torch.clamp(u, 0.0, 1.0)

    a_j = torch.gather(seg_a, 1, j_expand[:, :, None].expand(N, 1, 3)).squeeze(1)  # (N,3)
    v_j = torch.gather(v, 1, j_expand[:, :, None].expand(N, 1, 3)).squeeze(1)      # (N,3)
    p_L = a_j + u[:, None] * v_j
    return p_L

class ExpertAgent(FactoryAgent):
    """
    Expert agent.

    This class is a scaffold
    with detailed comments about the data flow and data formats so you can
    implement your own expert directly in this file.

    Current behavior:
    - Returns a simple analytic expert action (translation-only pure pursuit).

    Why keep it this way:
    - It lets you validate the runner/env → agent → env action plumbing without
      mixing in control logic.
    """

    def __init__(self, device: str, expert_cfg) -> None:
        super().__init__(device=device, obs_horizon=0, action_horizon=0)
        self.expert_cfg = expert_cfg
        self._scratch: dict[str, torch.Tensor] | None = None
        
    def _reset_internal_state(self) -> None:
        self._scratch = None

    def _ensure_state(self, env, dtype: torch.dtype) -> None:
        n = int(env.num_envs)
        device = env.device
        if self._scratch is None:
            self._scratch = {}
        # Per-batch cached start / goal waypoints for pure pursuit.
        # NOTE: We intentionally cache only *episode-invariant* quantities here
        # (start peg pose + a conservative safe approach height). The hole can
        # physically move during an episode, so we must NOT cache its pose.
        if "start_peg_pos" not in self._scratch or self._scratch["start_peg_pos"].shape[0] != n:
            self._scratch["start_peg_pos"] = torch.zeros((n, 3), device=device, dtype=dtype)
            self._scratch["safe_z"] = torch.zeros((n,), device=device, dtype=dtype)

    def act(self, obs_batch, done_mask, env, t_step: int):
        del obs_batch
        done_t = torch.as_tensor(done_mask, dtype=torch.bool, device=env.device)
        return self._compute_expert_actions(env=env, done_mask=done_t, t_step=int(t_step))

    def _alloc_action_batch(self, env):
        action_dim = int(env.unwrapped.cfg.action_space)
        return torch.zeros((self.num_envs, action_dim), device=self.device)

    def _zero_action_for_env(self, env, env_idx: int):
        # Zero end-effector deltas, keep gripper closed if present.
        action_dim = int(env.unwrapped.cfg.action_space)
        a = torch.zeros((action_dim,), device=self.device)
        if action_dim > 6:
            # a[0:3]: Cartesian position deltas
            # a[3:6]: orientation deltas (unused by the analytic expert)
            # a[6]:   gripper command; negative keeps it closed to hold the peg.
            a[6] = -1.0
        return a

    # ------------------------------------------------------------------ #
    # Core expert control                                                #
    # ------------------------------------------------------------------ #

    def _compute_expert_actions(
        self,
        env: FactoryILEnv,
        done_mask: torch.Tensor,
        t_step: int = 0,
    ) -> torch.Tensor:
        """Compute expert actions (analytic expert using polyline pure-pursuit).

        ## Inputs (what you can read)
        - `env`: The vectorized FactoryIL env (Isaac Lab).
          You can read privileged state from internal buffers. Typical tensors:
          - `env.num_envs`: number of parallel envs, N (int)
          - `env.device`: torch device for all tensors (e.g. "cuda:0")
          - `env.cfg.action_space`: action dimension, A (int)
          - `env.scene.env_origins`: (N, 3) env-origin translations in world
          - `env._fixed_asset.data.root_pos_w`: (N, 3) hole/root world positions
          - `env._held_asset.data.root_pos_w`: (N, 3) peg/root world positions
          These names are task-specific but are used by the current FactoryIL tasks.

        - `done_mask`: boolean tensor of shape (N,), True where an env is done.
        - `t_step`: int step index within the rollout (0-based).

        ## Output (what you must return)
        - `actions`: torch tensor of shape (N, A), dtype float, on `env.device`.

        ## Action format (important)
        FactoryIL uses a normalized delta-action convention (clipped to [-1, 1]):
        - `actions[:, 0:3]`: normalized Cartesian delta position (dx, dy, dz)
        - `actions[:, 3:6]`: normalized rotation delta (rx, ry, rz)
        - `actions[:, 6]` (if present): gripper command (task-dependent)

        The env/controller scales those values internally using config scalars
        (e.g. `env.cfg.ctrl.pos_scale`, `env.cfg.ctrl.rot_scale`). In other words:
        you output unitless normalized commands; the controller converts them.

        ## Objective
        Replace the placeholder action below with a real expert.
        Keep it fully vectorized over envs (avoid Python loops).

        ## Assumption for this homework variant
        We assume the peg is always **perfectly vertical and aligned** with the hole,
        so this expert outputs **no rotation** (`actions[:, 3:6] = 0`).
        """
        device = env.device
        num_envs = int(env.num_envs)
        action_dim = int(env.cfg.action_space)

        # You can call into env internals to refresh cached tensors, if needed.
        # Keep this try/except in case a task/env doesn't implement the method.
        try:
            env._compute_intermediate_values()
        except Exception:
            pass

        # Allocate optional scratch space (only needed once you implement logic).
        # Here we still call it so you have a clear place to add state.
        dtype = torch.float32
        try:
            # Prefer using the env's internal tensor dtype if available.
            dtype = env._fixed_asset.data.root_pos_w.dtype
        except Exception:
            pass
        self._ensure_state(env, dtype=dtype)

        # ------------------------------------------------------------------ #
        # Read state in the env/world frame used by the controller.          #
        # Positions are in the per-env translated frame (world - env_origin).#
        # Quaternions are in world orientation (translation-only origin shift).#
        # ------------------------------------------------------------------ #
        env_origins = env.scene.env_origins.to(device=device, dtype=dtype)  # (N,3)

        # Peg/hole root poses.
        fixed_pos = env._fixed_asset.data.root_pos_w.to(device=device, dtype=dtype) - env_origins  # (N,3)
        held_pos = env._held_asset.data.root_pos_w.to(device=device, dtype=dtype) - env_origins    # (N,3)

        # ------------------------------------------------------------------ #
        # Cache per-batch *episode-invariant* quantities at t_step==0.         #
        # IMPORTANT: do NOT cache the hole pose; it may move during the episode.#
        # ------------------------------------------------------------------ #
        # Task geometry scalars.
        try:
            height = float(getattr(env.cfg.task.fixed_asset_cfg, "height", 0.05))
        except Exception:
            height = 0.05

        if t_step == 0:
            self._scratch["start_peg_pos"].copy_(held_pos)

            # Compute a conservative approach height above the hole, but never below start z.
            clearance = max(0.02, 0.5 * float(height))
            safe_z = torch.maximum(held_pos[:, 2], fixed_pos[:, 2] + float(height) + clearance)
            self._scratch["safe_z"].copy_(safe_z)

        start_peg = self._scratch["start_peg_pos"]
        safe_z = self._scratch["safe_z"]

        # Live hole pose: do NOT cache (the fixed asset can move under contact).
        hole_pos = fixed_pos

        # Live insertion target depth from task success threshold.
        try:
            success_frac = float(getattr(env.cfg.task, "success_threshold", -0.8))
        except Exception:
            success_frac = -0.8
        # In our convention, negative means "below the hole base".
        if success_frac > 0.0:
            success_frac = -abs(success_frac)
        target_z_nom = fixed_pos[:, 2] + float(height) * float(success_frac) - 0.005

        # ------------------------------------------------------------------ #
        # Descent gating: don't start descending until XY is centered.
        # Since we assume perfect vertical alignment, we don't gate on orientation.
        # ------------------------------------------------------------------ #
        xy_err = held_pos[:, 0:2] - fixed_pos[:, 0:2]
        xy_dist = torch.linalg.vector_norm(xy_err, dim=-1)  # (N,)
        try:
            xy_tol = float(getattr(env.cfg.task, "xy_success_tol_m", 0.003))
        except Exception:
            xy_tol = 0.003
        xy_gate = max(2.0 * xy_tol, 0.008)  # meters
        allow_descent = xy_dist <= xy_gate

        target_z = torch.where(allow_descent, target_z_nom, safe_z)

        # ------------------------------------------------------------------ #
        # Polyline waypoints for pure-pursuit in 3D:                          #
        #   W0 = start peg position                                           #
        #   W1 = raise/lower at start XY to safe_z                            #
        #   W2 = move in XY at safe_z to above the hole                       #
        #   W3 = descend vertically into the hole (or hold at safe_z if gated)#
        # ------------------------------------------------------------------ #
        w0 = start_peg
        w1 = torch.stack([start_peg[:, 0], start_peg[:, 1], safe_z], dim=-1)
        w2 = torch.stack([hole_pos[:, 0], hole_pos[:, 1], safe_z], dim=-1)
        w3 = torch.stack([hole_pos[:, 0], hole_pos[:, 1], target_z], dim=-1)
        waypoints = torch.stack([w0, w1, w2, w3], dim=1)  # (N,4,3)

        # Lookahead along the polyline (carrot point).
        # Larger lookahead -> faster/straighter motion (cuts corners more).
        lookahead_m = 0.1
        p_L = _pure_pursuit_lookahead(held_pos, waypoints, lookahead_m=lookahead_m)

        # ------------------------------------------------------------------ #
        # Convert desired motion into env action-space (normalized deltas).  #
        # The env scales by cfg.ctrl.pos_scale/rot_scale and clamps.         #
        # ------------------------------------------------------------------ #
        # Controller period in seconds (physics dt * decimation).
        try:
            dt = float(env.cfg.sim.dt) * float(getattr(env.cfg, "decimation", 1))
        except Exception:
            dt = 0.02

        # Translation: P controller in task space + speed clamp.
        k_pos_s = 96.0  # [1/s]
        v_max = 5.20    # [m/s]
        v_des = k_pos_s * (p_L - held_pos)  # (N,3) m/s
        v_cmd = _clip_norm(v_des, v_max)
        delta_pos_m = v_cmd * dt  # (N,3) meters
        # During descent (i.e., after XY is centered), slow down to reduce rim hits / oscillations.
        delta_pos_m = delta_pos_m * torch.where(
            allow_descent.unsqueeze(-1),
            torch.tensor(0.45, device=device, dtype=dtype),
            torch.tensor(1.0, device=device, dtype=dtype),
        )


        # Map physical deltas -> normalized action deltas.
        pos_scale = torch.tensor(getattr(env.cfg.ctrl, "pos_scale", [0.75, 0.75, 0.75]), device=device, dtype=dtype).view(1, 3)

        a_pos = delta_pos_m / (pos_scale + 1e-9)

        actions = torch.zeros((num_envs, action_dim), device=device, dtype=dtype)
        actions[:, 0:3] = a_pos
        # Rotation is intentionally disabled for this variant (assumed always aligned).
        if action_dim >= 6:
            actions[:, 3:6] = 0.0
        if action_dim > 6:
            actions[:, 6] = -1.0  # keep gripper closed to hold the peg

        # Done envs: no motion (keep gripper closed).
        if done_mask is not None and done_mask.numel() == num_envs:
            if bool(done_mask.any().item()):
                actions[done_mask, 0:6] = 0.0
                if action_dim > 6:
                    actions[done_mask, 6] = -1.0

        # Final safety clamp (env also clamps).
        actions = torch.clamp(actions, -1.0, 1.0)
        # print("actions: ", actions)
        return actions

    def _compute_action_for_env(self, env_idx: int, env, t_step: int):
        """Fallback to satisfy FactoryAgent's abstract interface (unused)."""
        done = torch.zeros((int(env.unwrapped.num_envs),), device=env.device, dtype=torch.bool)
        return self._compute_expert_actions(env=env, done_mask=done, t_step=int(t_step))[env_idx]


__all__ = ["ExpertAgent"]

# example output:

# python -m factoryil.runner \
#   --agent expert \
#   --task peg_insert \
#   --episodes 1 \
#   --num_envs 1 \
#   --data_dir ./data/debug_expert \
#   --device cuda:0 --enable_cameras --headless

