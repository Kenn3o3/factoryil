from __future__ import annotations

import csv
from typing import List, Sequence, Tuple

import numpy as np


def _parse_semicolon_floats(s: str) -> List[float]:
    s = (s or "").strip()
    if not s:
        return []
    parts = [p.strip() for p in s.split(";") if p.strip() != ""]
    out: List[float] = []
    for p in parts:
        try:
            out.append(float(p))
        except Exception:
            continue
    return out


def _load_episode_csv(csv_path: str, action_dim: int) -> Tuple[Sequence[int], Sequence[bool], Sequence[np.ndarray]]:
    """Load an episode CSV and return (frames, is_last_flags, actions).

    Expected columns (additional columns are ignored):
      - frame: int
      - is_last: int/bool
      - action: semicolon-separated floats (length == action_dim)
    """
    frames: List[int] = []
    is_last_flags: List[bool] = []
    actions: List[np.ndarray] = []

    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                frame = int(float(row.get("frame", "0")))
            except Exception:
                frame = len(frames)

            is_last_raw = str(row.get("is_last", "0")).strip().lower()
            is_last = is_last_raw in ("1", "true", "t", "yes", "y")

            vals = _parse_semicolon_floats(row.get("action", ""))
            a = np.asarray(vals, dtype=np.float32).reshape(-1)
            if a.size < action_dim:
                pad = np.zeros((action_dim - a.size,), dtype=np.float32)
                a = np.concatenate([a, pad], axis=0)
            elif a.size > action_dim:
                a = a[:action_dim]

            frames.append(frame)
            is_last_flags.append(bool(is_last))
            actions.append(a.astype(np.float32, copy=False))

    return frames, is_last_flags, actions


__all__ = ["_load_episode_csv"]


