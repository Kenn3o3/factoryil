import numpy as np
import torch
from torch import nn
import torch.nn.functional as F

from ..utils.norm import Normalizer
from ..utils.misc import to_torch
from .dp_policy import DPPolicy
from ..utils.diffusion.lr_scheduler import get_scheduler

class DPAgent(object):
    def __init__(self, cfg):
        print(f"Initializing DP agent.")
        self.cfg = cfg
        self._init_actor()
        if cfg.mode == "train":
            # 优化器与学习率调度器
            self.optimizer = torch.optim.AdamW(
                self.actor.nets.parameters(),
                lr=cfg.training.lr,
                weight_decay=cfg.training.weight_decay,
            )
            self.lr_scheduler = get_scheduler(
                name="cosine",
                optimizer=self.optimizer,
                num_warmup_steps=500,
                num_training_steps=cfg.data.dataset.num_training_steps,
            )
        self.device = cfg.device
        self.num_eef = cfg.env.num_eef
        self.dof = cfg.env.dof
        self.num_points = cfg.data.dataset.num_points
        self.obs_mode = cfg.model.obs_mode
        self.ac_mode = cfg.model.ac_mode
        self.obs_horizon = cfg.model.obs_horizon
        self.pred_horizon = cfg.model.pred_horizon
        self.ac_horizon = cfg.model.ac_horizon
        self.shuffle_pc = cfg.data.dataset.shuffle_pc
        
        # 归一化器（点云/状态/动作），延迟初始化
        self.pc_normalizer = None
        self.state_normalizer = None
        self.ac_normalizer = None

        # 重要：使用 actor 解析得到的 rgb_keys，避免 Agent 与 Policy 不一致
        # 若 actor 未设置，回退到数据集的单视角 key
        self.rgb_input_size = getattr(cfg.model, "rgb_input_size", None)
        self.rgb_keys = getattr(self.actor, "rgb_keys", [])
        if self.obs_mode == "rgb" and not self.rgb_keys:
            single = getattr(cfg.data.dataset, "rgb_key", "rgb_zed")
            self.rgb_keys = [single]

    def _init_actor(self):
        # 初始化策略网络，并将 EMA 模型也移到 device 上
        self.actor = DPPolicy(self.cfg, device=self.cfg.device).to(self.cfg.device)
        self.actor.ema.averaged_model.to(self.cfg.device)

    def _init_normalizers(self, batch):
        # 从 batch 初始化各归一化器（仅初始化一次）
        if self.obs_mode.startswith("pc") and self.pc_normalizer is None:
            flattened_pc = batch["pc"].view(-1, 3)
            self.pc_normalizer = Normalizer(flattened_pc)
            self.actor.pc_normalizer = self.pc_normalizer
            print(f"PC normalization stats: {self.pc_normalizer.stats}")
        if self.state_normalizer is None:
            state = batch["eef_pose_w"]
            flattened_state = state.view(-1, state.shape[-1])
            self.state_normalizer = Normalizer(flattened_state)
            self.actor.state_normalizer = self.state_normalizer
            print(f"State normalization stats: {self.state_normalizer.stats}")
        if self.ac_normalizer is None:
            gt_action = batch["action"]
            flattened_gt_action = gt_action.view(-1, gt_action.shape[-1])
            self.ac_normalizer = Normalizer(flattened_gt_action)
            print(f"Action normalization stats: {self.ac_normalizer.stats}")

    def train(self, training=True):
        # 切换 actor 的训练/评估模式（只对包含参数的 nets 生效）
        self.actor.nets.train(training)

    def act(self, obs, return_dict=False, debug=False):
        self.train(False)
        has_batch_dim = True
        if len(obs["state"].shape) == 3:
            # print("obs['state']: ", obs["state"])
            # add batch dimension
            has_batch_dim = False
            obs["state"] = obs["state"][:, None]
            if self.obs_mode.startswith("pc"):
                obs["pc"] = [[x] for x in obs["pc"]]
            elif self.obs_mode == "rgb":
                # 多视角：逐视角补 batch 维
                if isinstance(obs["rgb"], dict):
                    for k in self.rgb_keys:
                        v = obs["rgb"][k]
                        assert v.ndim == 4, "RGB per-view must be [Ho, H, W, 3] at inference"
                        obs["rgb"][k] = v[:, None]  # [Ho, 1, H, W, 3]
                else:
                    # 兼容单视角：包装成 dict，key 为 "__single__"
                    v = obs["rgb"]
                    assert v.ndim == 4, "RGB must be [Ho, H, W, 3] when not using dict"
                    obs["rgb"] = {"__single__": v[:, None]}  # CHANGED: wrap single view as dict
                    self.rgb_keys = ["__single__"]
        elif len(obs["state"].shape) == 4:
            has_batch_dim = True
        else:
            raise ValueError("Input state format not recognized.")

        ac_dim = self.num_eef * self.dof
        batch_size = obs["state"].shape[1]
        state = obs["state"].reshape(tuple(obs["state"].shape[:2]) + (-1,))  # [obs_h, B, eef_dim*num_eef]

        if self.obs_mode.startswith("pc"):
            # process PCs similar to existing code
            xyzs = []
            ac = np.zeros([batch_size, self.pred_horizon, ac_dim])
            if return_dict:
                ac_dict = [None for _ in range(batch_size)]
            forward_idxs = list(np.arange(batch_size))
            for pcs in obs["pc"]:
                xyzs.append([])
                for batch_idx, xyz in enumerate(pcs):
                    if not batch_idx in forward_idxs:
                        xyzs[-1].append(np.zeros((self.num_points, 3)))
                    elif xyz.shape[0] == 0:
                        forward_idxs.remove(batch_idx)
                        xyzs[-1].append(np.zeros((self.num_points, 3)))
                    elif self.shuffle_pc:
                        choice = np.random.choice(xyz.shape[0], self.num_points, replace=True)
                        xyz = xyz[choice, :]
                        xyzs[-1].append(xyz)
                    else:
                        step = max(1, xyz.shape[0] // self.num_points)
                        xyz = xyz[::step, :][: self.num_points]
                        xyzs[-1].append(xyz)

            if len(forward_idxs) > 0:
                torch_obs = dict(
                    pc=torch.tensor(np.array(xyzs).swapaxes(0, 1)[forward_idxs]).to(self.device).float(),
                    state=torch.tensor(state.swapaxes(0, 1)[forward_idxs]).to(self.device).float(),
                )
                # pass through policy
                raw_ac_dict = self.actor(torch_obs, debug=debug)
            else:
                raw_ac_dict = {"ac": torch.zeros((batch_size, self.actor.pred_horizon, self.actor.action_dim)).to(self.actor.device)}

            # unnormalize
            out_ac = np.zeros([batch_size, self.pred_horizon, ac_dim])
            for i in range(batch_size):
                unnormed_action = (
                    self.ac_normalizer.unnormalize(raw_ac_dict["ac"][i]).detach().cpu().numpy()
                )
                out_ac[i] = unnormed_action

        else:  # rgb
            # 构造各视角 [B, Ho, H, W, 3] 的 float32 输入，并可选 resize
            rgb_dict = {}
            for k in self.rgb_keys:
                v = torch.tensor(obs["rgb"][k].swapaxes(0, 1)).to(self.device)  # [B, Ho, H, W, 3] uint8
                v = v.float() / 255.0
                if self.rgb_input_size is not None:
                    B, Ho, H, W, C = v.shape
                    flat = v.reshape(B * Ho, H, W, C).permute(0, 3, 1, 2)
                    flat = F.interpolate(flat, size=tuple(self.rgb_input_size), mode="bilinear", align_corners=False)
                    v = flat.permute(0, 2, 3, 1).reshape(B, Ho, *tuple(self.rgb_input_size), C)
                rgb_dict[k] = v

            torch_obs = dict(
                rgb=rgb_dict,  # CHANGED: pass dict of views
                state=torch.tensor(state.swapaxes(0, 1)).to(self.device).float(),
            )
            raw_ac_dict = self.actor(torch_obs, debug=debug)

            out_ac = self.ac_normalizer.unnormalize(raw_ac_dict["ac"]).detach().cpu().numpy()
        
        # 若原输入是单条（无 batch 维），推理输出去掉 batch 维
        if not has_batch_dim:
            out_ac = out_ac[0]
            if return_dict:
                raw_ac_dict = {k: v[0] for k, v in raw_ac_dict.items()}
        # print("act output: ", out_ac)
        if return_dict:
            return out_ac, raw_ac_dict
        else:
            return out_ac

    def update(self, batch, training=True):
        self.train(training)

        batch = to_torch(batch, self.device)
        batch["eef_pose_w"] = batch["eef_pose_w"].reshape(
            tuple(batch["eef_pose_w"].shape[:2]) + (-1,)
        )
        state = batch["eef_pose_w"]
        gt_action = batch["action"]

        if self.state_normalizer is None or self.ac_normalizer is None:
            self._init_normalizers(batch)

        if self.obs_mode.startswith("pc"):
            pc = batch["pc"]
            if self.pc_normalizer is None:
                flattened_pc = pc.view(-1, 3)
                self.pc_normalizer = Normalizer(flattened_pc)
                self.actor.pc_normalizer = self.pc_normalizer
            pc = self.pc_normalizer.normalize(pc)
        elif self.obs_mode == "rgb":
            # 多视角字典，逐视角归一化并可选 resize，得到 {k: [B, Ho, H, W, 3] float}
            rgb_dict = {}
            rgb_in = batch["rgb"]
            assert isinstance(rgb_in, dict), "Expected dict-of-views for RGB batch"
            for k in self.rgb_keys:
                v = rgb_in[k].float() / 255.0  # [B, Ho, H, W, 3]
                if self.rgb_input_size is not None:
                    B, Ho, H, W, C = v.shape
                    flat = v.reshape(B * Ho, H, W, C).permute(0, 3, 1, 2)  # [B*Ho, 3, H, W]
                    flat = F.interpolate(flat, size=tuple(self.rgb_input_size), mode="bilinear", align_corners=False)
                    v = flat.permute(0, 2, 3, 1).reshape(B, Ho, *tuple(self.rgb_input_size), C)
                rgb_dict[k] = v

        state = self.state_normalizer.normalize(state)
        gt_action = self.ac_normalizer.normalize(gt_action)

        batch_size = gt_action.shape[0]

        # build conditioning vector z

        if self.obs_mode == "state":
            z = state
        elif self.obs_mode.startswith("pc"):
            pc_shape = pc.shape  # [B, obs_h, N, 3]
            flattened_pc = pc.reshape(batch_size * self.obs_horizon, *pc_shape[-2:])
            if self.cfg.model.use_torch_compile:
                enc = self.actor.encoder_handle(flattened_pc.permute(0, 2, 1))["global"]
            else:
                enc = self.actor.encoder(flattened_pc.permute(0, 2, 1))["global"]
            z = enc.reshape(batch_size, self.obs_horizon, -1)
            z = torch.cat([z, state], dim=-1)
        elif self.obs_mode == "rgb":
            # 多视角：逐视角编码，再做均值池化融合
            B, Ho = batch_size, self.obs_horizon
            feats_per_view = []
            for k in self.rgb_keys:
                x = rgb_dict[k]  # [B, Ho, H, W, 3]
                H, W = x.shape[-3], x.shape[-2]
                flat = x.reshape(B * Ho, H, W, 3).permute(0, 3, 1, 2)  # [B*Ho, 3, H, W]
                if self.cfg.model.use_torch_compile and hasattr(self.actor, "encoder_handles"):
                    enc = self.actor.encoder_handles[k](flat)
                else:
                    enc = self.actor.encoders[k](flat)
                feats_per_view.append(enc)  # [B*Ho, 512]
            fused = torch.stack(feats_per_view, dim=0).mean(dim=0)  # [B*Ho, 512]
            z = fused.reshape(B, Ho, -1)
            z = torch.cat([z, state], dim=-1)
        else:
            raise ValueError(f"Unsupported obs_mode: {self.obs_mode}")
        
        # 展平时间维得到全局条件 obs_cond：[B, Ho*obs_dim]
        obs_cond = z.reshape(batch_size, -1)  # (BS, obs_horizion * obs_dim)

        with torch.set_grad_enabled(training):

            noise = torch.randn(gt_action.shape, device=self.device)

            timesteps = torch.randint(
                0,
                self.actor.noise_scheduler.config.num_train_timesteps,
                (batch_size,),
                device=self.device,
            ).long()

            noisy_actions = self.actor.noise_scheduler.add_noise(
                gt_action, noise, timesteps
            )

            if self.cfg.model.use_torch_compile:
                noise_pred = self.actor.noise_pred_net_handle(
                    noisy_actions, timesteps, global_cond=obs_cond
                )
            else:
                noise_pred = self.actor.noise_pred_net(
                    noisy_actions, timesteps, global_cond=obs_cond
                )
            loss = nn.functional.mse_loss(noise_pred, noise)

            if training:

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.lr_scheduler.step()

                # make sure gradients are complete
                if self.obs_mode == "state":
                    grads = [k.grad for k in self.actor.noise_pred_net.parameters()]
                else:
                    grads = self.actor.nets.parameters()
                assert np.array([g is not None for g in grads]).all()

                self.actor.step_ema()

        metrics = {
            "loss": loss,
            "mean_gt_noise_norm": np.linalg.norm(
                noise.reshape(gt_action.shape[0], -1).detach().cpu().numpy(), axis=1
            ).mean(),
            "mean_pred_noise_norm": np.linalg.norm(
                noise_pred.reshape(gt_action.shape[0], -1).detach().cpu().numpy(),
                axis=1,
            ).mean(),
        }
        return metrics

    def evaluate(self, batch):
        """Compute denoising (training) loss on a batch without gradient or updates."""
        self.train(False)
        with torch.no_grad():
            if self.state_normalizer is None or self.ac_normalizer is None:
                raise RuntimeError(
                    "Normalizers are not initialized. Run one training step on the train set "
                    "before calling evaluate(), or initialize from a train batch."
                )
            if self.obs_mode.startswith("pc") and self.pc_normalizer is None:
                raise RuntimeError(
                    "PC normalizer is not initialized. Initialize from a train batch before evaluation."
                )
            batch = to_torch(batch, self.device)
            batch["eef_pose_w"] = batch["eef_pose_w"].reshape(
                tuple(batch["eef_pose_w"].shape[:2]) + (-1,)
            )
            state = batch["eef_pose_w"]
            gt_action = batch["action"]

            if self.obs_mode.startswith("pc"):
                pc = self.pc_normalizer.normalize(batch["pc"])
            elif self.obs_mode == "rgb":
                # CHANGED: multi-view handling and optional resize
                rgb_in = batch["rgb"]
                assert isinstance(rgb_in, dict)
                rgb_dict = {}
                for k in self.rgb_keys:
                    v = rgb_in[k].float() / 255.0
                    if self.rgb_input_size is not None:
                        B, Ho, H, W, C = v.shape
                        flat = v.reshape(B * Ho, H, W, C).permute(0, 3, 1, 2)
                        flat = F.interpolate(flat, size=tuple(self.rgb_input_size), mode="bilinear", align_corners=False)
                        v = flat.permute(0, 2, 3, 1).reshape(B, Ho, *tuple(self.rgb_input_size), C)
                    rgb_dict[k] = v

            state = self.state_normalizer.normalize(state)
            gt_action = self.ac_normalizer.normalize(gt_action)

            batch_size = gt_action.shape[0]

            # build conditioning vector z
            if self.obs_mode == "state":
                z = state
            elif self.obs_mode.startswith("pc"):
                pc_shape = pc.shape
                flattened_pc = pc.reshape(batch_size * self.obs_horizon, *pc_shape[-2:])
                enc = self.actor.encoder(flattened_pc.permute(0, 2, 1))["global"]
                z = enc.reshape(batch_size, self.obs_horizon, -1)
                z = torch.cat([z, state], dim=-1)
            elif self.obs_mode == "rgb":
                # CHANGED: per-view encoding (non-EMA) for eval parity with training
                B, Ho = batch_size, self.obs_horizon
                feats_per_view = []
                for k in self.rgb_keys:
                    x = rgb_dict[k]
                    H, W = x.shape[-3], x.shape[-2]
                    flat = x.reshape(B * Ho, H, W, 3).permute(0, 3, 1, 2)
                    enc = self.actor.encoders[k](flat)
                    feats_per_view.append(enc)
                fused = torch.stack(feats_per_view, dim=0).mean(dim=0)
                z = fused.reshape(B, Ho, -1)
                z = torch.cat([z, state], dim=-1)
            else:
                raise ValueError(f"Unsupported obs_mode: {self.obs_mode}")

            obs_cond = z.reshape(batch_size, -1)  # (BS, obs_horizon * obs_dim)

            noise = torch.randn(gt_action.shape, device=self.device)
            timesteps = torch.randint(
                0,
                self.actor.noise_scheduler.config.num_train_timesteps,
                (batch_size,),
                device=self.device,
            ).long()
            noisy_actions = self.actor.noise_scheduler.add_noise(gt_action, noise, timesteps)

            noise_pred = self.actor.noise_pred_net(noisy_actions, timesteps, global_cond=obs_cond)
            loss = nn.functional.mse_loss(noise_pred, noise)

            metrics = {
                "loss": float(loss.detach().cpu().item()),
                "mean_gt_noise_norm": float(
                    np.linalg.norm(
                        noise.reshape(gt_action.shape[0], -1).detach().cpu().numpy(), axis=1
                    ).mean()
                ),
                "mean_pred_noise_norm": float(
                    np.linalg.norm(
                        noise_pred.reshape(gt_action.shape[0], -1).detach().cpu().numpy(), axis=1
                    ).mean()
                ),
            }
            return metrics

    def save_snapshot(self, save_path):
        def maybe_state_dict(norm):
            return None if norm is None else norm.state_dict()
        state_dict = dict(
            actor=self.actor.state_dict(),
            ema_model=self.actor.ema.averaged_model.state_dict(),
            pc_normalizer=maybe_state_dict(self.pc_normalizer),
            state_normalizer=maybe_state_dict(self.state_normalizer),
            ac_normalizer=maybe_state_dict(self.ac_normalizer),
        )
        torch.save(state_dict, save_path)

    def _fix_state_dict_keys(self, state_dict):
        return {k: v for k, v in state_dict.items() if not "handle" in k}

    def load_snapshot(self, save_path):

        state_dict = torch.load(save_path)
        self.state_normalizer = Normalizer(state_dict["state_normalizer"])
        self.actor.state_normalizer = self.state_normalizer
        self.ac_normalizer = Normalizer(state_dict["ac_normalizer"])
        if self.obs_mode.startswith("pc"):
            self.pc_normalizer = Normalizer(state_dict["pc_normalizer"])
            self.actor.pc_normalizer = self.pc_normalizer
        # clean any compiled handles on actor before loading fresh
        if hasattr(self.actor, "encoder_handle"):
            del self.actor.encoder_handle
        if hasattr(self.actor, "encoder_handles"):
            del self.actor.encoder_handles
        if hasattr(self.actor, "noise_pred_net_handle"):
            del self.actor.noise_pred_net_handle

        self.actor.load_state_dict(self._fix_state_dict_keys(state_dict["actor"]))
        self.actor._init_torch_compile()
        self.actor.ema.averaged_model.load_state_dict(state_dict["ema_model"])

        # 确保 agent 使用与 actor 一致的 rgb_keys
        self.rgb_keys = getattr(self.actor, "rgb_keys", self.rgb_keys)