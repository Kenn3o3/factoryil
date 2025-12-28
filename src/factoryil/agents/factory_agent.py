from __future__ import annotations

import abc
from typing import Any, Optional, Sequence

import numpy as np
import torch


class FactoryAgent(abc.ABC):
    """Base interface for FactoryIL agents.

    Agents are called from the unified runner with:
      `actions = agent.act(obs_batch, done_mask_np, env, t_step=step_idx)`

    where:
      - obs_batch: list[dict] length N (num_envs)
      - done_mask_np: numpy bool array length N
      - env: the vectorized FactoryILEnv
      - actions: torch tensor (N, action_dim) on env.device
    """

    def __init__(self, device: str, obs_horizon: int, action_horizon: int) -> None:
        self.device = str(device)
        self.obs_horizon = int(obs_horizon)
        self.action_horizon = int(action_horizon)
        self.num_envs: int = 0

    def reset(self, num_envs: int) -> None:
        self.num_envs = int(num_envs)
        self._reset_internal_state()

    @abc.abstractmethod
    def _reset_internal_state(self) -> None:
        """Reset all agent state (called at env.reset())"""

    def _reset_episode_internal(self, env_idx: int) -> None:  # noqa: ARG002
        """Reset per-env episode state (optional)."""
        return

    @abc.abstractmethod
    def _alloc_action_batch(self, env) -> torch.Tensor:
        """Allocate a (N, action_dim) tensor for actions."""

    @abc.abstractmethod
    def _zero_action_for_env(self, env, env_idx: int) -> torch.Tensor:
        """Return a neutral action for one env."""

    @abc.abstractmethod
    def _compute_action_for_env(self, env_idx: int, env, t_step: int) -> torch.Tensor:
        """Compute an action for one env index."""

    def act(self, obs_batch, done_mask, env, t_step: int):  # noqa: ARG002
        if self.num_envs <= 0:
            # Best-effort initialization when called without reset().
            try:
                self.reset(len(obs_batch))
            except Exception:
                pass

        N = int(self.num_envs or len(obs_batch))
        done_t: Optional[torch.Tensor] = None
        if done_mask is not None:
            if isinstance(done_mask, np.ndarray):
                done_t = torch.as_tensor(done_mask, dtype=torch.bool, device=self.device)
            else:
                done_t = torch.as_tensor(done_mask, dtype=torch.bool, device=self.device)

        actions = self._alloc_action_batch(env)
        for i in range(N):
            if done_t is not None and bool(done_t[i].item()):
                # Episode ended: output neutral action and reset per-episode state.
                try:
                    self._reset_episode_internal(i)
                except Exception:
                    pass
                actions[i] = self._zero_action_for_env(env, i)
                continue
            actions[i] = self._compute_action_for_env(i, env, int(t_step))

        return actions


__all__ = ["FactoryAgent"]


