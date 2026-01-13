import os
import glob
import time
import numpy as np
from tqdm import tqdm
from collections import defaultdict
from torch.utils.data import Dataset


class BaseDataset(Dataset):
    def __init__(self, cfg, mode) -> None:
        super().__init__()

        data_root = cfg.get("path", None)
        if not data_root:
            raise ValueError(
                "Dataset path is not set. Provide it via Hydra, e.g. "
                "`data_path=/path/to/training_data` so cfg.data.dataset.path points to a directory "
                "of per-frame .npz files (created by `factoryil.tools.convert_to_npz`)."
            )
        self.data_root = os.path.abspath(os.path.expanduser(str(data_root)))
        self.data_dir = os.path.join(self.data_root, "*.npz")
        self.file_names = sorted(glob.glob(self.data_dir))
        if not self.file_names:
            raise FileNotFoundError(f"No .npz files found under: {self.data_root!r}")

        self.mode = mode
        self.dof = cfg["dof"]
        self.num_eef = cfg["num_eef"]
        self.eef_dim = cfg["eef_dim"]
        self.num_points = cfg["num_points"]
        self.shuffle_pc = cfg["shuffle_pc"]
        self.min_demo_length = cfg["min_demo_length"]

        self.obs_horizon = cfg["obs_horizon"]
        self.pred_horizon = cfg["pred_horizon"]

        self.obs_mode = cfg.get("obs_mode", "pc")
        print("Dataset obs_mode:", self.obs_mode)
        assert self.obs_mode in ["pc", "rgb"], "obs_mode must be 'pc' or 'rgb'"

        rgb_keys_cfg = cfg.get("rgb_keys", None)
        if self.obs_mode == "rgb":
            if rgb_keys_cfg is None:
                single_rgb_key = cfg.get("rgb_key", "rgb_zed")
                self.rgb_keys = [single_rgb_key]
            else:
                self.rgb_keys = list(rgb_keys_cfg)
        else:

            if rgb_keys_cfg is None:
                self.rgb_keys = []
            else:
                self.rgb_keys = list(rgb_keys_cfg)

        self.cache_rgb = cfg.get("cache_rgb", True)

        self.precache = cfg.get("precache", True)

        episode_names = cfg.get("episode_names", None)
        print(f"Dataset Mode: {self.mode}, episodes: {episode_names}")
        if episode_names is not None:
            key_fn = lambda x: "_".join(os.path.basename(x).split("_")[:-1])
            before_count = len(self.file_names)
            allowed = set(episode_names)
            self.file_names = [f for f in self.file_names if key_fn(f) in allowed]
            print(
                f"[dataset.py] Episode filtering: {len(allowed)} episodes -> "
                f"{len(self.file_names)} frames kept (from {before_count})."
            )
            if len(self.file_names) == 0:
                raise FileNotFoundError(
                    f"No frames remain after episode filtering. "
                    f"data_root={self.data_root!r}, episode_names={list(allowed)!r}"
                )

        num_demos = cfg.get("num_demos", None)
        if num_demos is not None:
            key_fn = lambda x: "_".join(os.path.basename(x).split("_")[:-1])
            ep_list = list(sorted(set([key_fn(fn) for fn in self.file_names])))
            if int(num_demos) < len(ep_list):
                print(f"[dataset.py] Filtering demos to {int(num_demos)} demo(s)")
                filtered_eps = set(ep_list[: int(num_demos)])
                self.file_names = [
                    f for f in self.file_names if key_fn(f) in filtered_eps
                ]
                if len(self.file_names) == 0:
                    raise FileNotFoundError(
                        f"No frames remain after num_demos filtering. "
                        f"data_root={self.data_root!r}, num_demos={num_demos!r}"
                    )
        else:
            print("[dataset.py] Using all demos")

        ep_length_dict = defaultdict(lambda: 0)
        key_fn = lambda x: "_".join(os.path.basename(x).split("_")[:-1])
        for fn in self.file_names:
            ep_length_dict[key_fn(fn)] += 1
        self.ep_length_dict = ep_length_dict

        self.file_names = [
            fn
            for fn in self.file_names
            if ep_length_dict[key_fn(fn)] >= self.min_demo_length
        ]
        ep_length_dict = {
            k: v for k, v in ep_length_dict.items() if v >= self.min_demo_length
        }

        if len(self.file_names) == 0:
            raise FileNotFoundError(
                f"No episodes have length >= min_demo_length={self.min_demo_length}. "
                f"data_root={self.data_root!r}"
            )

        if len(self.file_names[0].split("_")[-1].split(".")[0][1:]) == 4:
            self.use_four_digit_time = True
        else:
            self.use_four_digit_time = False

        if self.precache:
            self._init_cache()
        else:
            self.cache = dict()

    def __len__(self):
        return len(self.file_names)

    def __getitem__(self, idx):
        fn = self.file_names[idx]
        key_fn = lambda x: "_".join(x.split("/")[-1].split("_")[:-1])
        ep_t = int(fn.split("_")[-1][1:-4])
        start_t = ep_t - (self.obs_horizon - 1)
        end_t = ep_t + self.pred_horizon
        ep_t_list = np.arange(start_t, end_t)
        clipped_ep_t_list = np.clip(ep_t_list, 0, self.ep_length_dict[key_fn(fn)] - 1)

        ret = dict(eef_pose_w=[], eef_pos=[], action=[])
        if self.obs_mode.startswith("pc"):
            ret["pc"] = []
            if len(self.rgb_keys) > 0:
                ret["rgb"] = {k: [] for k in self.rgb_keys}
        else:
            ret["rgb"] = {k: [] for k in self.rgb_keys}
        for t, clipped_t in zip(ep_t_list, clipped_ep_t_list):

            if self.use_four_digit_time:
                fn_t = "_".join(fn.split("_")[:-1] + [f"t{clipped_t:04d}.npz"])
            else:
                fn_t = "_".join(fn.split("_")[:-1] + [f"t{clipped_t:02d}.npz"])

            if t < ep_t:
                keys = ["eef_pose_w"]
                if self.obs_mode == "pc":
                    keys.append("pc")

                    if len(self.rgb_keys) > 0:
                        keys.append("rgb")
                elif self.obs_mode == "rgb":
                    keys.append("rgb")
            elif t == ep_t:
                keys = ["action", "eef_pose_w"]
                if self.obs_mode == "pc":
                    keys.append("pc")
                    if len(self.rgb_keys) > 0:
                        keys.append("rgb")
                elif self.obs_mode == "rgb":
                    keys.append("rgb")
            else:
                keys = ["action"]
            data_t = self._process_data_from_file(fn_t, keys)

            if t >= ep_t:
                ret["action"].append(data_t["action"])

            if t < ep_t or t == ep_t:

                if "eef_pos" in data_t:
                    ret["eef_pos"].append(data_t["eef_pos"])

                if "eef_pose_w" in data_t:
                    ret["eef_pose_w"].append(data_t["eef_pose_w"])
                if self.obs_mode.startswith("pc") and "pc" in data_t:
                    ret["pc"].append(data_t["pc"])

                if "rgb" in data_t and "rgb" in ret:
                    for k in self.rgb_keys:
                        ret["rgb"][k].append(data_t["rgb"][k])

        if len(ret["eef_pos"]) > 0:
            ret["eef_pos"] = np.array(ret["eef_pos"])
        if len(ret["eef_pose_w"]) > 0:
            ret["eef_pose_w"] = np.array(ret["eef_pose_w"])
        if len(ret["action"]) > 0:
            ret["action"] = np.array(ret["action"])
        if self.obs_mode.startswith("pc"):
            ret["pc"] = np.array(ret["pc"])
        if "rgb" in ret:
            for k in self.rgb_keys:
                ret["rgb"][k] = np.array(ret["rgb"][k])

        assert len(ret["action"]) == self.pred_horizon

        if (
            "eef_pos" in ret
            and isinstance(ret["eef_pos"], np.ndarray)
            and ret["eef_pos"].ndim > 0
        ):
            assert len(ret["eef_pos"]) == self.obs_horizon
        if (
            "eef_pose_w" in ret
            and isinstance(ret["eef_pose_w"], np.ndarray)
            and ret["eef_pose_w"].ndim > 0
        ):
            assert len(ret["eef_pose_w"]) == self.obs_horizon
        if "pc" in ret and isinstance(ret["pc"], np.ndarray) and ret["pc"].ndim > 0:
            assert len(ret["pc"]) == self.obs_horizon
        if "rgb" in ret:
            for k in self.rgb_keys:
                assert k in ret["rgb"], f"Expected view key {k} in returned rgb dict"
                assert len(ret["rgb"][k]) == self.obs_horizon, (
                    f"Expected {self.obs_horizon} frames for view {k}, "
                    f"got {len(ret['rgb'][k])}"
                )

        return ret

    def _init_cache(self):

        self.cache = dict()

        keys_to_keep = ["eef_pose_w", "action"]
        if self.obs_mode.startswith("pc"):
            keys_to_keep.append("pc")
        if self.obs_mode == "rgb" and self.cache_rgb:
            keys_to_keep.extend(self.rgb_keys)

        for fn in tqdm(self.file_names, desc="Building dataset cache"):
            with np.load(fn) as data:
                self.cache[fn] = dict()

                if "eef_pos" in data.files:
                    self.cache[fn]["eef_pos"] = data["eef_pos"].astype(np.float32)
                if "eef_pose_w" in data.files:
                    self.cache[fn]["eef_pose_w"] = data["eef_pose_w"].astype(np.float32)

                self.cache[fn]["action"] = data["action"].astype(np.float32)

                if "pc" in keys_to_keep and "pc" in data.files:
                    self.cache[fn]["pc"] = data["pc"].astype(np.float32)
                if self.obs_mode == "rgb" and self.cache_rgb:
                    for k in self.rgb_keys:
                        if k in data.files:
                            self.cache[fn][k] = data[k]

    def _process_data_from_file(self, fn, keys):
        entry = self.cache.get(fn, {})
        file_data = None

        def ensure_file():
            nonlocal file_data
            if file_data is None:
                file_data = np.load(fn)
            return file_data

        ret = {}

        if "eef_pos" in keys:
            if "eef_pos" in entry:
                eef_pos = entry["eef_pos"].astype(np.float32)
            else:
                fd = ensure_file()
                if "eef_pos" not in fd.files:

                    eef_pos = None
                else:
                    eef_pos = fd["eef_pos"].astype(np.float32)
            if eef_pos is not None:
                eef_pos = eef_pos.reshape(self.num_eef, -1)[:, : self.eef_dim]
                ret["eef_pos"] = eef_pos

        if "eef_pose_w" in keys:
            if "eef_pose_w" in entry:
                eef6 = entry["eef_pose_w"].astype(np.float32)
            else:
                fd = ensure_file()
                if "eef_pose_w" not in fd.files:
                    eef6 = None
                else:
                    eef6 = fd["eef_pose_w"].astype(np.float32)
            if eef6 is not None:

                eef6 = eef6.reshape(self.num_eef, -1)
                ret["eef_pose_w"] = eef6

        if "action" in keys:
            if "action" in entry:
                action = entry["action"].astype(np.float32)
            else:
                fd = ensure_file()
                if "action" not in fd.files:
                    raise KeyError(f"Missing 'action' in NPZ '{fn}'.")
                action = fd["action"].astype(np.float32)
            ret["action"] = action.flatten().astype(np.float32)

        if "pc" in keys:
            if "pc" in entry:
                xyz = entry["pc"].astype(np.float32)
            else:
                fd = ensure_file()
                if "pc" not in fd.files:
                    raise KeyError(
                        f"Missing 'pc' in NPZ '{fn}'. "
                        f"Re-collect demos with point clouds enabled (FactoryIL runner: --save_pc) "
                        f"and re-run `factoryil.tools.convert_to_npz`."
                    )
                xyz = fd["pc"].astype(np.float32)

            N = xyz.shape[0]
            K = self.num_points

            if N == 0:

                ret["pc"] = xyz.astype(np.float32)
            else:
                if self.mode == "train" and self.shuffle_pc:

                    if N >= K:

                        choice = np.random.choice(N, K, replace=False)
                    else:

                        choice = np.random.choice(N, K, replace=True)
                    xyz = xyz[choice, :]
                else:

                    if N > K:
                        step = max(1, N // K)
                        xyz = xyz[::step, :][:K, :]
                    elif N < K:

                        choice = np.random.choice(N, K, replace=True)
                        xyz = xyz[choice, :]

                ret["pc"] = xyz.astype(np.float32)

        if "rgb" in keys:

            rgb_dict = {}
            for k in self.rgb_keys:
                if k in entry:
                    rgb = entry[k]
                else:
                    fd = ensure_file()

                    rgb = fd[k]
                rgb_dict[k] = rgb
            ret["rgb"] = rgb_dict

        if file_data is not None:
            file_data.close()

        return ret
