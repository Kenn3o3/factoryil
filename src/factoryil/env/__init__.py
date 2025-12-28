"""
FactoryIL: Teleoperation-oriented factory manipulation environments for imitation learning.

This package provides a lightweight Isaac Lab ``DirectRLEnv`` that reuses the TacEx
factory assets (Franka + GelSight Mini gripper + peg/hole/gear/nut tasks), but
switches the control stack to differential IK for smooth SE(3) teleoperation.

Key modules:
- ``factory_env``: Defines :class:`FactoryILEnv`, a DirectRLEnv with 7D actions
  (6D relative EE pose + 1D gripper open/close).
- ``factory_task_cfg``: Task and environment configuration for peg-insertion,
  gear-meshing, and nut-threading variants.
"""

from .factory_env import FactoryILEnv  # noqa: F401
from .factory_task_cfg import (  # noqa: F401
    FactoryILEnvCfg,
    FactoryILPegInsertCfg,
    FactoryILGearMeshCfg,
    FactoryILNutThreadCfg,
)
from .make_env import make_env_and_cfg  # noqa: F401

__all__ = [
    "FactoryILEnv",
    "FactoryILEnvCfg",
    "FactoryILPegInsertCfg",
    "FactoryILGearMeshCfg",
    "FactoryILNutThreadCfg",
    "make_env_and_cfg",
]