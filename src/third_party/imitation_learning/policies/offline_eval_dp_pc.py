#!/usr/bin/env python
"""
Offline imitation evaluation for the point-cloud Diffusion Policy (DP, pc mode)
trained on FactoryIL expert peg-insertion data.

This script:
- loads a Hydra config and DP checkpoint from a given training run
- constructs train/test datasets restricted to `episode00` and `episode01`
- runs the policy in open-loop on those NPZ frames (no environment)
- reports per-step L2 errors between predicted and ground-truth actions.

Usage (from workspace root, with your IsaacLab environment activated):

  python -m imitation_learning.policies.offline_eval_dp_pc \
    --config path/to/run/.hydra/config.yaml \
    --ckpt   path/to/run/ckpt_best.pth
"""

from __future__ import annotations

import copy
import argparse
import os
from typing import Tuple, Optional

import numpy as np
import torch
from omegaconf import OmegaConf

from .utils.misc import get_agent, get_dataset


def _load_cfg(config_path: str, device: Optional[str] = None):
    """Load a Hydra config.yaml from a training run and adapt it for eval."""
    cfg = OmegaConf.load(os.path.abspath(config_path))

    # Switch to eval mode so DPAgent does not allocate optimizer / scheduler.
    cfg.mode = "eval"
    cfg.use_wandb = False

    if device is not None:
        cfg.device = device

    # Ensure obs_mode is pc and agent is DP (sanity for this script).
    obs_mode = str(OmegaConf.select(cfg, "model.obs_mode", default="pc"))
    agent_name = str(OmegaConf.select(cfg, "agent.agent_name", default="dp"))
    if obs_mode != "pc":
        raise ValueError(f"Expected pc-based DP config; got model.obs_mode={obs_mode!r}")
    if agent_name.lower() != "dp":
        raise ValueError(f"Expected DP agent; got agent_name={agent_name!r}")

    return cfg


def _build_datasets(cfg) -> Tuple[torch.utils.data.Dataset, torch.utils.data.Dataset]:
    """
    Build train/test datasets restricted to episode00 (train) and episode01 (test),
    regardless of how the original training script performed splitting.
    """
    train_cfg = copy.deepcopy(cfg)
    test_cfg = copy.deepcopy(cfg)

    # Explicitly pin episodes by name; BaseDataset filters by episode_names.
    train_cfg.data.dataset.episode_names = ["episode00"]
    test_cfg.data.dataset.episode_names = ["episode01"]

    train_ds = get_dataset(train_cfg, mode="train")
    test_ds = get_dataset(test_cfg, mode="test")
    return train_ds, test_ds


def _eval_split(agent, dataset, split_name: str, max_samples: Optional[int] = None):
    """
    Run the DP policy open-loop on NPZ frames and compare to ground-truth actions.

    For each sample:
      - Build `obs` in the same format that DPAgent.act expects for pc mode:
        * state: [Ho, num_eef, eef_dim]
        * pc:    list of length Ho, each (N, 3)
      - Call agent.act(obs) to get predicted action sequence [Hp, num_eef*dof].
      - Compare the first 6 action dims (SE(3) delta; gripper dim is constant-zero
        in the dataset) against ground-truth and accumulate per-step L2.
    """
    obs_h = int(agent.obs_horizon)
    pred_h = int(agent.pred_horizon)
    dof = int(agent.dof)
    num_eef = int(agent.num_eef)

    n = len(dataset) if max_samples is None else min(len(dataset), max_samples)
    if n == 0:
        print(f"[offline_eval_dp_pc] Split {split_name}: dataset is empty.")
        return

    per_sample_l2 = []

    for idx in range(n):
        sample = dataset[idx]
        state = sample["eef_pose_w"]  # [Ho, num_eef, eef_dim]
        pc = sample["pc"]  # [Ho, N, 3]
        gt_action = sample["action"]  # [Hp, dof_full]

        if state.shape[0] != obs_h or pc.shape[0] != obs_h:
            raise RuntimeError(
                f"Sample {idx} in split {split_name} has mismatched horizons: "
                f"state.shape[0]={state.shape[0]}, pc.shape[0]={pc.shape[0]}, "
                f"expected obs_h={obs_h}"
            )

        # Ensure numpy float32.
        state_np = state.astype(np.float32)
        pc_np = pc.astype(np.float32)
        gt_action_np = gt_action.astype(np.float32)

        # Build observation dict for DPAgent.act (no batch dim).
        obs = {
            "state": state_np,  # [Ho, num_eef, eef_dim]
            "pc": [pc_np[t] for t in range(obs_h)],  # list of Ho arrays (N,3)
        }

        pred = agent.act(obs, return_dict=False, debug=False)
        pred = np.asarray(pred, dtype=np.float32)  # [Hp, num_eef*dof]

        # Align horizons (in case of slight mismatch).
        Hp_eff = min(pred.shape[0], gt_action_np.shape[0], pred_h)
        pred = pred[:Hp_eff]
        gt_action_np = gt_action_np[:Hp_eff]

        # Compare only the first 6 dims (SE(3) delta); gripper dim is constant.
        pred6 = pred[..., :6]
        gt6 = gt_action_np[..., :6]

        diff = pred6 - gt6  # [Hp_eff, 6]
        l2_per_t = np.linalg.norm(diff, axis=-1)  # [Hp_eff]
        per_sample_l2.append(float(l2_per_t.mean()))

    per_sample_l2 = np.asarray(per_sample_l2, dtype=np.float32)
    print(
        f"[offline_eval_dp_pc] Split {split_name}: "
        f"n={n}, mean per-step L2 over first 6 action dims = "
        f"{per_sample_l2.mean():.6e} (std={per_sample_l2.std():.6e})"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Offline imitation evaluation for DP (pc mode) on FactoryIL NPZ data."
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to Hydra config.yaml from the DP training run.",
    )
    parser.add_argument(
        "--ckpt",
        type=str,
        required=True,
        help="Path to DP checkpoint .pth (e.g., ckpt_best.pth).",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Override device in config (e.g., 'cuda' or 'cuda:0'); "
        "if omitted, uses the device from the config file.",
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=None,
        help="Optional cap on number of samples per split to evaluate.",
    )
    args = parser.parse_args()

    cfg = _load_cfg(args.config, device=args.device)

    # Resolve dataset path; config already has it baked in from training.
    data_path = str(OmegaConf.select(cfg, "data_path", default=None))
    if not data_path:
        data_path = str(OmegaConf.select(cfg, "data.dataset.path", default=""))
    if not data_path:
        raise ValueError("No dataset path found in config; please set data_path.")
    if not os.path.isdir(data_path):
        raise FileNotFoundError(f"Data directory not found: {data_path}")

    # Build datasets restricted to episode00 / episode01.
    train_ds, test_ds = _build_datasets(cfg)

    # Instantiate and load DP agent.
    AgentCls = get_agent(cfg.agent.agent_name)
    agent = AgentCls(cfg)
    agent.load_snapshot(os.path.abspath(args.ckpt))
    agent.train(False)

    # Evaluate both splits.
    _eval_split(agent, train_ds, "train", max_samples=args.max_samples)
    _eval_split(agent, test_ds, "test", max_samples=args.max_samples)


if __name__ == "__main__":
    main()