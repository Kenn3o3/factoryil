"""Reproducibility utilities for FactoryIL.

Centralizes seed-setting for:
- Python stdlib (`random`)
- NumPy (`np.random`)
- PyTorch (`torch` / CUDA)

We hardcode a single repo-wide seed (requested). Full bitwise determinism is not
always guaranteed across GPU drivers / Isaac Sim versions, but this makes runs
seeded and repeatable within the same stack (best-effort).
"""

from __future__ import annotations

import os
import random
from typing import Optional


# Hardcoded, repo-wide seed (requested).
FACTORYIL_FIXED_SEED: int = 0


def seed_everything(seed: int = FACTORYIL_FIXED_SEED, deterministic: bool = True) -> int:
    """Seed Python/NumPy/Torch RNGs (best-effort) and enable deterministic modes.

    Returns the seed used.
    """
    try:
        # Only fully effective when set before interpreter start, but still
        # useful to set and we also set it in `run_experiment.py` for children.
        os.environ.setdefault("PYTHONHASHSEED", str(int(seed)))
    except Exception:
        pass

    if deterministic:
        # Deterministic cuBLAS algorithms (important for some torch GPU ops).
        try:
            os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        except Exception:
            pass

    random.seed(int(seed))

    try:
        import numpy as np

        np.random.seed(int(seed))
    except Exception:
        pass

    try:
        import torch

        torch.manual_seed(int(seed))
        if torch.cuda.is_available():
            torch.cuda.manual_seed(int(seed))
            torch.cuda.manual_seed_all(int(seed))

        if deterministic:
            try:
                torch.backends.cudnn.deterministic = True
                torch.backends.cudnn.benchmark = False
            except Exception:
                pass
            try:
                torch.use_deterministic_algorithms(True)
            except Exception:
                pass
    except Exception:
        pass

    return int(seed)


def seed_worker(worker_id: int, base_seed: Optional[int] = None) -> None:
    """Deterministically seed a PyTorch DataLoader worker."""
    try:
        import torch

        worker_seed = int(torch.initial_seed() % 2**32)
    except Exception:
        worker_seed = int(base_seed or FACTORYIL_FIXED_SEED) + int(worker_id)

    random.seed(worker_seed)
    try:
        import numpy as np

        np.random.seed(worker_seed)
    except Exception:
        pass


__all__ = ["FACTORYIL_FIXED_SEED", "seed_everything", "seed_worker"]


