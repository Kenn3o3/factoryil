from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch

from .factory_agent import FactoryAgent


def _ensure_len(history: List[Any], target_len: int) -> List[Any]:
    """Left-pad history by repeating the first element until `target_len`."""
    if target_len <= 0:
        return []
    if len(history) >= target_len:
        return history[-target_len:]
    if len(history) == 0:
        raise ValueError("Cannot pad an empty history.")
    first = history[0]
    return [first for _ in range(target_len - len(history))] + history


def _chw01_to_hwc_u8(chw01: torch.Tensor) -> np.ndarray:
    """CHW float tensor in [0,1] -> HWC uint8 numpy."""
    t = torch.clamp(chw01, 0.0, 1.0)
    return (t.permute(1, 2, 0) * 255.0).round().to(torch.uint8).cpu().numpy()


def _resolve_latest_ckpt(path: str) -> str:
    """If `path` is a directory, resolve to the latest ckpt_best*.pth inside it."""
    p = Path(path)
    if not p.exists():
        return path
    if p.is_file():
        return str(p)
    # directory
    candidates = list(p.rglob("ckpt_best*.pth"))
    if not candidates:
        # fall back to any .pth
        candidates = list(p.rglob("*.pth"))
    if not candidates:
        raise FileNotFoundError(f"No checkpoint found under directory: {path}")
    latest = max(candidates, key=lambda x: x.stat().st_mtime)
    return str(latest)


@dataclass
class _PerEnvILState:
    state_hist: List[np.ndarray]
    pc_hist: List[np.ndarray]
    rgb_hist: Dict[str, List[np.ndarray]]
    pred_buf: Optional[np.ndarray]
    pred_idx: int
    steps_left: int


