#!/usr/bin/env python
import argparse
import glob
import os
import re
import shlex
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, TextIO, Union

import yaml  # pip install pyyaml


def _iso_now() -> str:
    return datetime.now().astimezone().isoformat()


def _resolve_against_repo_root(repo_root: str, p: str) -> str:
    if os.path.isabs(p):
        return os.path.abspath(p)
    return os.path.abspath(os.path.join(repo_root, p))

def _sanitize_for_filename(s: str) -> str:
    """Make a best-effort safe filename stem from an arbitrary string."""
    s = str(s).strip().replace(" ", "_")
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)
    s = s.strip("._-")
    if not s:
        return "step"
    # Keep filenames reasonably short for filesystem compatibility.
    return s[:180]


def _is_parallel_group(step: Any) -> bool:
    return isinstance(step, dict) and "parallel" in step


def _terminate_process_group(proc: subprocess.Popen, timeout_s: float = 10.0) -> None:
    """Terminate a subprocess *and its process group* (best-effort)."""
    try:
        if proc.poll() is not None:
            return
    except Exception:
        pass

    pid = getattr(proc, "pid", None)
    if not pid:
        try:
            proc.terminate()
        except Exception:
            pass
        return

    # We launch with start_new_session=True, so pid is the PGID leader.
    try:
        os.killpg(pid, signal.SIGTERM)
    except Exception:
        try:
            proc.terminate()
        except Exception:
            pass

    try:
        proc.wait(timeout=timeout_s)
        return
    except Exception:
        pass

    try:
        os.killpg(pid, signal.SIGKILL)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


StepIdx = Union[int, str]


class _TimeLogger:
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

        existed = os.path.exists(path)
        self._f: TextIO = open(path, "a", buffering=1, encoding="utf-8")
        if not existed or os.path.getsize(path) == 0:
            self._f.write("# timestamp\tevent\tstep_idx\tstep_name\tstatus\tduration_s\n")

        self._f.write(f"# run_started\t{_iso_now()}\n")
        self._f.flush()

    def log_step_start(self, step_idx: StepIdx, step_name: str) -> None:
        self._f.write(f"{_iso_now()}\tSTART\t{step_idx}\t{step_name}\t\t\n")
        self._f.flush()

    def log_step_end(self, step_idx: StepIdx, step_name: str, status: str, duration_s: float) -> None:
        self._f.write(
            f"{_iso_now()}\tEND\t{step_idx}\t{step_name}\t{status}\t{duration_s:.3f}\n"
        )
        self._f.flush()

    def close(self) -> None:
        try:
            self._f.write(f"# run_ended\t{_iso_now()}\n")
            self._f.flush()
        finally:
            self._f.close()


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


def run_step(step, env, time_logger: Optional[_TimeLogger] = None, step_idx: StepIdx = 0):
    name = step.get("name", "<unnamed>")
    kind = step.get("kind", "python_module")

    cmd = build_python_cmd(kind, step)

    if time_logger is not None:
        time_logger.log_step_start(step_idx, name)
    t0 = time.perf_counter()
    status = "ok"

    print(f"\n=== Running step: {name} ===")
    print(cmd)
    try:
        subprocess.run(cmd, shell=True, check=True, env=env)
    except subprocess.CalledProcessError as e:
        status = f"error({e.returncode})"
        raise
    except KeyboardInterrupt:
        status = "interrupted"
        raise
    finally:
        if time_logger is not None:
            duration_s = time.perf_counter() - t0
            time_logger.log_step_end(step_idx, name, status, duration_s)


