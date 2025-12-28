#!/usr/bin/env python
import argparse
import glob
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import yaml  # pip install pyyaml


def _find_repo_root(start_dir: str) -> str:
    """Find the repo root by walking upwards until a `pyproject.toml` is found.

    This makes experiment YAMLs robust to the current shell working directory.
    """
    d = Path(start_dir).resolve()
    for p in [d, *d.parents]:
        if (p / "pyproject.toml").is_file():
            return str(p)
    # Fallback: best-effort to the config's directory.
    return str(d)


def _expand_value(value: Any, context: Dict[str, Any]) -> Any:
    if isinstance(value, str):
        try:
            return value.format(**context)
        except Exception:
            # If formatting fails (e.g. unknown key), leave string unchanged.
            return value
    if isinstance(value, dict):
        return {k: _expand_value(v, context) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_value(v, context) for v in value]
    return value


def _expand_config(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Expand {placeholders} across the loaded YAML config."""
    # Use simple scalar top-level keys as the formatting context, e.g. "name"
    context: Dict[str, Any] = {
        k: v for k, v in cfg.items() if isinstance(v, (str, int, float))
    }
    return _expand_value(cfg, context)


def _resolve_special_arg(key, value):
    """Handle dynamic argument values that need to be resolved at runtime.

    Currently supported:
      - il_ckpt: if set to a directory, pick the latest ckpt_best.pth under it.
      - if drift_dp, pick the latest ckpt_final_drift_dp.pth under the il_ckpt directory.
    """
    if key == "il_ckpt" and isinstance(value, str) and os.path.isdir(value):
        if "drift_dp" in value:
            pattern = os.path.join(value, "**", "ckpt_best_drift_dp.pth")
            candidates = glob.glob(pattern, recursive=True)
            if not candidates:
                raise FileNotFoundError(
                    f"No ckpt_best_drift_dp.pth found under directory: {value}"
                )
            latest = max(candidates, key=os.path.getmtime)
            print(f"[run_experiment] Resolved il_ckpt dir '{value}' -> '{latest}'")
            return latest
        else:
            pattern = os.path.join(value, "**", "ckpt_best.pth")

            candidates = glob.glob(pattern, recursive=True)
            if not candidates:
                raise FileNotFoundError(
                    f"No ckpt_best.pth found under directory: {value}"
                )
            latest = max(candidates, key=os.path.getmtime)
            print(f"[run_experiment] Resolved il_ckpt dir '{value}' -> '{latest}'")
            return latest

    return value


def _maybe_abspath_arg(key: str, value: Any) -> Any:
    """Convert path-like CLI args to absolute paths.

    This is important for Hydra-based training entrypoints that change the
    process working directory (Hydra run dir). If we pass relative paths like
    `data/OVERFIT_EXPERIMENT/training_data`, Hydra will interpret them relative
    to the run directory and the dataset scan will find zero files.

    We only apply this to common path keys to avoid surprising conversions.
    """
    if not isinstance(value, str):
        return value

    leaf = str(key).split(".")[-1]
    path_keys = {
        "data_path",
        "log_dir",
        "out_dir",
        "data_dir",
        "episodes_root",
        "episode_dir",
        "checkpoint",
        "ckpt",
        "eval_data_path",
    }
    if leaf not in path_keys and not leaf.endswith(("_dir", "_path")):
        return value

    # Only convert clearly-path-like strings.
    if os.path.isabs(value):
        return value
    if ("/" not in value) and (not value.startswith(".")):
        return value
    return os.path.abspath(value)


def build_python_cmd(kind, spec):
    args = spec.get("args", {}) or {}
    py = sys.executable or "python"

    if kind == "python_module":
        module = spec["module"]
        parts = [py, "-m", module]
        # Special handling for Hydra-based training entrypoints.
        # We vendor policy code under `src/third_party/imitation_learning/policies`.
        is_hydra_train = (
            module.endswith("imitation_learning.policies.train")
            or module.endswith("imitation_learning.policies.train_drift_dp")
            # Backward-compat (older recovered configs)
            or module.endswith("factoryil.imitation_learning.policies.train")
            or module.endswith("factoryil.imitation_learning.policies.train_drift_dp")
        )
    elif kind == "python_script":
        parts = [py, spec["script"]]
        is_hydra_train = False
    elif kind == "shell":
        # Direct shell command (no arg -> flag conversion)
        return spec["cmd"]
    else:
        raise ValueError(f"Unknown step kind: {kind}")

    for k, v in args.items():
        v = _resolve_special_arg(k, v)
        v = _maybe_abspath_arg(k, v)

        if is_hydra_train:
            # Hydra CLI style:
            #   python -m ... --config-name dp_pc prefix=EXPERIMENT_1_dp_pc ...
            if k in ("config-name", "config_name"):
                flag = "--config-name"
                parts.extend([flag, str(v)])
                continue

            # Everything else is treated as a Hydra override: key=value
            if isinstance(v, bool):
                v_str = "true" if v else "false"
            else:
                v_str = str(v)
                # Fix for ambiguous comma-separated strings in Hydra (e.g. "coarse,rfm")
                # If it contains comma and is not list syntax, wrap in quotes so Hydra treats as string.
                if "," in v_str and not (v_str.strip().startswith("[") and v_str.strip().endswith("]")):
                    # Only quote if not already quoted.
                    if not (
                        (v_str.startswith("'") and v_str.endswith("'"))
                        or (v_str.startswith('"') and v_str.endswith('"'))
                    ):
                        v_str = f"'{v_str}'"

            parts.append(f"{k}={v_str}")
        else:
            # Standard argparse-style flags: keep underscores as-is so they
            # match definitions like --num_envs, --timeout_s, etc.
            flag = f"--{k}"

            # bool flags: use presence/absence
            if isinstance(v, bool):
                if v:
                    parts.append(flag)
            else:
                parts.extend([flag, str(v)])

    return " ".join(shlex.quote(p) for p in parts)


def run_step(step, env):
    name = step.get("name", "<unnamed>")
    kind = step.get("kind", "python_module")

    cmd = build_python_cmd(kind, step)

    print(f"\n=== Running step: {name} ===")
    print(cmd)
    subprocess.run(cmd, shell=True, check=True, env=env)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="Path to experiment YAML")
    args = parser.parse_args()

    cfg_path = os.path.abspath(args.config)
    cfg_dir = os.path.dirname(cfg_path)
    repo_root = _find_repo_root(cfg_dir)

    with open(cfg_path, "r") as f:
        raw_cfg = yaml.safe_load(f)

    # First expand any {placeholders} based on top-level fields
    cfg = _expand_config(raw_cfg)

    # Working directory
    workdir = cfg.get("workdir")
    if workdir:
        # Interpret relative `workdir` relative to the repo root (not the
        # current shell cwd), so `workdir: .` means "repo root".
        resolved = workdir if os.path.isabs(workdir) else os.path.join(repo_root, workdir)
        resolved = os.path.abspath(resolved)
        os.chdir(resolved)
        print(f"[run_experiment] workdir: {workdir!r} -> {resolved!r}")

    # Environment variables
    env = os.environ.copy()
    for k, v in (cfg.get("env") or {}).items():
        env[k] = str(v)

    for step in cfg.get("steps", []):
        run_step(step, env)


if __name__ == "__main__":
    main()