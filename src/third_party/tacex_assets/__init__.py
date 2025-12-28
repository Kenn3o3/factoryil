"""TacEx assets (vendored).

The upstream TacEx project ships as an Isaac Sim extension and reads metadata
from `config/extension.toml`. In this repo we vendor it as a plain python
package under `src/third_party`, so we avoid extension-specific metadata at
import time.
"""

from __future__ import annotations

import os

# Path to the package directory (contains the `data/` folder).
_PKG_DIR = os.path.dirname(__file__)

# Public constant used throughout TacEx configs.
TACEX_ASSETS_DATA_DIR = os.path.join(_PKG_DIR, "data")

# Best-effort version (the exact extension version is not required by FactoryIL).
__version__ = "0.0.0"

__all__ = ["TACEX_ASSETS_DATA_DIR", "__version__"]
