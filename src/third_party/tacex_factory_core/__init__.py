"""Vendored TacEx factory components used by FactoryIL.

This package is a small, self-contained subset of the TacEx/IsaacLab *factory*
task stack. It includes:

- Task/asset configuration objects (peg/hole/gears/nut).
- (Optional) the TacEx RL-style factory `DirectRLEnv` + gym registrations.

Gym registrations are performed **best-effort**: if IsaacLab/TacEx dependencies
are not available in the current environment, import will still succeed (only
the lightweight config objects will be available).
"""

from __future__ import annotations

from .factory_tasks_cfg import (  # noqa: F401
    FactoryTask,
    FixedAssetCfg,
    GearMesh,
    HeldAssetCfg,
    NutThread,
    PegInsert,
    RobotCfg,
)


def register_gym_envs() -> None:
    """Register TacEx factory environments with Gymnasium (best-effort).

    IDs:
      - TacEx-Factory-PegInsert-Direct-v0
      - TacEx-Factory-GearMesh-Direct-v0
      - TacEx-Factory-NutThread-Direct-v0
    """
    try:
        import gymnasium as gym

        from . import agents
        from .factory_env import FactoryEnv
        from .factory_env_cfg import (
            FactoryTaskGearMeshCfg,
            FactoryTaskNutThreadCfg,
            FactoryTaskPegInsertCfg,
        )
    except Exception:
        return

    def _maybe_register(env_id: str, cfg_cls) -> None:
        try:
            gym.spec(env_id)
            return
        except Exception:
            pass
        gym.register(
            id=env_id,
            entry_point=f"{__name__}.factory_env:FactoryEnv",
            disable_env_checker=True,
            kwargs={
                "env_cfg_entry_point": cfg_cls,
                "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
            },
        )

    _maybe_register("TacEx-Factory-PegInsert-Direct-v0", FactoryTaskPegInsertCfg)
    _maybe_register("TacEx-Factory-GearMesh-Direct-v0", FactoryTaskGearMeshCfg)
    _maybe_register("TacEx-Factory-NutThread-Direct-v0", FactoryTaskNutThreadCfg)


# Try to register at import time (but don't fail if dependencies aren't present).
register_gym_envs()


__all__ = [
    "FactoryTask",
    "FixedAssetCfg",
    "HeldAssetCfg",
    "RobotCfg",
    "PegInsert",
    "GearMesh",
    "NutThread",
    "register_gym_envs",
]
