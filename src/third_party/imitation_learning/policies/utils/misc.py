import numpy as np
import torch
from typing import Any
import omegaconf
import importlib
from omegaconf import OmegaConf


def to_torch(x: Any, device: torch.device | str):
    """
    递归地将 numpy 数组与张量搬到指定 device。
    - dict: 递归到值
    - list/tuple: 递归到元素（保持类型）
    - numpy.ndarray: 转为 torch.tensor 并搬到 device
    - torch.Tensor: 直接搬到 device
    - 其他类型: 原样返回
    """
    if isinstance(x, dict):
        return {k: to_torch(v, device) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return type(x)(to_torch(v, device) for v in x)
    if torch.is_tensor(x):
        return x.to(device)
    if isinstance(x, np.ndarray):
        return torch.from_numpy(x).to(device)
    return x

def rotate_around_z(
    points,
    angle_rad=0.0,
    center=np.array([0.0, 0.0, 0.0]),
    scale=np.array([1.0, 1.0, 1.0]),
):
    # 简单的围绕 z 轴旋转与缩放（用于数据增强或可视化）
    assert (len(points.shape) == 1 and len(points) == 3) or points.shape[-1] == 3
    p_shape = points.shape
    points = points.reshape(-1, 3) - center[None]

    # Create the rotation matrix
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)
    rotation_matrix = np.array(
        [[cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0, 0, 1]]
    )

    # Apply the rotation to all points using matrix multiplication
    rotated_points = np.dot(points, rotation_matrix.T) * scale[None] + center[None]
    rotated_points = rotated_points.reshape(p_shape)

    return rotated_points

def get_agent(name):
    lname = str(name).lower()
    if lname == "dp":
        from ..agents.dp_agent import DPAgent
        return DPAgent
    if lname in ("drift_dp", "driftdp", "drift-dp"):
        from ..agents.drift_dp_agent import DriftDPAgent
        return DriftDPAgent
    if lname == "equibot":
        from ..agents.equibot_agent import EquiBotAgent
        return EquiBotAgent
    raise ValueError(f"Unknown agent name: {name}")

# def get_dataset(cfg, mode):
#     # If you previously imported datasets at top-level, do the same lazy pattern here if needed.
#     # Prefer the BaseDataset by default (as your EquiBot precompute uses it).
#     from policies.datasets.dataset import BaseDataset
#     ds_cfg = cfg.data.dataset if hasattr(cfg, "data") else cfg["data"]["dataset"]
#     return BaseDataset(ds_cfg, mode)

def get_dataset(cfg, mode):
    """
    cfg is the Hydra config (root). If cfg.data.dataset._target_ is set,
    instantiate that dataset; otherwise use BaseDataset.
    """
    target = OmegaConf.select(cfg, "data.dataset._target_", default=None)
    if target is not None:
        if target == "policies.datasets.rfm_dataset.RFMDataset":
            from ..datasets.rfm_dataset import RFMDataset  # type: ignore
            return RFMDataset(cfg.data, mode)
        # Generic dynamic import (optional)
        module, name = target.rsplit(".", 1)
        Cls = getattr(importlib.import_module(module), name)
        return Cls(cfg.data, mode)

    # Fallback: original BaseDataset
    from ..datasets.dataset import BaseDataset
    return BaseDataset(cfg.data.dataset, mode)