"""Path utilities for third-party dependencies."""

from pathlib import Path


def get_project_root() -> Path:
    """Get project root directory."""
    # Assuming this file is in src/franka/utils/paths.py
    return Path(__file__).resolve().parents[3]


def get_gsrobotics_path() -> Path:
    """Get path to gsrobotics library."""
    return get_project_root() / "src" / "third_party" / "gsrobotics"


def get_pyorbbecsdk_path() -> Path:
    """Get path to pyorbbecsdk library."""
    return get_project_root() / "src" / "third_party" / "pyorbbecsdk"


def get_pyorbbecsdk_examples_path() -> Path:
    """Get path to pyorbbecsdk examples."""
    return get_pyorbbecsdk_path() / "examples"
