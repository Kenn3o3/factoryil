import os
import sys
import copy
import hydra
import torch
import wandb
import omegaconf
import numpy as np
import getpass as gt
from tqdm import tqdm
from glob import glob
import re
from torch.utils.data._utils.collate import default_collate
import time

try:

    from hydra.core.hydra_config import HydraConfig
except Exception:
    HydraConfig = None


from .utils.misc import get_dataset, get_agent
from factoryil.utils.seed import seed_everything, seed_worker


def _numpy_to_tensor(x):
    if isinstance(x, dict):
        return {k: _numpy_to_tensor(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return type(x)(_numpy_to_tensor(v) for v in x)
    if isinstance(x, np.ndarray):
        return torch.tensor(x)
    return x


def safe_collate(batch):
    converted = [_numpy_to_tensor(sample) for sample in batch]
    return default_collate(converted)


def _natural_sort(xs):

    return sorted(
        xs,
        key=lambda s: [
            int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)
        ],
    )


def _episode_lengths_from_dir(data_path):
    pattern = os.path.join(data_path, "*")
    fns = sorted(glob(pattern))
    key_fn = lambda x: "_".join(os.path.basename(x).split("_")[:-1])
    ep_len = {}
    for fn in fns:
        ep = key_fn(fn)
        ep_len[ep] = ep_len.get(ep, 0) + 1
    return ep_len


def _required_state_key_for_agent(agent_name: str):

    return "eef_pose_w"


def _check_dataset_agent_compat(train_dataset, agent_name: str):
    req = _required_state_key_for_agent(agent_name)
    try:
        probe = train_dataset[0]
        has_req = req in probe
        has_action = "action" in probe
        if not has_req:
            raise RuntimeError(
                f"Dataset sample does not contain required state key '{req}' for agent '{agent_name}'. "
                f"Available keys in sample: {list(probe.keys())}. "
                f"Make sure your converted per-frame NPZ contains '{req}' "
                f"(FactoryIL uses `factoryil.tools.convert_to_npz`)."
            )
        if not has_action:
            raise RuntimeError("Dataset sample is missing 'action'.")
    except Exception as e:
        raise RuntimeError(f"Dataset/Agent compatibility check failed: {e}") from e


@hydra.main(config_path="configs", config_name="dp_pc", version_base=None)
def main(cfg):
    assert cfg.mode == "train"
    # Deterministic training (best-effort): seed Python/NumPy/Torch (+ CUDA).
    seed_everything(int(cfg.seed), deterministic=True)

    batch_size = cfg.training.batch_size
    print("batch_size: ", batch_size)

    if cfg.use_wandb:
        wandb_config = omegaconf.OmegaConf.to_container(
            cfg, resolve=True, throw_on_missing=False
        )
        wandb.init(
            entity=cfg.wandb.entity,
            project=cfg.wandb.project,
            tags=["train"],
            name=cfg.prefix,
            settings=wandb.Settings(code_dir="."),
            config=wandb_config,
        )

    log_dir = None
    if HydraConfig is not None:
        try:
            if HydraConfig.initialized():
                log_dir = HydraConfig.get().runtime.output_dir
        except Exception:
            log_dir = None
    if not log_dir:
        log_dir = os.getcwd()
    os.makedirs(log_dir, exist_ok=True)

    ep_len_all = _episode_lengths_from_dir(cfg.data.dataset.path)
    min_demo_len = cfg.data.dataset.min_demo_length
    valid_eps = [ep for ep, L in ep_len_all.items() if L >= min_demo_len]
    if len(valid_eps) == 0:
        raise RuntimeError(
            f"No episodes satisfy min_demo_length={min_demo_len}. "
            f"Found episodes: {len(ep_len_all)}"
        )
    valid_eps_sorted = _natural_sort(valid_eps)
    custom = omegaconf.OmegaConf.select(cfg, "data.custom_split", default=False)

    if custom:
        train_spec = omegaconf.OmegaConf.select(
            cfg, "data.train_episodes", default=None
        )
        test_spec = omegaconf.OmegaConf.select(cfg, "data.test_episodes", default=None)

        def resolve(spec):
            if spec is None:
                return []
            seq = list(spec)

            if all(
                isinstance(x, (int, np.integer)) or (isinstance(x, str) and x.isdigit())
                for x in seq
            ):
                idxs = [int(x) for x in seq]
                names = []
                N = len(valid_eps_sorted)
                for i in idxs:
                    if not (-(N) <= i < N):
                        raise ValueError(
                            f"Episode index {i} out of range for {N} valid episodes"
                        )
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
                "data.custom_split is True but neither data.train_episodes nor data.test_episodes were provided."
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
        f"[train.py] Episode split: {len(train_eps)} train episodes, {len(test_eps)} test episodes "
        f"(from {len(valid_eps)} valid episodes)."
    )
    print("training episodes selected: ", train_eps)
    print("testing episodes selected: ", test_eps)

    train_log_path = os.path.join(log_dir, "train.log")
    with open(train_log_path, "a") as f:
        f.write(f"training episodes selected:  {train_eps}\n")
        f.write(f"testing episodes selected:  {test_eps}\n")

    train_cfg = copy.deepcopy(cfg)
    test_cfg = copy.deepcopy(cfg)
    train_cfg.data.dataset.episode_names = train_eps
    test_cfg.data.dataset.episode_names = test_eps

    train_dataset = get_dataset(train_cfg, "train")
    test_dataset = get_dataset(test_cfg, "test")

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

    cfg.data.dataset.num_training_steps = (
        cfg.training.num_epochs * len(train_dataset) // batch_size
    )

    agent = get_agent(cfg.agent.agent_name)(cfg)
    if cfg.training.ckpt is not None:
        agent.load_snapshot(cfg.training.ckpt)
        start_epoch_ix = int(cfg.training.ckpt.split("/")[-1].split(".")[0][4:])
    else:
        start_epoch_ix = 0

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
    best_test_loss = float("inf")
    best_epoch_ix = -1
    CHECK_TOPK_EVERY = int(
        omegaconf.OmegaConf.select(cfg, "training.check_topk_every", default=20)
    )
    TOP_K_BEST = 10
    topk_best = []
    topk_files = {}
    for epoch_ix in tqdm(range(start_epoch_ix, cfg.training.num_epochs)):

        batch_ix = 0
        running_train_loss = 0.0
        running_train_count = 0
        for batch in tqdm(train_loader, leave=False, desc="Train Batches"):
            train_metrics = agent.update(batch)
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
                        "train/" + k: (v.item() if hasattr(v, "item") else v)
                        for k, v in train_metrics.items()
                    },
                    step=global_step,
                )
                wandb.log({"epoch": epoch_ix}, step=global_step)
            del train_metrics
            global_step += 1
            batch_ix += 1

        train_epoch_loss = running_train_loss / max(1, running_train_count)

        test_running = {
            "loss": 0.0,
            "mean_gt_noise_norm": 0.0,
            "mean_pred_noise_norm": 0.0,
        }
        test_count = 0
        for batch in tqdm(test_loader, leave=False, desc="Test Batches"):
            with torch.no_grad():
                metrics = agent.evaluate(batch)
            bs = batch["action"].shape[0]
            test_running["loss"] += metrics["loss"] * bs
            test_running["mean_gt_noise_norm"] += metrics["mean_gt_noise_norm"] * bs
            test_running["mean_pred_noise_norm"] += metrics["mean_pred_noise_norm"] * bs
            test_count += bs

        test_metrics = {k: (v / max(1, test_count)) for k, v in test_running.items()}

        if cfg.use_wandb:
            wandb.log(
                {
                    "train/epoch_loss": train_epoch_loss,
                    "test/loss": test_metrics["loss"],
                    "test/mean_gt_noise_norm": test_metrics["mean_gt_noise_norm"],
                    "test/mean_pred_noise_norm": test_metrics["mean_pred_noise_norm"],
                    "epoch": epoch_ix,
                },
                step=global_step,
            )

        current_test_loss = float(test_metrics["loss"])
        is_topk_interval = (epoch_ix - start_epoch_ix + 1) % CHECK_TOPK_EVERY == 0

        if is_topk_interval:

            topk_best.append((current_test_loss, epoch_ix))
            topk_best.sort(key=lambda t: t[0])
            topk_best = topk_best[:TOP_K_BEST]

            current_epochs = {ep for _, ep in topk_best}

            for ep, path in list(topk_files.items()):
                if ep not in current_epochs:
                    try:
                        os.remove(path)
                        print(
                            f"[train.py] Dropped from top-{TOP_K_BEST}: epoch {ep}; removed {path}"
                        )
                    except Exception:
                        pass
                    topk_files.pop(ep, None)

            for rank, (loss_val, ep) in enumerate(topk_best, start=1):
                expected_path = os.path.join(log_dir, f"top_{rank}_at_epoch_{ep}.pth")
                old_path = topk_files.get(ep)
                if old_path is None:

                    agent.save_snapshot(expected_path)
                    topk_files[ep] = expected_path
                    print(
                        f"[train.py] Saved top-{rank} checkpoint at epoch {ep}: {expected_path} (loss={loss_val:.6f})"
                    )
                elif old_path != expected_path:

                    try:
                        os.replace(old_path, expected_path)
                    except FileNotFoundError:
                        agent.save_snapshot(expected_path)
                    topk_files[ep] = expected_path
                    print(
                        f"[train.py] Updated rank for epoch {ep}: now top-{rank} -> {expected_path}"
                    )

        if is_topk_interval and (current_test_loss < best_test_loss):
            best_test_loss = current_test_loss
            best_epoch_ix = epoch_ix
            best_ckpt_path = os.path.join(log_dir, "ckpt_best.pth")
            agent.save_snapshot(best_ckpt_path)
            print(
                f"[train.py] New best test loss {best_test_loss:.6f} at epoch {best_epoch_ix}. Saved: {best_ckpt_path}"
            )
            if cfg.use_wandb:
                wandb.run.summary["best_test/loss"] = best_test_loss
                wandb.run.summary["best_test/epoch"] = best_epoch_ix

        if (
            epoch_ix % cfg.training.save_interval == 0
            or epoch_ix == cfg.training.num_epochs - 1
        ):
            save_path = os.path.join(log_dir, f"ckpt{epoch_ix:05d}.pth")
            num_ckpt_to_keep = 10
            numbered_ckpts = sorted(glob(os.path.join(log_dir, "ckpt[0-9]*.pth")))
            if len(numbered_ckpts) > num_ckpt_to_keep:

                for fn in numbered_ckpts[:-num_ckpt_to_keep]:
                    os.remove(fn)
            agent.save_snapshot(save_path)


if __name__ == "__main__":
    main()
