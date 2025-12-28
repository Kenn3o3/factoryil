# FactoryIL/config.py
import os
import time
from dataclasses import dataclass

# All default knobs live here. Keep CLI small and override only the essentials.

# Image sizes
RGB_H = 256
RGB_W = 512
STACK_RGB = 1

TACT_H = 32
TACT_W = 32

# Optional depth scaling (keep 1.0 to pass raw depth; adjust if your env requires normalization)
DEPTH_SCALE = 1.0

# Point cloud
PC_NUM_POINTS = 20000
PC_FROM_CAMERA = True  # build point cloud from camera depth
# If False, point clouds are transformed to the per-env "world/env" frame:
#   pc_env = pc_world - env.scene.env_origins
# This ensures that identical object placements across parallel envs map to the
# same coordinates (standard robotics convention).
PC_IN_CAMERA_FRAME = False  # output pc in camera frame (not env/world)

# PPO defaults (legacy; no longer used by default)
LR = 1e-4
GAMMA = 0.995
GAE_LAMBDA = 0.95
CLIP_COEF = 0.2
VF_COEF = 2.0
ENT_COEF = 0.0
MAX_GRAD_NORM = 1.0

UPDATE_HORIZON = 64
PPO_EPOCHS = 4
MINIBATCH_SIZE = 1024

# Output
OUT_DIR = os.environ.get("FACTORYIL_OUT_DIR", "out")

# TensorBoard toggle (kept as a code-level toggle, not a CLI arg)
USE_TENSORBOARD = False

@dataclass(frozen=True)
class ModalityConfig:
    use_rgb: bool
    use_depth: bool
    use_tactile: bool
    use_pc: bool = False
    stack_rgb: int = STACK_RGB

# Model registry (RL-only, LSTM policies)
# Provide explicit LSTM model keys and keep legacy synonyms mapped to LSTM variants for convenience.
MODEL_TO_MODALITY = {
    # LSTM models (preferred keys)
    "lstm_proprio": ModalityConfig(use_rgb=False, use_depth=False, use_tactile=False, use_pc=False),
    "lstm_rgb_proprio": ModalityConfig(use_rgb=True, use_depth=False, use_tactile=False, use_pc=False),
    "lstm_rgbd_proprio": ModalityConfig(use_rgb=True, use_depth=True, use_tactile=False, use_pc=False),
    "lstm_rgb_tactile_proprio": ModalityConfig(use_rgb=True, use_depth=False, use_tactile=True, use_pc=False),
    "lstm_rgbd_tactile_proprio": ModalityConfig(use_rgb=True, use_depth=True, use_tactile=True, use_pc=False),

    # Legacy synonyms mapped to LSTM variants
    "mlp_proprio": ModalityConfig(use_rgb=False, use_depth=False, use_tactile=False, use_pc=False),
    "rgb_proprio": ModalityConfig(use_rgb=True, use_depth=False, use_tactile=False, use_pc=False),
    "rgb_tactile_proprio": ModalityConfig(use_rgb=True, use_depth=False, use_tactile=True, use_pc=False),
    "rgbd_tactile_proprio": ModalityConfig(use_rgb=True, use_depth=True, use_tactile=True, use_pc=False),
}

def default_run_name():
    return time.strftime("%Y-%m-%d_%H-%M-%S")