from __future__ import annotations

import os
from typing import Dict

import numpy as np
import torch
import torch.nn.functional as F


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _to_uint8_image(arr: np.ndarray) -> np.ndarray:
    """Convert an array-like image to uint8 HWC if possible."""
    arr = np.asarray(arr)
    if arr.dtype != np.uint8:
        m = float(arr.max()) if arr.size else 1.0
        if m <= 1.0 + 1e-6:
            arr = arr * 255.0
        arr = np.clip(arr, 0, 255).astype(np.uint8)
    # If CHW, convert to HWC
    if arr.ndim == 3 and arr.shape[0] in (1, 3, 4) and arr.shape[-1] not in (3, 4):
        arr = np.transpose(arr, (1, 2, 0))
    return arr


def fetch_tactile_images(env) -> Dict[str, Dict[str, np.ndarray]]:
    """Fetch GelSight Mini tactile sensor outputs as uint8 numpy arrays.

    Expected env structure (FactoryILEnv):
    - `env.unwrapped.scene.sensors["gsmini_left"].data.output["tactile_rgb"]`
    - `env.unwrapped.scene.sensors["gsmini_right"].data.output["tactile_rgb"]`

    Returns:
      dict with keys:
        - "gsmini_left":  {"tactile_rgb": (N,H,W,3) uint8, "height_map": (N,H,W) uint8 (if present)}
        - "gsmini_right": {"tactile_rgb": (N,H,W,3) uint8, "height_map": (N,H,W) uint8 (if present)}
    """
    out: Dict[str, Dict[str, np.ndarray]] = {"gsmini_left": {}, "gsmini_right": {}}
    unwrapped = getattr(env, "unwrapped", env)

    def _as_numpy(x):
        """Convert common Isaac/TacEx outputs to numpy.

        GelSight sensors typically output torch tensors (often on CUDA).
        Converting a CUDA tensor via `np.asarray()` raises, which previously
        caused tactile to be silently dropped by callers.
        """
        if x is None:
            return None
        try:
            if torch.is_tensor(x):
                return x.detach().to("cpu").numpy()
        except Exception:
            pass

        # Handle lists/tuples of tensors/arrays.
        if isinstance(x, (list, tuple)) and len(x) > 0:
            try:
                if torch.is_tensor(x[0]):
                    return torch.stack([t.detach().to("cpu") for t in x], dim=0).numpy()
            except Exception:
                pass

        return np.asarray(x)

    def _get_sensor(name: str):
        try:
            return unwrapped.scene.sensors[name]
        except Exception as e:  # pragma: no cover
            raise RuntimeError(f"Sensor {name!r} not found in env.scene.sensors") from e

    left = _get_sensor("gsmini_left")
    right = _get_sensor("gsmini_right")

    left_rgb = left.data.output.get("tactile_rgb", None)
    right_rgb = right.data.output.get("tactile_rgb", None)
    if left_rgb is None or right_rgb is None:
        raise RuntimeError("GelSight sensors did not produce 'tactile_rgb' output.")

    left_rgb = _as_numpy(left_rgb)
    right_rgb = _as_numpy(right_rgb)
    if left_rgb is None or right_rgb is None:
        raise RuntimeError("GelSight sensors produced no tactile output.")
    out["gsmini_left"]["tactile_rgb"] = np.stack(
        [_to_uint8_image(left_rgb[i]) for i in range(left_rgb.shape[0])], axis=0
    )
    out["gsmini_right"]["tactile_rgb"] = np.stack(
        [_to_uint8_image(right_rgb[i]) for i in range(right_rgb.shape[0])], axis=0
    )

    # height_map is optional.
    left_hm = left.data.output.get("height_map", None)
    right_hm = right.data.output.get("height_map", None)
    if left_hm is not None:
        left_hm = _as_numpy(left_hm)
        out["gsmini_left"]["height_map"] = np.stack(
            [_to_uint8_image(left_hm[i]) for i in range(left_hm.shape[0])], axis=0
        )
    if right_hm is not None:
        right_hm = _as_numpy(right_hm)
        out["gsmini_right"]["height_map"] = np.stack(
            [_to_uint8_image(right_hm[i]) for i in range(right_hm.shape[0])], axis=0
        )

    return out


def create_look_at_quat(eye: torch.Tensor, target: torch.Tensor, up_axis: torch.Tensor) -> torch.Tensor:
    """Compute a quaternion (w,x,y,z) so a frame at `eye` looks at `target`.

    This is a small helper used in some debugging/visualization utilities.
    """
    forward_vec = F.normalize(eye - target, p=2, dim=-1)
    right_vec = F.normalize(torch.cross(up_axis.expand_as(forward_vec), forward_vec, dim=-1), p=2, dim=-1)
    up_vec = torch.cross(forward_vec, right_vec, dim=-1)

    rot_matrix = torch.stack((right_vec, up_vec, forward_vec), dim=-1)

    w = 0.5 * torch.sqrt(
        1.0 + rot_matrix[..., 0, 0] + rot_matrix[..., 1, 1] + rot_matrix[..., 2, 2]
    ).unsqueeze(-1)
    x = (0.5 / w) * (rot_matrix[..., 2, 1] - rot_matrix[..., 1, 2]).unsqueeze(-1)
    y = (0.5 / w) * (rot_matrix[..., 0, 2] - rot_matrix[..., 2, 0]).unsqueeze(-1)
    z = (0.5 / w) * (rot_matrix[..., 1, 0] - rot_matrix[..., 0, 1]).unsqueeze(-1)

    return torch.cat((w, x, y, z), dim=-1)


__all__ = [
    "_ensure_dir",
    "_to_uint8_image",
    "fetch_tactile_images",
    "create_look_at_quat",
]


