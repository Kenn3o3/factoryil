import os
import sys
import copy
from glob import glob

import hydra
import numpy as np
import omegaconf
import torch
import wandb
from omegaconf import OmegaConf
from torch.utils.data._utils.collate import default_collate
from tqdm import tqdm

from .utils.misc import get_dataset, get_agent
from factoryil.utils.seed import seed_everything, seed_worker
from .train import (
    _episode_lengths_from_dir,
    _natural_sort,
    _check_dataset_agent_compat,
)


def _numpy_to_tensor(x):
    """Recursively convert numpy arrays in a sample to fresh CPU tensors."""
    if isinstance(x, dict):
        return {k: _numpy_to_tensor(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return type(x)(_numpy_to_tensor(v) for v in x)
    if isinstance(x, np.ndarray):
        return torch.tensor(x)
    return x


def safe_collate(batch):
    """Collate function that first converts numpy arrays to tensors."""
    converted = [_numpy_to_tensor(sample) for sample in batch]
    return default_collate(converted)


def _parse_modules(cfg_training) -> list:
    modules_str = str(getattr(cfg_training, "modules", "coarse")).strip()
    parts = [m.strip().lower() for m in modules_str.split(",") if m.strip()]
    if not parts:
        parts = ["coarse"]
    allowed = {"coarse", "rfm"}
    if any(p not in allowed for p in parts):
        raise ValueError(f"training.modules must use subset of {allowed}, got {parts}")
    # Normalize convenience forms
    if parts == ["coarse", "rfm"]:
        return ["coarse", "rfm"]
    if parts == ["rfm", "coarse"]:
        return ["coarse", "rfm"]
    return parts


@hydra.main(config_path="configs", config_name="drift_dp_pc")
def main(cfg):
    assert cfg.mode == "train"
    # Deterministic training (best-effort): seed Python/NumPy/Torch (+ CUDA).
    seed_everything(int(cfg.seed), deterministic=True)

    modules = _parse_modules(cfg.training)
    print(f"[train_drift_dp] training.modules = {modules}")

    # Determine coarse / RFM epoch budgets
    if modules == ["coarse"]:
        num_epochs_coarse = int(cfg.training.num_epochs)
        num_epochs_rfm = 0
    elif modules == ["rfm"]:
        num_epochs_coarse = 0
        num_epochs_rfm = int(cfg.training.num_epochs)
    elif modules == ["coarse", "rfm"]:
        num_epochs_coarse = int(getattr(cfg.training, "num_epochs_coarse", cfg.training.num_epochs))
        num_epochs_rfm = int(getattr(cfg.training, "num_epochs_rfm", cfg.training.num_epochs))
    else:
        raise ValueError(f"Unsupported modules combination: {modules}")

    batch_size = cfg.training.batch_size
    print("batch_size: ", batch_size)

    # Gentle sanity check: warn if we are about to train an RFM head with
    # point-cloud–only conditioning (no tactile), which is usually not what
    # DRIFT-DP is designed for in METHOD.md.
    
    if (
        num_epochs_rfm > 0
        and str(getattr(cfg.model, "obs_mode", "")).startswith("pc")
        and not bool(getattr(cfg.model, "rfm_use_tactile", False))
    ):
        print(
            "[train_drift_dp] WARNING: RFM training is enabled but "
            "model.rfm_use_tactile is False while obs_mode='pc'. "
            "This trains a PC-only residual head, which differs from the "
            "visuotactile DRIFT-DP design in METHOD.md. Consider enabling "
            "rfm_use_tactile and providing tactile RGB keys if you intend to "
            "use visuotactile RFM."
        )

    # Optional: W&B logging
    if cfg.use_wandb:
        wandb_config = OmegaConf.to_container(cfg, resolve=True, throw_on_missing=False)
        wandb.init(
            entity=cfg.wandb.entity,
            project=cfg.wandb.project,
            tags=["train", "drift_dp"],
            name=cfg.prefix,
            settings=wandb.Settings(code_dir="."),
            config=wandb_config,
        )

    log_dir = os.getcwd()

    # ------------------------------------------------------------------
    # Episode-level split (reuse logic from train.py)
    # ------------------------------------------------------------------
    ep_len_all = _episode_lengths_from_dir(cfg.data.dataset.path)
    min_demo_len = cfg.data.dataset.min_demo_length
    valid_eps = [ep for ep, L in ep_len_all.items() if L >= min_demo_len]
    if len(valid_eps) == 0:
        raise RuntimeError(
            f"No episodes satisfy min_demo_length={min_demo_len}. "
            f"Found episodes: {len(ep_len_all)}"
        )
    valid_eps_sorted = _natural_sort(valid_eps)
    custom = OmegaConf.select(cfg, "data.custom_split", default=False)

    if custom:
        train_spec = OmegaConf.select(cfg, "data.train_episodes", default=None)
        test_spec = OmegaConf.select(cfg, "data.test_episodes", default=None)

        def resolve(spec):
            if spec is None:
                return []
            seq = list(spec)
            if all(
                isinstance(x, (int, np.integer))
                or (isinstance(x, str) and x.isdigit())
                for x in seq
            ):
                idxs = [int(x) for x in seq]
                names = []
                N = len(valid_eps_sorted)
                for i in idxs:
                    if not (-(N) <= i < N):
                        raise ValueError(f"Episode index {i} out of range for {N} valid episodes")
                    names.append(valid_eps_sorted[i])
                return names
            names = [str(x) for x in seq]
            missing = [n for n in names if n not in valid_eps]
            if missing:
                raise ValueError(
                    f"These episode names are not present or too short: {missing}. "
                    f"Valid episodes: {valid_eps_sorted}"
                )
            return names

        train_eps = resolve(train_spec)
        test_eps = resolve(test_spec)

        if len(train_eps) == 0 and len(test_eps) == 0:
            raise ValueError(
                "data.custom_split is True but neither data.train_episodes "
                "nor data.test_episodes were provided."
            )

        if len(train_eps) == 0:
            train_eps = [ep for ep in valid_eps_sorted if ep not in set(test_eps)]
        if len(test_eps) == 0:
            test_eps = [ep for ep in valid_eps_sorted if ep not in set(train_eps)]

        overlap = set(train_eps) & set(test_eps)
        if overlap:
            raise ValueError(f"Train/Test episode lists overlap: {sorted(overlap)}")
    else:
        rng = np.random.RandomState(cfg.seed)
        rng.shuffle(valid_eps)
        split_ratio = float(cfg.training.train_test_split)
        n_train = int(len(valid_eps) * split_ratio)
        if n_train == 0 and len(valid_eps) > 1:
            n_train = 1
        if n_train == len(valid_eps) and len(valid_eps) > 1:
            n_train = len(valid_eps) - 1
        train_eps = valid_eps[:n_train]
        test_eps = valid_eps[n_train:]

    print(
        f"[train_drift_dp] Episode split: {len(train_eps)} train episodes, "
        f"{len(test_eps)} test episodes (from {len(valid_eps)} valid episodes)."
    )
    print("training episodes selected: ", train_eps)
    print("testing episodes selected: ", test_eps)

    train_log_path = os.path.join(log_dir, "train.log")
    with open(train_log_path, "a") as f:
        f.write(f"[drift_dp] training episodes selected:  {train_eps}\n")
        f.write(f"[drift_dp] testing episodes selected:  {test_eps}\n")

    # Dataset / DataLoader instantiation
    train_cfg = copy.deepcopy(cfg)
    test_cfg = copy.deepcopy(cfg)
    train_cfg.data.dataset.episode_names = train_eps
    test_cfg.data.dataset.episode_names = test_eps

    train_dataset = get_dataset(train_cfg, "train")
    test_dataset = get_dataset(test_cfg, "test")

    # Sanity-check dataset vs agent
    agent_name = str(cfg.agent.agent_name)
    _check_dataset_agent_compat(train_dataset, agent_name)

    num_workers = cfg.data.dataset.num_workers
    batch_size = cfg.training.batch_size
    dl_gen = torch.Generator()
    dl_gen.manual_seed(int(cfg.seed))

    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        shuffle=True,
        drop_last=False,
        pin_memory=True,
        collate_fn=safe_collate,
        worker_init_fn=seed_worker,
        generator=dl_gen,
    )

    test_loader = torch.utils.data.DataLoader(
        test_dataset,
        batch_size=batch_size,
        num_workers=max(1, num_workers // 2),
        shuffle=False,
        drop_last=False,
        pin_memory=True,
        collate_fn=safe_collate,
        worker_init_fn=seed_worker,
    )

    # Number of coarse optimization steps for LR scheduler
    if num_epochs_coarse > 0:
        cfg.data.dataset.num_training_steps = (
            num_epochs_coarse * len(train_dataset) // batch_size
        )
    else:
        cfg.data.dataset.num_training_steps = 1

    # Initialize DRIFT-DP agent
    AgentCls = get_agent(cfg.agent.agent_name)
    agent = AgentCls(cfg)

    # Optional: load coarse / RFM weights as pure initialization.
    coarse_ckpt = getattr(cfg.training, "coarse_ckpt", None)
    if coarse_ckpt is not None:
        agent.load_coarse_state(coarse_ckpt)
    rfm_ckpt = getattr(cfg.training, "rfm_ckpt", None)
    if rfm_ckpt is not None:
        agent.load_rfm_state(rfm_ckpt)

    if cfg.use_wandb:
        wandb.log(
            {
                "data/train_num_frames": len(train_dataset),
                "data/test_num_frames": len(test_dataset),
                "data/train_num_episodes": len(train_eps),
                "data/test_num_episodes": len(test_eps),
            },
            step=0,
        )

    global_step = 0

    # ------------------------------------------------------------------
    # Phase 1 – Coarse DP training (optional)
    # ------------------------------------------------------------------
    best_coarse_metric = float("inf")
    best_coarse_epoch = -1
    if num_epochs_coarse > 0:
        print(f"[train_drift_dp] Starting coarse training for {num_epochs_coarse} epochs.")
        for epoch_ix in tqdm(range(num_epochs_coarse), desc="Coarse Epochs"):
            running_train_loss = 0.0
            running_train_count = 0
            for batch in tqdm(train_loader, leave=False, desc="Coarse Train Batches"):
                train_metrics = agent.update_coarse(batch)
                bs = batch["action"].shape[0]
                loss_val = (
                    train_metrics["loss"].item()
                    if hasattr(train_metrics["loss"], "item")
                    else float(train_metrics["loss"])
                )
                running_train_loss += loss_val * bs
                running_train_count += bs

                if cfg.use_wandb:
                    wandb.log(
                        {
                            "train/coarse_" + k: (
                                v.item() if hasattr(v, "item") else v
                            )
                            for k, v in train_metrics.items()
                        },
                        step=global_step,
                    )
                    wandb.log({"epoch": epoch_ix, "phase": 1}, step=global_step)
                global_step += 1

            train_epoch_loss = running_train_loss / max(1, running_train_count)

            # Evaluation (aggregate whatever metrics the agent chooses to return).
            test_running = {}
            test_count = 0
            for batch in tqdm(test_loader, leave=False, desc="Coarse Test Batches"):
                with torch.no_grad():
                    metrics = agent.evaluate_coarse(batch)
                bs = batch["action"].shape[0]
                for k, v in metrics.items():
                    # Convert possible tensors to float scalars.
                    if hasattr(v, "item"):
                        v_val = float(v.item())
                    else:
                        v_val = float(v)
                    test_running[k] = test_running.get(k, 0.0) + v_val * bs
                test_count += bs

            test_metrics = {
                k: (v / max(1, test_count)) for k, v in test_running.items()
            }

            if cfg.use_wandb:
                log_payload = {
                    "train/coarse_epoch_loss": train_epoch_loss,
                    "epoch": epoch_ix,
                    "phase": 1,
                }
                if "loss" in test_metrics:
                    log_payload["test/coarse_noise_loss"] = test_metrics["loss"]
                if "mean_gt_noise_norm" in test_metrics:
                    log_payload["test/coarse_mean_gt_noise_norm"] = test_metrics[
                        "mean_gt_noise_norm"
                    ]
                if "mean_pred_noise_norm" in test_metrics:
                    log_payload["test/coarse_mean_pred_noise_norm"] = test_metrics[
                        "mean_pred_noise_norm"
                    ]
                if "coarse_action_l2" in test_metrics:
                    log_payload["test/coarse_action_l2"] = test_metrics[
                        "coarse_action_l2"
                    ]
                wandb.log(log_payload, step=global_step)

            # Prefer coarse_action_l2 when available; otherwise fall back to noise loss.
            if "coarse_action_l2" in test_metrics:
                current_metric = float(test_metrics["coarse_action_l2"])
            else:
                current_metric = float(test_metrics.get("loss", float("inf")))
            if current_metric < best_coarse_metric:
                best_coarse_metric = current_metric
                best_coarse_epoch = epoch_ix
                best_ckpt_path = os.path.join(log_dir, "ckpt_best_coarse_drift_dp.pth")
                agent.save_snapshot(best_ckpt_path)
                print(
                    f"[train_drift_dp] New best coarse metric {best_coarse_metric:.6f} "
                    f"at epoch {best_coarse_epoch}. Saved: {best_ckpt_path}"
                )
                if cfg.use_wandb:
                    # Track best coarse metric under a key that reflects what we used.
                    if "coarse_action_l2" in test_metrics:
                        wandb.run.summary["best_coarse/action_l2"] = best_coarse_metric
                    else:
                        wandb.run.summary["best_coarse/loss"] = best_coarse_metric
                    wandb.run.summary["best_coarse/epoch"] = best_coarse_epoch

    # ------------------------------------------------------------------
    # Phase 2 – RFM-only training on frozen coarse (optional)
    # ------------------------------------------------------------------
    if num_epochs_rfm > 0:
        print(f"[train_drift_dp] Starting RFM training for {num_epochs_rfm} epochs.")
        # If we have a best coarse checkpoint from Phase 1, reload it.
        best_coarse_ckpt = os.path.join(log_dir, "ckpt_best_coarse_drift_dp.pth")
        if os.path.exists(best_coarse_ckpt):
            print(f"[train_drift_dp] Reloading best coarse checkpoint: {best_coarse_ckpt}")
            agent.load_coarse_state(best_coarse_ckpt)

        agent.freeze_coarse()
        steps_rfm = num_epochs_rfm * len(train_dataset) // batch_size
        agent.configure_rfm_optim(steps_rfm)

        best_rfm_metric = float("inf")
        best_rfm_epoch = -1

        for epoch_ix in tqdm(range(num_epochs_rfm), desc="RFM Epochs"):
            running_train_loss = 0.0
            running_train_count = 0
            for batch in tqdm(train_loader, leave=False, desc="RFM Train Batches"):
                train_metrics = agent.update_rfm(batch)
                bs = batch["action"].shape[0]
                loss_val = (
                    train_metrics["rfm_residual_loss"].item()
                    if hasattr(train_metrics["rfm_residual_loss"], "item")
                    else float(train_metrics["rfm_residual_loss"])
                )
                running_train_loss += loss_val * bs
                running_train_count += bs

                if cfg.use_wandb:
                    wandb.log(
                        {
                            "train/rfm_" + k: (
                                v.item() if hasattr(v, "item") else v
                            )
                            for k, v in train_metrics.items()
                        },
                        step=global_step,
                    )
                    wandb.log({"epoch": epoch_ix, "phase": 2}, step=global_step)
                global_step += 1

            train_epoch_loss = running_train_loss / max(1, running_train_count)

            # Evaluation
            test_running = {"rfm_residual_loss": 0.0, "refined_action_l2": 0.0}
            test_count = 0
            for batch in tqdm(test_loader, leave=False, desc="RFM Test Batches"):
                with torch.no_grad():
                    metrics = agent.evaluate_rfm(batch)
                bs = batch["action"].shape[0]
                test_running["rfm_residual_loss"] += metrics["rfm_residual_loss"] * bs
                test_running["refined_action_l2"] += metrics["refined_action_l2"] * bs
                test_count += bs

            test_metrics = {
                k: (v / max(1, test_count)) for k, v in test_running.items()
            }

            if cfg.use_wandb:
                wandb.log(
                    {
                        "train/rfm_epoch_loss": train_epoch_loss,
                        "test/rfm_residual_loss": test_metrics["rfm_residual_loss"],
                        "test/refined_action_l2": test_metrics["refined_action_l2"],
                        "epoch": epoch_ix,
                        "phase": 2,
                    },
                    step=global_step,
                )

            current_metric = float(test_metrics["refined_action_l2"])
            if current_metric < best_rfm_metric:
                best_rfm_metric = current_metric
                best_rfm_epoch = epoch_ix
                best_ckpt_path = os.path.join(log_dir, "ckpt_best_drift_dp.pth")
                agent.save_snapshot(best_ckpt_path)
                print(
                    f"[train_drift_dp] New best RFM metric {best_rfm_metric:.6f} "
                    f"at epoch {best_rfm_epoch}. Saved: {best_ckpt_path}"
                )
                if cfg.use_wandb:
                    wandb.run.summary["best_rfm/refined_action_l2"] = best_rfm_metric
                    wandb.run.summary["best_rfm/epoch"] = best_rfm_epoch

        # Also save final combined DRIFT-DP model
        final_ckpt_path = os.path.join(log_dir, "ckpt_final_drift_dp.pth")
        agent.save_snapshot(final_ckpt_path)
        print(f"[train_drift_dp] Saved final DRIFT-DP checkpoint: {final_ckpt_path}")


if __name__ == "__main__":
    main()