def run_parallel_group(
    group_step: Dict[str, Any],
    env: Dict[str, str],
    time_logger: Optional[_TimeLogger],
    step_idx: int,
    logs_dir: str,
) -> None:
    """
    Run a YAML step-group of the form:

      - name: <optional group name>
        parallel:
          - name: child_a
            ...
          - name: child_b
            ...
    """
    group_name = str(group_step.get("name") or f"parallel_{step_idx}")
    children = group_step.get("parallel")
    if not isinstance(children, list) or not children:
        raise ValueError(
            f"Parallel step-group {group_name!r} must contain a non-empty list under key 'parallel'."
        )

    os.makedirs(logs_dir, exist_ok=True)

    if time_logger is not None:
        time_logger.log_step_start(step_idx, group_name)
    group_t0 = time.perf_counter()
    group_status = "ok"

    print(f"\n=== Running parallel group: {group_name} ({len(children)} steps) ===")

    launched = []
    try:
        # 1) Launch all children.
        for j, child in enumerate(children, start=1):
            if not isinstance(child, dict):
                raise ValueError(
                    f"Parallel group {group_name!r} contains a non-dict child at index {j}: {type(child)}"
                )

            child_name = str(child.get("name") or f"child_{j}")
            child_kind = child.get("kind", "python_module")
            child_cmd = build_python_cmd(child_kind, child)

            child_idx: StepIdx = f"{step_idx}.{j}"
            log_path = os.path.join(
                logs_dir,
                f"{_sanitize_for_filename(str(child_idx))}__{_sanitize_for_filename(group_name)}__{_sanitize_for_filename(child_name)}.log",
            )
            print(f"[parallel] {child_idx} {child_name} -> {log_path}")
            print(child_cmd)

            if time_logger is not None:
                time_logger.log_step_start(child_idx, f"{group_name}/{child_name}")
            t0 = time.perf_counter()

            # Redirect stdout/stderr to a per-step log to avoid interleaved output.
            log_f = open(log_path, "w", buffering=1, encoding="utf-8")
            proc = subprocess.Popen(
                child_cmd,
                shell=True,
                env=env,
                stdout=log_f,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            launched.append(
                {
                    "j": j,
                    "idx": child_idx,
                    "name": child_name,
                    "full_name": f"{group_name}/{child_name}",
                    "cmd": child_cmd,
                    "proc": proc,
                    "log_f": log_f,
                    "log_path": log_path,
                    "t0": t0,
                    "ended": False,
                }
            )

        # 2) Poll until all done, failing fast if any child errors.
        first_failure = None
        while True:
            all_done = True
            for info in launched:
                proc = info["proc"]
                rc = proc.poll()
                if rc is None:
                    all_done = False
                    continue

                if not info["ended"]:
                    info["ended"] = True
                    duration_s = time.perf_counter() - info["t0"]
                    status = "ok" if rc == 0 else f"error({rc})"
                    if time_logger is not None:
                        time_logger.log_step_end(info["idx"], info["full_name"], status, duration_s)
                    if rc != 0 and first_failure is None:
                        first_failure = info

            if first_failure is not None:
                break
            if all_done:
                break
            time.sleep(0.2)

        if first_failure is not None:
            group_status = f"error({first_failure['proc'].returncode})"
            print(
                f"[parallel] ERROR in {first_failure['full_name']} (rc={first_failure['proc'].returncode}). "
                f"Terminating remaining jobs...",
                flush=True,
            )
            # Terminate anything still running.
            for info in launched:
                if info is first_failure:
                    continue
                if info["proc"].poll() is None:
                    _terminate_process_group(info["proc"])

            # Ensure all are ended and logged.
            for info in launched:
                if info["proc"].poll() is None:
                    try:
                        info["proc"].wait(timeout=5.0)
                    except Exception:
                        _terminate_process_group(info["proc"], timeout_s=0.0)
                if not info["ended"]:
                    info["ended"] = True
                    rc = info["proc"].returncode
                    duration_s = time.perf_counter() - info["t0"]
                    status = "ok" if rc == 0 else f"error({rc})"
                    if time_logger is not None:
                        time_logger.log_step_end(info["idx"], info["full_name"], status, duration_s)

            raise subprocess.CalledProcessError(
                returncode=int(first_failure["proc"].returncode or 1),
                cmd=first_failure["cmd"],
            )

    except KeyboardInterrupt:
        group_status = "interrupted"
        print("[parallel] Interrupted. Terminating all parallel jobs...", flush=True)
        for info in launched:
            _terminate_process_group(info["proc"])
        raise
    finally:
        for info in launched:
            try:
                info["log_f"].close()
            except Exception:
                pass
        if time_logger is not None:
            time_logger.log_step_end(step_idx, group_name, group_status, time.perf_counter() - group_t0)


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
    # Hardcoded determinism knobs for all child steps.
    # Note: PYTHONHASHSEED only affects hashing if set at process start; this is
    # why we set it here for subprocesses launched by this runner.
    env.setdefault("PYTHONHASHSEED", "0")
    # Deterministic cuBLAS algorithms (important for some torch GPU ops).
    env.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")

    for k, v in (cfg.get("env") or {}).items():
        env[k] = str(v)

    timelog_path = cfg.get("timelog_path") or cfg.get("timelog")
    if not timelog_path:
        exp_name = cfg.get("name") or "experiment"
        timelog_path = f"data/{exp_name}/timelog"

    timelog_abspath = _resolve_against_repo_root(repo_root, str(timelog_path))
    time_logger = _TimeLogger(timelog_abspath)
    print(f"[run_experiment] timelog: {timelog_path!r} -> {timelog_abspath!r}")

    exp_name = cfg.get("name") or "experiment"
    logs_dir = cfg.get("logs_dir") or cfg.get("log_dir") or f"data/{exp_name}/logs"
    logs_abspath = _resolve_against_repo_root(repo_root, str(logs_dir))
    os.makedirs(logs_abspath, exist_ok=True)
    print(f"[run_experiment] logs: {logs_dir!r} -> {logs_abspath!r}")

    try:
        for i, step in enumerate(cfg.get("steps", []), start=1):
            if _is_parallel_group(step):
                run_parallel_group(
                    step,
                    env,
                    time_logger=time_logger,
                    step_idx=i,
                    logs_dir=logs_abspath,
                )
            else:
                run_step(step, env, time_logger=time_logger, step_idx=i)
    finally:
        time_logger.close()


if __name__ == "__main__":
    main()