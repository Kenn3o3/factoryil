"""Helpers for running Franky demos.

PYTHONPATH cannot make binary wheels (like franky-control/libfranka) available in
an unrelated conda environment. So the recommended approach is to re-exec the
current script under the target conda environment before importing `franky`.
"""

from __future__ import annotations

import os
import shlex
import shutil
import sys
from pathlib import Path


def activate_franka_conda_env(script_path: str | os.PathLike[str] | None = None) -> None:
    target_env = os.environ.get("FRANKA_CONDA_ENV", "franka_arm")
    current_env = os.environ.get("CONDA_DEFAULT_ENV")
    if not current_env:
        conda_prefix = os.environ.get("CONDA_PREFIX")
        if conda_prefix:
            current_env = Path(conda_prefix).name
    if current_env == target_env:
        if os.environ.get("FRANKA_DEMO_DEBUG") == "1":
            print(
                f"[franka] Using python={sys.executable} env={current_env} prefix={os.environ.get('CONDA_PREFIX')}",
                file=sys.stderr,
            )
        return

    # Avoid accidental recursion if something is misconfigured.
    if os.environ.get("FRANKA_DEMO_NO_REEXEC") == "1":
        return

    conda_exe = os.environ.get("CONDA_EXE") or shutil.which("conda")
    if not conda_exe:
        raise RuntimeError(
            "Cannot find `conda` on PATH. Either run this script with the "
            f"Python from env '{target_env}', or use: conda run -n {target_env} "
            f"python <path/to/script.py>"
        )

    # When imported, __file__ points to this module; we want the entry script.
    entry = Path(script_path) if script_path is not None else Path(sys.argv[0])
    entry = entry.expanduser()
    if not entry.is_absolute():
        entry = (Path.cwd() / entry).resolve()
    if not entry.exists():
        raise RuntimeError(f"Entry script not found: {entry}")

    cmd = [conda_exe, "run", "-n", target_env, "python", str(entry), *sys.argv[1:]]
    print("Activating Franka Enviroment")
    env = dict(os.environ)
    env["FRANKA_DEMO_NO_REEXEC"] = "1"
    os.execvpe(cmd[0], cmd, env)