class ILPolicyAgent(FactoryAgent):
    """Imitation-learning policy agent (Diffusion Policy / EquiBot).

    This is a thin wrapper around the vendored code under:
      `src/third_party/imitation_learning/policies`.

    Notes:
    - We assume the policy was trained on env-frame actions (the same 6D delta
      action used by FactoryILEnv), and we keep the gripper closed during rollouts.
    """

    def __init__(self, il_cfg: str, il_checkpoint: str, device: str, args: Any) -> None:
        super().__init__(device=device, obs_horizon=0, action_horizon=0)
        self.args = args

        self.cfg_name = str(il_cfg)
        self.ckpt_path = _resolve_latest_ckpt(str(il_checkpoint))

        # Lazily imported optional deps.
        try:
            from omegaconf import OmegaConf
        except Exception as e:  # pragma: no cover
            raise ImportError(
                "ILPolicyAgent requires OmegaConf (omegaconf). Install it (e.g. `pip install -e .[il]`) "
                "or run with --agent expert/replay."
            ) from e

        # Locate configs relative to the vendored policy package.
        try:
            import imitation_learning.policies as pol_pkg
        except Exception as e:  # pragma: no cover
            raise ImportError(
                "Could not import `imitation_learning.policies`. "
                "Make sure `src/third_party` is on the python path (see pyproject.toml)."
            ) from e

        pkg_dir = Path(getattr(pol_pkg, "__file__", "")).resolve().parent
        config_dir = pkg_dir / "configs"

        cfg_path = Path(self.cfg_name)
        if cfg_path.suffix == ".yaml" and cfg_path.exists():
            cfg_file = cfg_path
        else:
            cfg_file = config_dir / f"{self.cfg_name}.yaml"
        if not cfg_file.exists():
            raise FileNotFoundError(f"IL config not found: {cfg_file}")

        # NOTE: the policy configs use Hydra-style defaults (e.g. `defaults: - base`).
        # For inference inside FactoryIL we do a minimal "compose" by merging
        # `base.yaml` + the selected config.
        base_file = config_dir / "base.yaml"
        if not base_file.exists():
            raise FileNotFoundError(f"Missing base policy config: {base_file}")
        cfg_base = OmegaConf.load(str(base_file))
        cfg_spec = OmegaConf.load(str(cfg_file))
        cfg = OmegaConf.merge(cfg_base, cfg_spec)
        # Best-effort overrides for evaluation/inference.
        try:
            cfg.mode = "eval"
        except Exception:
            pass
        try:
            cfg.device = str(device)
        except Exception:
            pass
        try:
            cfg.use_wandb = False
        except Exception:
            pass

        # Instantiate the underlying IL agent.
        try:
            from imitation_learning.policies.utils.misc import get_agent
        except Exception as e:  # pragma: no cover
            raise ImportError("Failed importing IL policy utilities from vendored code.") from e

        AgentCls = get_agent(cfg.agent.agent_name)
        self._agent = AgentCls(cfg)
        self._agent.load_snapshot(self.ckpt_path)
        self._agent.train(False)

        # Resolve observation spec from agent.
        self.obs_mode: str = str(getattr(self._agent, "obs_mode", "pc"))
        self.obs_horizon = int(getattr(self._agent, "obs_horizon", 2))
        self.pred_horizon = int(getattr(self._agent, "pred_horizon", 8))
        self.ac_horizon = int(getattr(self._agent, "ac_horizon", 1))
        self.num_eef = int(getattr(self._agent, "num_eef", 1))
        self.dof = int(getattr(self._agent, "dof", 7))

        # RGB view keys for rgb-mode agents.
        self.rgb_keys: List[str] = list(getattr(self._agent, "rgb_keys", []))

        # Per-env state is allocated in reset().
        self._env_state: List[_PerEnvILState] = []

    # ------------------------------------------------------------------ #
    # FactoryAgent hooks
    # ------------------------------------------------------------------ #

    def _reset_internal_state(self) -> None:
        self._env_state = []
        for _ in range(int(self.num_envs)):
            self._env_state.append(
                _PerEnvILState(
                    state_hist=[],
                    pc_hist=[],
                    rgb_hist={k: [] for k in self.rgb_keys},
                    pred_buf=None,
                    pred_idx=0,
                    steps_left=0,
                )
            )

    def _reset_episode_internal(self, env_idx: int) -> None:
        if env_idx < 0 or env_idx >= len(self._env_state):
            return
        st = self._env_state[env_idx]
        st.state_hist.clear()
        st.pc_hist.clear()
        for k in st.rgb_hist:
            st.rgb_hist[k].clear()
        st.pred_buf = None
        st.pred_idx = 0
        st.steps_left = 0

    def _alloc_action_batch(self, env) -> torch.Tensor:
        action_dim = int(env.unwrapped.cfg.action_space)
        return torch.zeros((int(self.num_envs), action_dim), device=env.device, dtype=torch.float32)

    def _zero_action_for_env(self, env, env_idx: int) -> torch.Tensor:  # noqa: ARG002
        action_dim = int(env.unwrapped.cfg.action_space)
        a = torch.zeros((action_dim,), device=self.device, dtype=torch.float32)
        if action_dim > 6:
            a[6] = -1.0
        return a

    def _compute_action_for_env(self, env_idx: int, env, t_step: int) -> torch.Tensor:  # noqa: ARG002
        # Unused because we override `act` vectorized over envs.
        return self._zero_action_for_env(env, env_idx)

    # ------------------------------------------------------------------ #
    # Main policy inference entrypoint
    # ------------------------------------------------------------------ #

    @torch.no_grad()
    def act(self, obs_batch, done_mask, env, t_step: int):  # noqa: ARG002
        n = int(self.num_envs or len(obs_batch))
        if self.num_envs != n:
            self.reset(n)

        done = np.asarray(done_mask, dtype=bool) if done_mask is not None else np.zeros((n,), dtype=bool)

        action_dim_env = int(env.unwrapped.cfg.action_space)
        out = torch.zeros((n, action_dim_env), device=env.device, dtype=torch.float32)

        for i in range(n):
            if done[i]:
                out[i] = self._zero_action_for_env(env, i)
                continue

            obs_i = obs_batch[i] or {}
            st = self._env_state[i]

            # ------------------------------------------------------------------
            # 1) Update per-env observation histories (pre-step obs_t).
            # ------------------------------------------------------------------
            state_t = obs_i.get("state", None)
            if state_t is None:
                raise KeyError("ILPolicyAgent expected obs_i['state'] (EEF pose) to be present.")

            if torch.is_tensor(state_t):
                state_np = state_t.detach().to("cpu").numpy().astype(np.float32).reshape(-1)
            else:
                state_np = np.asarray(state_t, dtype=np.float32).reshape(-1)
            # Convert 9D -> 10D by appending a constant 0.0 (gripper).
            if state_np.size == 9:
                state_np = np.concatenate([state_np, np.zeros((1,), dtype=np.float32)], axis=0)
            if state_np.size < 10:
                pad = np.zeros((10 - state_np.size,), dtype=np.float32)
                state_np = np.concatenate([state_np, pad], axis=0)
            state_np = state_np[:10].astype(np.float32, copy=False).reshape(self.num_eef, 10)
            st.state_hist.append(state_np)

            if self.obs_mode.startswith("pc"):
                pc_t = obs_i.get("pc", None)
                if pc_t is not None:
                    if torch.is_tensor(pc_t):
                        pc_np = pc_t.detach().to("cpu").numpy().astype(np.float32)
                    else:
                        pc_np = np.asarray(pc_t, dtype=np.float32)
                    if pc_np.ndim == 2 and pc_np.shape[1] >= 3:
                        pc_np = pc_np[:, :3]
                    st.pc_hist.append(pc_np)

            if self.obs_mode == "rgb":
                rgb_views = obs_i.get("rgb", {}) or {}
                if not self.rgb_keys:
                    # First call: infer view keys from provided observation.
                    self.rgb_keys = list(rgb_views.keys())
                    st.rgb_hist = {k: [] for k in self.rgb_keys}
                for k in self.rgb_keys:
                    v = rgb_views.get(k, None)
                    if v is None:
                        continue
                    if torch.is_tensor(v):
                        st.rgb_hist[k].append(_chw01_to_hwc_u8(v))
                    else:
                        st.rgb_hist[k].append(np.asarray(v))

            # ------------------------------------------------------------------
            # 2) Run inference when the current predicted sequence is exhausted.
            # ------------------------------------------------------------------
            need_new = (
                st.pred_buf is None
                or st.steps_left <= 0
                or st.pred_idx >= int(self.pred_horizon)
            )
            if need_new:
                state_seq = _ensure_len(st.state_hist, int(self.obs_horizon))
                agent_obs: Dict[str, Any] = {"state": np.stack(state_seq, axis=0)}
                if self.obs_mode.startswith("pc"):
                    if len(st.pc_hist) == 0:
                        raise RuntimeError(
                            "ILPolicyAgent is in pc mode but did not receive any 'pc' observations yet. "
                            "Did you enable --save_pc and set up segmentation?"
                        )
                    pc_seq = _ensure_len(st.pc_hist, int(self.obs_horizon))
                    agent_obs["pc"] = pc_seq  # list of arrays
                else:
                    rgb_dict: Dict[str, np.ndarray] = {}
                    for k in self.rgb_keys:
                        if len(st.rgb_hist.get(k, [])) == 0:
                            continue
                        seq = _ensure_len(st.rgb_hist[k], int(self.obs_horizon))
                        rgb_dict[k] = np.stack(seq, axis=0)
                    agent_obs["rgb"] = rgb_dict

                pred = self._agent.act(agent_obs, return_dict=False, debug=False)
                st.pred_buf = np.asarray(pred, dtype=np.float32)
                st.pred_idx = 0
                st.steps_left = min(int(self.ac_horizon), int(st.pred_buf.shape[0]))

            # ------------------------------------------------------------------
            # 3) Execute one step from the predicted sequence.
            # ------------------------------------------------------------------
            assert st.pred_buf is not None
            if st.pred_idx >= st.pred_buf.shape[0]:
                exec_one = st.pred_buf[-1]
            else:
                exec_one = st.pred_buf[st.pred_idx]

            st.pred_idx += 1
            st.steps_left -= 1

            exec_one = np.asarray(exec_one, dtype=np.float32).reshape(-1)
            # Predicted vector is [num_eef*dof]; take the first EEF and first 6 DOFs.
            if exec_one.size >= self.dof:
                exec_eef = exec_one[: self.dof]
            else:
                pad = np.zeros((self.dof - exec_one.size,), dtype=np.float32)
                exec_eef = np.concatenate([exec_one, pad], axis=0)

            a = np.zeros((action_dim_env,), dtype=np.float32)
            a[:6] = exec_eef[:6]
            if action_dim_env > 6:
                a[6] = -1.0  # keep gripper closed during IL rollouts
            a = np.clip(a, -1.0, 1.0)
            out[i] = torch.as_tensor(a, device=env.device, dtype=torch.float32)

        return out


# Backward-compatible alias.
ILAgent = ILPolicyAgent


__all__ = ["ILPolicyAgent", "ILAgent"]


