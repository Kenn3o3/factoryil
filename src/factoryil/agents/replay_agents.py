from __future__ import annotations

import os
from typing import List, Optional

import torch

from .factory_agent import FactoryAgent

from factoryil.replay_actions import _load_episode_csv as _load_episode_csv_helper

class ReplayAgent(FactoryAgent):
    """
    Replays pre-recorded actions from an episode directory (``timestamps_robot.csv``).

    - Does NOT use online history to plan, so:
        ``obs_horizon = 0``, ``action_horizon = 0`` (buffers stay empty).
    - Internally maintains:
        - ``world_actions[idx]``: full offline sequence per frame.
        - ``is_last_flags[idx]``: whether this CSV row is the terminal frame.
        - ``current_index``: which frame to apply next.
    """

    def __init__(self, device: str, episode_dir: str) -> None:
        super().__init__(device=device, obs_horizon=0, action_horizon=0)
        self.episode_dir = os.path.abspath(episode_dir)

        self.frames: List[int] = []
        self.world_actions: List[torch.Tensor] = []
        self.is_last_flags: List[bool] = []
        self.current_index: int = 0
        self.action_dim: Optional[int] = None

    # ------------------------------------------------------------------ #
    # FactoryAgent hooks                                                 #
    # ------------------------------------------------------------------ #

    def _reset_internal_state(self) -> None:
        # Load CSV only once per run (could also be per-episode).
        # Actual loading is deferred until we see an env (in _maybe_load_csv).
        self.current_index = 0

    def _reset_episode_internal(self, env_idx: int) -> None:  # noqa: ARG002
        # For replay we typically run single-env; but if multi-env is used,
        # we simply loop back to the start of the same episode.
        self.current_index = 0

    def _maybe_load_csv(self, env) -> None:
        if self.world_actions:
            return
        # Determine action_dim from env to validate CSV contents.
        self.action_dim = int(env.unwrapped.cfg.action_space)
        csv_path = os.path.join(self.episode_dir, "timestamps_robot.csv")
        # _load_episode_csv_helper returns (frames, is_last_flags, world_actions_np)
        ret = _load_episode_csv_helper(csv_path, self.action_dim)
        
        frames = ret[0]
        is_last_flags = ret[1]
        world_actions_np = ret[2]

        device = self.device
        self.frames = list(frames)
        self.is_last_flags = list(is_last_flags)
        # Convert numpy arrays to torch tensors on the agent device.
        self.world_actions = [
            torch.as_tensor(a, dtype=torch.float32, device=device) for a in world_actions_np
        ]

    def _alloc_action_batch(self, env):
        if self.action_dim is None:
            self.action_dim = int(env.unwrapped.cfg.action_space)
        return torch.zeros((self.num_envs, self.action_dim), device=self.device)

    def _zero_action_for_env(self, env, env_idx: int):  # noqa: ARG002
        if self.action_dim is None:
            raise RuntimeError("ReplayAgent._zero_action_for_env called before action_dim set.")
        a = torch.zeros((self.action_dim,), device=self.device)
        if self.action_dim > 6:
            a[6] = -1.0
        return a

    # ------------------------------------------------------------------ #
    # Core replay logic                                                  #
    # ------------------------------------------------------------------ #

    def _compute_action_for_env(self, env_idx: int, env, t_step: int):  # noqa: ARG002
        """
        Return the next action from CSV sequence, or zero if we've reached the
        terminal row (``is_last == True``).
        """
        self._maybe_load_csv(env)

        if self.current_index >= len(self.world_actions):
            # No more replay frames -> neutral action.
            return self._zero_action_for_env(env, env_idx)

        # Stop before terminal zero-action frame.
        if self.is_last_flags[self.current_index]:
            return self._zero_action_for_env(env, env_idx)

        world_action = self.world_actions[self.current_index]

        self.current_index += 1
        return world_action

__all__ = ["ReplayAgent"]


