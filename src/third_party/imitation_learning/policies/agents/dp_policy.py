import copy
import hydra
import torch
from torch import nn
import torch.nn.functional as F

from ..vision.pointnet_encoder import PointNetEncoder
from ..utils.diffusion.ema_model import EMAModel
from ..utils.diffusion.conditional_unet1d import ConditionalUnet1D
from ..utils.diffusion.resnet_with_gn import get_resnet, replace_bn_with_gn


class DPPolicy(nn.Module):
    def __init__(self, cfg, device="cpu"):
        super().__init__()
        self.cfg = cfg
        self.hidden_dim = hidden_dim = cfg.model.hidden_dim
        self.obs_mode = cfg.model.obs_mode
        self.device = device

        # |o|o|                             observations: 2
        # | |a|a|a|a|a|a|a|a|               actions executed: 8
        # |p|p|p|p|p|p|p|p|p|p|p|p|p|p|p|p| actions predicted: 16
        self.pred_horizon = cfg.model.pred_horizon
        self.obs_horizon = cfg.model.obs_horizon
        self.action_horizon = cfg.model.ac_horizon

        if hasattr(cfg.model, "num_diffusion_iters"):
            self.num_diffusion_iters = cfg.model.num_diffusion_iters
        else:
            self.num_diffusion_iters = cfg.model.noise_scheduler.num_train_timesteps

        self.num_eef = cfg.env.num_eef
        self.eef_dim = cfg.env.eef_dim
        self.dof = cfg.env.dof

        # CHANGED: 解析 RGB 视角 keys 的优先级：
        # 1) cfg.model.rgb_keys -> 2) cfg.data.dataset.rgb_keys -> 3) cfg.data.dataset.rgb_key（单视角回退）
        if self.obs_mode == "rgb":
            rgb_keys_model = list(getattr(cfg.model, "rgb_keys", []))
            if len(rgb_keys_model) > 0:
                self.rgb_keys = rgb_keys_model
            else:
                rgb_keys_ds = list(getattr(cfg.data.dataset, "rgb_keys", []))
                if len(rgb_keys_ds) > 0:
                    self.rgb_keys = rgb_keys_ds
                else:
                    single = getattr(cfg.data.dataset, "rgb_key", "rgb_zed")
                    self.rgb_keys = [single]
        else:
            self.rgb_keys = []

        if cfg.model.obs_mode == "state":
            self.obs_dim = self.num_eef * self.eef_dim
        elif cfg.model.obs_mode == "rgb":
            # 多视角经编码器再“均值池化融合”后得到 512 维视觉特征，再与 state 拼接
            self.obs_dim = 512 + self.num_eef * self.eef_dim
        else:
            self.obs_dim = hidden_dim + self.num_eef * self.eef_dim
        self.action_dim = self.dof * cfg.env.num_eef

        if self.obs_mode.startswith("pc"):
            self.encoder = PointNetEncoder(
                h_dim=hidden_dim,
                c_dim=hidden_dim,
                num_layers=cfg.model.encoder.backbone_args.num_layers,
            )
        elif self.obs_mode == "rgb":
            # 每个视角一个 ResNet18，并将 BN 替换为 GroupNorm（更稳健的小 batch 训练）
            self.encoders = nn.ModuleDict({
                k: replace_bn_with_gn(get_resnet("resnet18")) for k in self.rgb_keys
            })
        else:
            self.encoder = nn.Identity()

        # 条件一维 U-Net：输入为动作序列（pred_horizon, action_dim）
        # 条件为展开后的观测（Ho*obs_dim）
        self.noise_pred_net = ConditionalUnet1D(
            input_dim=self.action_dim,
            diffusion_step_embed_dim=self.obs_dim * self.obs_horizon,
            global_cond_dim=self.obs_dim * self.obs_horizon,
        )

        # CHANGED: register nets for EMA differently for PC vs RGB
        if self.obs_mode == "rgb":
            self.nets = nn.ModuleDict(
                {"encoders": self.encoders, "noise_pred_net": self.noise_pred_net}
            )
        else:
            self.nets = nn.ModuleDict(
                {"encoder": self.encoder, "noise_pred_net": self.noise_pred_net}
            )

        self.ema = EMAModel(model=copy.deepcopy(self.nets), power=0.75)

        self._init_torch_compile()

        self.noise_scheduler = hydra.utils.instantiate(cfg.model.noise_scheduler)

        num_parameters = sum(p.numel() for p in self.parameters() if p.requires_grad)
        print(f"Initialized DP Policy with {num_parameters} parameters")

    def _init_torch_compile(self):
        if self.cfg.model.use_torch_compile:
            # 多视角时为每个视角单独编译编码器，避免共享引起的图不匹配
            if self.obs_mode == "rgb":
                self.encoder_handles = nn.ModuleDict({
                    k: torch.compile(enc) for k, enc in self.encoders.items()
                })
            else:
                self.encoder_handle = torch.compile(self.encoder)
            self.noise_pred_net_handle = torch.compile(self.noise_pred_net)

    def forward(self, obs, predict_action=True, debug=False):
        state = obs["state"]
        state = self.state_normalizer.normalize(state)

        ema_nets = self.ema.averaged_model

        if self.obs_mode == "state":
            z = state
        elif self.obs_mode.startswith("pc"):
            pc = obs["pc"]
            pc = self.pc_normalizer.normalize(pc)
            pc_shape = pc.shape
            batch_size = pc.shape[0]
            flattened_pc = pc.reshape(batch_size * self.obs_horizon, *pc_shape[-2:])
            z = ema_nets["encoder"](flattened_pc.permute(0, 2, 1))["global"]
            z = z.reshape(batch_size, self.obs_horizon, -1)
            z = torch.cat([z, state], dim=-1)
        elif self.obs_mode == "rgb":
            # 多视角 RGB：
            # - obs["rgb"] 是 {key: [B, Ho, H, W, 3]} 的字典
            # - 逐视角用对应的 EMA 编码器提取 [B*Ho, 512]，再按视角做均值池化融合
            rgb = obs["rgb"]
            feats_per_view = []
            if isinstance(rgb, dict):
                # use first view to infer B and Ho
                first_k = self.rgb_keys[0]
                B, Ho = rgb[first_k].shape[0], rgb[first_k].shape[1]
                ema_encoders = ema_nets["encoders"]
                for k in self.rgb_keys:
                    x = rgb[k]  # [B, Ho, H, W, 3], float in [0,1]
                    H, W = x.shape[-3], x.shape[-2]
                    flat = x.reshape(B * Ho, H, W, 3).permute(0, 3, 1, 2)
                    # 若输入尺寸与目标不同，这里可再次保险 resize（通常在 Agent 已处理）
                    target = getattr(self.cfg.model, "rgb_input_size", None)
                    if target is not None and flat.shape[-2:] != tuple(target):
                        flat = F.interpolate(flat, size=tuple(target), mode="bilinear", align_corners=False)
                    feat = ema_encoders[k](flat)  # [B*Ho, 512]
                    feats_per_view.append(feat)
                fused = torch.stack(feats_per_view, dim=0).mean(dim=0)  # [B*Ho, 512]
                z_img = fused.reshape(B, Ho, -1)
            else:
                # 兼容 fallback：将可能的视角维并入 Ho，逐视角取用
                if rgb.ndim == 5:
                    rgb = rgb.unsqueeze(2)  # -> [B, Ho, 1, H, W, 3]
                B, Ho, V, H, W, C = rgb.shape
                ema_encoders = ema_nets["encoders"]
                for vi, k in enumerate(self.rgb_keys):
                    x = rgb[:, :, vi]  # [B, Ho, H, W, 3]
                    flat = x.reshape(B * Ho, H, W, C).permute(0, 3, 1, 2)
                    target = getattr(self.cfg.model, "rgb_input_size", None)
                    if target is not None and flat.shape[-2:] != tuple(target):
                        flat = F.interpolate(flat, size=tuple(target), mode="bilinear", align_corners=False)
                    feat = ema_encoders[k](flat)
                    feats_per_view.append(feat)
                fused = torch.stack(feats_per_view, dim=0).mean(dim=0)
                z_img = fused.reshape(B, Ho, -1)

            z = torch.cat([z_img, state], dim=-1)
        else:
            raise ValueError(f"Unsupported obs_mode: {self.obs_mode}")

        obs_cond = z.reshape(z.shape[0], -1)  # (BS, obs_horizon * obs_dim)

        initial_noise_scale = 0.0 if debug else 1.0
        noisy_action = (
            torch.randn((z.shape[0], self.pred_horizon, self.action_dim)).to(
                self.device
            )
            * initial_noise_scale
        )
        curr_action = noisy_action
        self.noise_scheduler.set_timesteps(self.num_diffusion_iters)

        for k in self.noise_scheduler.timesteps:
            # predict noise
            noise_pred = ema_nets["noise_pred_net"](
                sample=curr_action, timestep=k, global_cond=obs_cond
            )

            # inverse diffusion step
            curr_action = self.noise_scheduler.step(
                model_output=noise_pred, timestep=k, sample=curr_action
            ).prev_sample

        ret = dict(ac=curr_action)
        return ret

    def step_ema(self):
        self.ema.step(self.nets)