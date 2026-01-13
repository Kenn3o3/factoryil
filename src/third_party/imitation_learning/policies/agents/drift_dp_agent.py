import copy
from typing import Dict, Tuple, Optional, List

import numpy as np
import torch
from torch import nn
import torch.nn.functional as F

from .dp_agent import DPAgent
from ..utils.diffusion.lr_scheduler import get_scheduler
from ..utils.diffusion.positional_embedding import SinusoidalPosEmb
from ..utils.misc import to_torch
from ..utils.norm import Normalizer
from ..utils.se3 import relative_axis_angle, compose_axis_angles

class RFMResidual(nn.Module):
    """
    Rectified-flow residual head operating in residual space R^6 with
    time embedding and generic conditioning vector c \\in R^C.

    v_theta: (r_s, s, c) -> R^6
    """

    def __init__(
        self,
        residual_dim: int,
        cond_dim: int,
        time_emb_dim: int = 64,
        hidden_dim: int = 256,
        num_layers: int = 4,
    ) -> None:
        super().__init__()
        self.residual_dim = residual_dim
        self.cond_dim = cond_dim

        self.time_mlp = nn.Sequential(
            SinusoidalPosEmb(time_emb_dim),
            nn.Linear(time_emb_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
        )

        in_dim = residual_dim + hidden_dim + cond_dim
        layers: List[nn.Module] = []
        for i in range(num_layers):
            layers.append(nn.Linear(in_dim if i == 0 else hidden_dim, hidden_dim))
            layers.append(nn.SiLU())
        self.net = nn.Sequential(*layers)
        self.out = nn.Linear(hidden_dim, residual_dim)

    def forward(
        self,
        r_s: torch.Tensor,
        times: torch.Tensor,
        cond: torch.Tensor,
    ) -> torch.Tensor:
        """
        r_s:   [B, H, 6]
        times: [B, H]  in [0,1]
        cond:  [B, H, C]
        """
        B, H, D = r_s.shape
        assert D == self.residual_dim, f"Expected residual_dim={self.residual_dim}, got {D}"
        assert cond.shape[0] == B and cond.shape[1] == H

        r_flat = r_s.reshape(B * H, D)
        t_flat = times.reshape(B * H)
        c_flat = cond.reshape(B * H, -1)

        t_emb = self.time_mlp(t_flat)
        x = torch.cat([r_flat, t_emb, c_flat], dim=-1)
        h = self.net(x)
        out = self.out(h)
        return out.reshape(B, H, D)


class DriftDPAgent(DPAgent):
    """
    DRIFT-DP agent:
    - Coarse module: inherited Diffusion Policy (DPAgent / DPPolicy) operating
      on visuo-proprio inputs in the dataset's conventions.
    - RFM module: residual rectified-flow head that refines only the first 6
      action dimensions (SE(3) motion) in the same conventions.

    This class keeps the public `act` interface identical to DPAgent so that
    FactoryIL/il_infer can swap configs by changing `agent.agent_name`.
    """

    def __init__(self, cfg) -> None:
        super().__init__(cfg)

        self.rfm_enabled: bool = False  # toggled on once RFM is trained / loaded

        # RFM configuration (with sensible defaults if not present in cfg)
        self.rfm_hidden_dim: int = int(getattr(cfg.model, "rfm_hidden_dim", 256))
        self.rfm_time_emb_dim: int = int(getattr(cfg.model, "rfm_time_emb_dim", 64))
        self.rfm_feat_dim: int = int(getattr(cfg.model, "rfm_feat_dim", 128))

        # Whether to use tactile images as additional conditioning for RFM.
        # This is the key switch for the visuotactile DRIFT-DP design in METHOD.md:
        # - Coarse head can remain purely point-cloud based (obs_mode="pc").
        # - RFM can still condition on tactile RGB images via a separate encoder.
        self.rfm_use_tactile: bool = bool(
            getattr(cfg.model, "rfm_use_tactile", False)
        )
        # Tactile view keys expected in batch["rgb"] when rfm_use_tactile is True
        # (e.g., ["rgb_tactile_left", "rgb_tactile_right"]).
        self.rfm_tactile_keys: List[str] = list(
            getattr(
                getattr(cfg, "model", cfg),
                "rfm_tactile_keys",
                ["rgb_tactile_left", "rgb_tactile_right"],
            )
        )

        if self.obs_mode.startswith("pc"):
            # Base cond parts: pc, eef_pose_w, coarse_action_horizon
            num_parts = 3
            # Optionally append tactile_static and tactile_dynamic parts when available.
            if self.rfm_use_tactile:
                num_parts += 2
        elif self.obs_mode == "rgb":
            # cond parts: visual, eef_pose_w, coarse_action_horizon,
            #             tactile_static, tactile_dynamic
            num_parts = 5
        else:
            raise ValueError(f"Unsupported obs_mode for DriftDPAgent: {self.obs_mode}")

        self.rfm_cond_dim: int = num_parts * self.rfm_feat_dim

        # Projections from various feature sources into a shared cond feature space.
        self.rfm_pc_proj: Optional[nn.Module] = None
        self.rfm_vis_proj: Optional[nn.Module] = None
        self.rfm_state_proj = nn.Linear(
            self.obs_horizon * self.num_eef * self.cfg.env.eef_dim, self.rfm_feat_dim
        )
        # coarse actions: use 6 DoF per EEF over the prediction horizon
        self.rfm_action_proj = nn.Linear(
            self.pred_horizon * self.num_eef * 6, self.rfm_feat_dim
        )

        if self.obs_mode.startswith("pc"):
            # Canonical point-cloud encoder features from DPPolicy (vn_pointnet)
            self.rfm_pc_proj = nn.Linear(self.cfg.model.hidden_dim, self.rfm_feat_dim)
        elif self.obs_mode == "rgb":
            # RGB visual encoder output is 512-d per frame (ResNet18 without fc)
            self.rfm_vis_proj = nn.Linear(512, self.rfm_feat_dim)
            # Tactile static / dynamic features each projected separately
            self.rfm_tactile_static_proj = nn.Linear(512, self.rfm_feat_dim)
            self.rfm_tactile_dynamic_proj = nn.Linear(512, self.rfm_feat_dim)

        # For obs_mode="pc" with tactile enabled, we instantiate a dedicated
        # ResNet18 encoder for tactile RGB inputs so that:
        # - The coarse DP head stays purely point-cloud based.
        # - The RFM residual head still receives rich visuotactile conditioning,
        #   as required by DRIFT-DP.
        if self.obs_mode.startswith("pc") and self.rfm_use_tactile:
            try:
                import torchvision.models as tv_models  # type: ignore
            except ImportError as exc:  # pragma: no cover - dependency error surfaced at runtime
                raise ImportError(
                    "torchvision is required for tactile-conditioned RFM "
                    "(rfm_use_tactile=True) but is not installed."
                ) from exc

            resnet = tv_models.resnet18(weights=None)
            # Drop the classification head; keep convolutional trunk.
            self.rfm_tactile_encoder = nn.Sequential(*list(resnet.children())[:-1])
            # ResNet18 trunk outputs [B, 512, 1, 1] → flatten to 512
            self.rfm_tactile_static_proj = nn.Linear(512, self.rfm_feat_dim)
            self.rfm_tactile_dynamic_proj = nn.Linear(512, self.rfm_feat_dim)

        # RFM residual network
        self.rfm = RFMResidual(
            residual_dim=6,
            cond_dim=self.rfm_cond_dim,
            time_emb_dim=self.rfm_time_emb_dim,
            hidden_dim=self.rfm_hidden_dim,
            num_layers=4,
        )

        # Group all RFM trainable modules (core + projections) for device handling & optimization
        self.rfm_modules = nn.ModuleDict(
            {
                "core": self.rfm,
                "state_proj": self.rfm_state_proj,
                "action_proj": self.rfm_action_proj,
            }
        )
        if self.rfm_pc_proj is not None:
            self.rfm_modules["pc_proj"] = self.rfm_pc_proj
        if self.rfm_vis_proj is not None:
            self.rfm_modules["vis_proj"] = self.rfm_vis_proj
        if hasattr(self, "rfm_tactile_encoder"):
            self.rfm_modules["tactile_encoder"] = self.rfm_tactile_encoder  # type: ignore[attr-defined]
        if hasattr(self, "rfm_tactile_static_proj"):
            self.rfm_modules["tactile_static_proj"] = self.rfm_tactile_static_proj
        if hasattr(self, "rfm_tactile_dynamic_proj"):
            self.rfm_modules["tactile_dynamic_proj"] = self.rfm_tactile_dynamic_proj

        self.rfm_modules.to(self.device)

        self.rfm_optimizer: Optional[torch.optim.Optimizer] = None
        self.rfm_lr_scheduler = None

    # ------------------------------------------------------------------
    # Coarse DP training / evaluation (reuse DPAgent logic)
    # ------------------------------------------------------------------
    def update_coarse(self, batch, training: bool = True) -> Dict[str, torch.Tensor]:
        """
        Wrapper around DPAgent.update (coarse-only). This keeps the DP training
        path unchanged so existing configs remain valid.
        """
        return super().update(batch, training=training)

    def evaluate_coarse(self, batch) -> Dict[str, float]:
        """
        Wrapper around DPAgent.evaluate with an extra action-space metric in
        action space (L2 between denoised coarse actions and GT actions, first
        6 dims only).

        When cfg.training.fast_eval is True, we skip the extra forward pass
        needed for coarse_action_l2 and only return the base DP metrics to
        speed up validation.
        """
        metrics = super().evaluate(batch)  # noise loss + norms

        # Optional fast-eval mode (avoid extra forward for coarse_action_l2).
        training_cfg = getattr(self.cfg, "training", None)
        fast_eval = (
            bool(getattr(training_cfg, "fast_eval", False))
            if training_cfg is not None
            else False
        )
        if fast_eval:
            return metrics

        try:
            with torch.no_grad():
                l2 = float(self._coarse_action_l2(batch).item())
        except Exception:
            l2 = float("nan")
        metrics["coarse_action_l2"] = l2
        return metrics

    def _coarse_action_l2(self, batch) -> torch.Tensor:
        """
        Compute L2 between coarse predicted actions and GT actions (first 6 dims
        only, averaged over batch and horizon).
        """
        if self.state_normalizer is None or self.ac_normalizer is None:
            raise RuntimeError(
                "Normalizers are not initialized; run at least one coarse "
                "training step or load a coarse checkpoint before calling "
                "_coarse_action_l2."
            )

        # Clone to avoid in-place modifications leaking back to caller
        batch_t = copy.deepcopy(batch)
        batch_t = to_torch(batch_t, self.device)

        B = batch_t["action"].shape[0]
        batch_t["eef_pose_w"] = batch_t["eef_pose_w"].reshape(
            tuple(batch_t["eef_pose_w"].shape[:2]) + (-1,)
        )
        state = batch_t["eef_pose_w"]  # [B, Ho, num_eef*eef_dim]
        gt_action = batch_t["action"]  # [B, Hpred, dof]

        # Build obs dict expected by DPPolicy.forward (un-normalized; policy
        # applies its own normalizers)
        if self.obs_mode.startswith("pc"):
            pc = batch_t["pc"]  # [B, Ho, N, 3]
            obs = dict(state=state, pc=pc)
        elif self.obs_mode == "rgb":
            rgb_in = batch_t["rgb"]
            assert isinstance(rgb_in, dict)
            rgb_dict = {}
            for k in self.rgb_keys:
                v = rgb_in[k].float() / 255.0  # [B, Ho, H, W, 3]
                rgb_dict[k] = v
            obs = dict(state=state, rgb=rgb_dict)
        else:
            raise ValueError(f"Unsupported obs_mode for DriftDPAgent: {self.obs_mode}")

        with torch.no_grad():
            coarse_out = self.actor(obs, predict_action=True, debug=False)
            # unnormalize actions back to physical units
            coarse_norm = coarse_out["ac"]  # [B, Hpred, action_dim]
            coarse = self.ac_normalizer.unnormalize(coarse_norm)

        # Compare only the SE(3) motion dims (first 6 per EEF)
        dims_se3 = 6 * self.num_eef
        gt6 = gt_action[..., :dims_se3]
        coarse6 = coarse[..., :dims_se3]
        return F.mse_loss(coarse6, gt6)

    # ------------------------------------------------------------------
    # RFM optimizer & parameter freezing
    # ------------------------------------------------------------------
    def configure_rfm_optim(self, num_training_steps: int) -> None:
        """
        Initialize optimizer + LR scheduler for RFM-only training.
        """
        self.rfm_optimizer = torch.optim.AdamW(
            self.rfm_modules.parameters(),
            lr=self.cfg.training.lr,
            weight_decay=self.cfg.training.weight_decay,
        )
        self.rfm_lr_scheduler = get_scheduler(
            name="cosine",
            optimizer=self.rfm_optimizer,
            num_warmup_steps=500,
            num_training_steps=num_training_steps,
        )

    def freeze_coarse(self) -> None:
        """
        Freeze coarse DP parameters (for RFM-only training).
        """
        for p in self.actor.nets.parameters():
            p.requires_grad = False

    def unfreeze_coarse(self) -> None:
        """
        Unfreeze coarse DP parameters (optional Phase 3).
        """
        for p in self.actor.nets.parameters():
            p.requires_grad = True

    # ------------------------------------------------------------------
    # RFM training / evaluation
    # ------------------------------------------------------------------
    def _ensure_normalizers(self, batch) -> None:
        """
        Ensure PC / state / action normalizers exist (may be loaded from a
        coarse checkpoint or initialized from a batch).
        """
        batch_t = to_torch(batch, self.device)
        batch_t["eef_pose_w"] = batch_t["eef_pose_w"].reshape(
            tuple(batch_t["eef_pose_w"].shape[:2]) + (-1,)
        )

        # Reuse DPAgent logic for initializing from data if needed
        if self.state_normalizer is None or self.ac_normalizer is None:
            self._init_normalizers(batch_t)
        if self.obs_mode.startswith("pc") and self.pc_normalizer is None:
            pc = batch_t["pc"]
            flattened_pc = pc.view(-1, 3)
            self.pc_normalizer = Normalizer(flattened_pc)
            self.actor.pc_normalizer = self.pc_normalizer

    def _build_rfm_cond_from_batch(
        self,
        batch_t: Dict[str, torch.Tensor],
        coarse_actions: torch.Tensor,
    ) -> torch.Tensor:
        """
        Construct conditioning tensor c_{k+j} for RFM training.

        batch_t: dict on device, with shapes:
            - eef_pose_w: [B, Ho, num_eef*eef_dim]
            - pc (when obs_mode=='pc'): [B, Ho, N, 3]
            - rgb (when obs_mode=='rgb'): dict of [B, Ho, H, W, 3]
        coarse_actions: [B, Hpred, action_dim] in physical units (dataset conventions).

        Returns:
            cond: [B, Hpred, C]
        """
        B = batch_t["action"].shape[0]
        state = batch_t["eef_pose_w"]  # [B, Ho, num_eef*eef_dim]

        # EEF pose features: flatten over time and project
        state_flat = state.reshape(B, -1)
        state_feat = self.rfm_state_proj(state_flat)  # [B, F]

        # Coarse action context: use only SE(3) dims and flatten over horizon
        dims_se3 = 6 * self.num_eef
        coarse6 = coarse_actions[..., :dims_se3]  # [B, Hpred, 6*num_eef]
        action_flat = coarse6.reshape(B, -1)
        action_feat = self.rfm_action_proj(action_flat)  # [B, F]

        feats: List[torch.Tensor] = []

        if self.obs_mode.startswith("pc"):
            assert self.rfm_pc_proj is not None
            pc = batch_t["pc"]  # [B, Ho, N, 3]
            pc_shape = pc.shape
            flattened_pc = pc.reshape(B * self.obs_horizon, *pc_shape[-2:])
            # Encode point clouds using the same backbone as coarse DP.
            if self.cfg.model.use_torch_compile and hasattr(
                self.actor, "encoder_handle"
            ):
                enc = self.actor.encoder_handle(flattened_pc.permute(0, 2, 1))[
                    "global"
                ]
            else:
                enc = self.actor.encoder(flattened_pc.permute(0, 2, 1))["global"]
            pc_enc = enc.reshape(B, self.obs_horizon, -1)  # [B, Ho, hidden_dim]
            pc_global = pc_enc.mean(dim=1)  # [B, hidden_dim]
            pc_feat = self.rfm_pc_proj(pc_global)  # [B, F]
            feats.extend([pc_feat, state_feat, action_feat])

            # Optional tactile conditioning for RFM when coarse head is PC-only.
            if self.rfm_use_tactile:
                if "rgb" not in batch_t:
                    raise RuntimeError(
                        "RFM tactile conditioning is enabled (rfm_use_tactile=True) "
                        "but batch does not contain 'rgb'. Ensure the dataset "
                        "provides tactile RGB keys and that they are listed in "
                        "cfg.model.rfm_tactile_keys."
                    )
                assert hasattr(
                    self, "rfm_tactile_encoder"
                ), "rfm_tactile_encoder is not initialized."
                rgb_in = batch_t["rgb"]
                assert isinstance(
                    rgb_in, dict
                ), "Expected dict batch['rgb'] when using tactile conditioning."

                tact_feats: List[torch.Tensor] = []
                for k in self.rfm_tactile_keys:
                    if k not in rgb_in:
                        raise KeyError(
                            f"Tactile key '{k}' not found in batch['rgb']. "
                            f"Available keys: {list(rgb_in.keys())}"
                        )
                    x = rgb_in[k].float() / 255.0  # [B, Ho, H, W, 3]
                    H_img, W_img = x.shape[-3], x.shape[-2]
                    flat = x.reshape(B * self.obs_horizon, H_img, W_img, 3).permute(
                        0, 3, 1, 2
                    )  # [B*Ho, 3, H, W]
                    enc = self.rfm_tactile_encoder(flat)  # [B*Ho, 512, 1, 1]
                    enc = enc.view(enc.shape[0], -1)  # [B*Ho, 512]
                    tact_feats.append(enc)

                if len(tact_feats) > 0:
                    tact_fused = torch.stack(tact_feats, dim=0).mean(
                        dim=0
                    )  # [B*Ho, 512]
                    tact_seq = tact_fused.reshape(
                        B, self.obs_horizon, -1
                    )  # [B, Ho, 512]
                    # Static embedding: average over time.
                    static_emb = tact_seq.mean(dim=1)  # [B, 512]
                    # Dynamic embedding: endpoint difference as proxy for drift/slip.
                    if self.obs_horizon >= 2:
                        dynamic_emb = tact_seq[:, -1] - tact_seq[:, 0]
                    else:
                        dynamic_emb = torch.zeros_like(static_emb)
                    tact_static_feat = self.rfm_tactile_static_proj(static_emb)
                    tact_dynamic_feat = self.rfm_tactile_dynamic_proj(dynamic_emb)
                else:
                    tact_static_feat = torch.zeros(
                        B, self.rfm_feat_dim, device=self.device, dtype=state.dtype
                    )
                    tact_dynamic_feat = torch.zeros_like(tact_static_feat)

                feats.extend([tact_static_feat, tact_dynamic_feat])
        elif self.obs_mode == "rgb":
            assert self.rfm_vis_proj is not None
            rgb_in = batch_t["rgb"]
            assert isinstance(rgb_in, dict)

            # Visual "cam" context (if present) – average over time.
            vis_feats: List[torch.Tensor] = []
            for k in self.rgb_keys:
                if not k.startswith("rgb_cam"):
                    continue
                x = rgb_in[k].float() / 255.0  # [B, Ho, H, W, 3]
                H, W = x.shape[-3], x.shape[-2]
                flat = x.reshape(B * self.obs_horizon, H, W, 3).permute(0, 3, 1, 2)
                if (
                    self.cfg.model.use_torch_compile
                    and hasattr(self.actor, "encoder_handles")
                ):
                    enc = self.actor.encoder_handles[k](flat)
                else:
                    enc = self.actor.encoders[k](flat)
                vis_feats.append(enc)  # [B*Ho, 512]
            if len(vis_feats) > 0:
                vis_fused = torch.stack(vis_feats, dim=0).mean(dim=0)
                vis_seq = vis_fused.reshape(B, self.obs_horizon, -1)  # [B, Ho, 512]
                vis_global = vis_seq.mean(dim=1)  # [B, 512]
                vis_feat = self.rfm_vis_proj(vis_global)  # [B, F]
            else:
                vis_feat = torch.zeros(
                    B, self.rfm_feat_dim, device=self.device, dtype=state.dtype
                )

            # Tactile static / dynamic features from tactile views if present.
            tact_feats: List[torch.Tensor] = []
            for k in self.rgb_keys:
                if not (k.startswith("rgb_tactile_left") or k.startswith("rgb_tactile_right")):
                    continue
                x = rgb_in[k].float() / 255.0  # [B, Ho, H, W, 3]
                H, W = x.shape[-3], x.shape[-2]
                flat = x.reshape(B * self.obs_horizon, H, W, 3).permute(0, 3, 1, 2)
                if (
                    self.cfg.model.use_torch_compile
                    and hasattr(self.actor, "encoder_handles")
                ):
                    enc = self.actor.encoder_handles[k](flat)
                else:
                    enc = self.actor.encoders[k](flat)
                tact_feats.append(enc)  # [B*Ho, 512]
            if len(tact_feats) > 0:
                tact_fused = torch.stack(tact_feats, dim=0).mean(dim=0)
                tact_seq = tact_fused.reshape(B, self.obs_horizon, -1)  # [B, Ho, 512]
                # Static: average early frames (or all if Ho is small).
                static_emb = tact_seq.mean(dim=1)
                # Dynamic: simple endpoint difference as a proxy for drift/slip.
                if self.obs_horizon >= 2:
                    dynamic_emb = tact_seq[:, -1] - tact_seq[:, 0]
                else:
                    dynamic_emb = torch.zeros_like(static_emb)
                tact_static_feat = self.rfm_tactile_static_proj(static_emb)
                tact_dynamic_feat = self.rfm_tactile_dynamic_proj(dynamic_emb)
            else:
                tact_static_feat = torch.zeros(
                    B, self.rfm_feat_dim, device=self.device, dtype=state.dtype
                )
                tact_dynamic_feat = torch.zeros_like(tact_static_feat)

            feats.extend(
                [vis_feat, state_feat, action_feat, tact_static_feat, tact_dynamic_feat]
            )
        else:
            raise ValueError(f"Unsupported obs_mode for DriftDPAgent: {self.obs_mode}")

        cond_per_sample = torch.cat(feats, dim=-1)  # [B, C]
        # Broadcast across prediction horizon so each step sees the same context.
        cond = cond_per_sample.unsqueeze(1).expand(-1, self.pred_horizon, -1).contiguous()
        return cond

    def update_rfm(self, batch, training: bool = True) -> Dict[str, torch.Tensor]:
        """
        Single RFM training step:
        - Requires a frozen coarse module with initialized normalizers.
        - Assumes actions / poses follow the same conventions used during collection.
        """
        assert (
            self.rfm is not None
        ), "RFM network is not initialized. Did you construct DriftDPAgent correctly?"
        if self.rfm_optimizer is None:
            raise RuntimeError(
                "RFM optimizer is not configured. Call configure_rfm_optim(...) "
                "before starting RFM training."
            )

        self.train(False)  # coarse nets in eval mode
        self.rfm_modules.train(training)

        self._ensure_normalizers(batch)
        batch_t = to_torch(batch, self.device)

        B = batch_t["action"].shape[0]
        batch_t["eef_pose_w"] = batch_t["eef_pose_w"].reshape(
            tuple(batch_t["eef_pose_w"].shape[:2]) + (-1,)
        )
        state = batch_t["eef_pose_w"]  # [B, Ho, num_eef*eef_dim]
        gt_action = batch_t["action"]  # [B, Hpred, dof]

        # Build obs for coarse DP forward.
        if self.obs_mode.startswith("pc"):
            pc = batch_t["pc"]
            obs = dict(state=state, pc=pc)
        elif self.obs_mode == "rgb":
            rgb_in = batch_t["rgb"]
            assert isinstance(rgb_in, dict)
            rgb_dict = {}
            for k in self.rgb_keys:
                v = rgb_in[k].float() / 255.0
                rgb_dict[k] = v
            obs = dict(state=state, rgb=rgb_dict)
        else:
            raise ValueError(f"Unsupported obs_mode for DriftDPAgent: {self.obs_mode}")

        # Coarse predictions (unnormalized actions).
        with torch.no_grad():
            coarse_out = self.actor(obs, predict_action=True, debug=False)
            coarse_norm = coarse_out["ac"]  # [B, Hpred, action_dim]
            coarse_actions = self.ac_normalizer.unnormalize(coarse_norm)

        # Residual targets r* (Eq. 8–10) for the first 6 dims (per EEF).
        dims_se3 = 6 * self.num_eef
        gt6 = gt_action[..., :dims_se3]
        coarse6 = coarse_actions[..., :dims_se3]

        # Translation residual
        pos_res = gt6[..., :3] - coarse6[..., :3]
        # Rotation residual via axis-angle composition on SO(3)
        rot_coarse = coarse6[..., 3:6]
        rot_gt = gt6[..., 3:6]
        rot_res = relative_axis_angle(rot_coarse, rot_gt)
        r_star = torch.cat([pos_res, rot_res], dim=-1)  # [B, Hpred, 6]

        # Sample s ~ Uniform[0,1] per (batch, horizon) and compute r_s = s * r*
        times = torch.rand(B, self.pred_horizon, device=self.device)
        r_s = times.unsqueeze(-1) * r_star

        # Conditioning c_{k+j}: PC / EEF / coarse-action (and tactile if RGB).
        cond = self._build_rfm_cond_from_batch(batch_t, coarse_actions)

        with torch.set_grad_enabled(training):
            r_pred = self.rfm(r_s, times, cond)  # [B, Hpred, 6]
            loss = F.mse_loss(r_pred, r_star)

            if training:
                assert self.rfm_optimizer is not None
                self.rfm_optimizer.zero_grad()
                loss.backward()
                self.rfm_optimizer.step()
                if self.rfm_lr_scheduler is not None:
                    self.rfm_lr_scheduler.step()

        # Optional refined action L2 metric for monitoring.
        with torch.no_grad():
            trans_refined = coarse6[..., :3] + r_pred[..., :3]
            rot_res_pred = r_pred[..., 3:6]
            rot_refined = compose_axis_angles(rot_coarse, rot_res_pred)
            refined6 = torch.cat([trans_refined, rot_refined], dim=-1)
            refined_l2 = F.mse_loss(refined6, gt6)

        metrics = {
            "rfm_residual_loss": loss,
            "refined_action_l2": refined_l2,
        }
        return metrics

    def evaluate_rfm(self, batch) -> Dict[str, float]:
        self.rfm_modules.eval()
        with torch.no_grad():
            metrics_t = self.update_rfm(batch, training=False)
        return {k: float(v.detach().cpu().item()) for k, v in metrics_t.items()}

    # ------------------------------------------------------------------
    # Checkpointing helpers
    # ------------------------------------------------------------------
    def _fix_state_dict_keys(self, state_dict):
        # reuse DPAgent helper to strip any compiled handles
        return {k: v for k, v in state_dict.items() if "handle" not in k}

    def _load_coarse_from_state(self, state_dict: Dict) -> None:
        def maybe_get(d, key, default=None):
            return d[key] if key in d else default

        actor_sd = maybe_get(state_dict, "actor")
        ema_sd = maybe_get(state_dict, "ema_model")
        pc_norm_sd = maybe_get(state_dict, "pc_normalizer")
        state_norm_sd = maybe_get(state_dict, "state_normalizer")
        ac_norm_sd = maybe_get(state_dict, "ac_normalizer")

        if state_norm_sd is not None:
            self.state_normalizer = Normalizer(state_norm_sd)
            self.actor.state_normalizer = self.state_normalizer
        if ac_norm_sd is not None:
            self.ac_normalizer = Normalizer(ac_norm_sd)
        if pc_norm_sd is not None and self.obs_mode.startswith("pc"):
            self.pc_normalizer = Normalizer(pc_norm_sd)
            self.actor.pc_normalizer = self.pc_normalizer

        # Clean any compiled handles on actor before loading fresh weights.
        if hasattr(self.actor, "encoder_handle"):
            del self.actor.encoder_handle
        if hasattr(self.actor, "encoder_handles"):
            del self.actor.encoder_handles
        if hasattr(self.actor, "noise_pred_net_handle"):
            del self.actor.noise_pred_net_handle

        if actor_sd is not None:
            self.actor.load_state_dict(self._fix_state_dict_keys(actor_sd))
            self.actor._init_torch_compile()
        if ema_sd is not None:
            self.actor.ema.averaged_model.load_state_dict(ema_sd)

        # Ensure rgb_keys is consistent with actor (for RGB agents)
        self.rgb_keys = getattr(self.actor, "rgb_keys", self.rgb_keys)

    def save_snapshot(self, save_path: str) -> None:
        def maybe_state_dict(norm):
            return None if norm is None else norm.state_dict()

        state = dict(
            coarse=dict(
                actor=self.actor.state_dict(),
                ema_model=self.actor.ema.averaged_model.state_dict(),
                pc_normalizer=maybe_state_dict(self.pc_normalizer),
                state_normalizer=maybe_state_dict(self.state_normalizer),
                ac_normalizer=maybe_state_dict(self.ac_normalizer),
            ),
            rfm=dict(
                model=self.rfm_modules.state_dict(),
            ),
            meta=dict(
                version="drift_dp_v1",
            ),
        )
        torch.save(state, save_path)

    def load_snapshot(self, save_path: str) -> None:
        """
        Load a DRIFT-DP checkpoint. If the file is a legacy DP-only snapshot,
        it is interpreted as coarse-only and RFM is left untouched.
        """
        state = torch.load(save_path, map_location=self.device)
        if "coarse" in state or "rfm" in state:
            if "coarse" in state:
                self._load_coarse_from_state(state["coarse"])
            if "rfm" in state and "model" in state["rfm"]:
                try:
                    self.rfm_modules.load_state_dict(state["rfm"]["model"])
                except RuntimeError:
                    # Backward compatibility: old checkpoints only have the core RFM dict
                    print("[DriftDPAgent] Loading legacy RFM checkpoint (core only).")
                    self.rfm.load_state_dict(state["rfm"]["model"])
                self.rfm_enabled = True
        else:
            # Backwards compatibility: treat as DPAgent snapshot.
            self._load_coarse_from_state(state)
            # RFM remains uninitialized (coarse-only baseline).

    def load_coarse_state(self, save_path: str) -> None:
        """
        Load coarse DP weights + normalizers only from a checkpoint.
        This can be either a DPAgent snapshot or a DRIFT-DP snapshot.
        """
        state = torch.load(save_path, map_location=self.device)
        if "coarse" in state:
            self._load_coarse_from_state(state["coarse"])
        else:
            self._load_coarse_from_state(state)

    def load_rfm_state(self, save_path: str) -> None:
        """
        Load only the RFM residual head from a DRIFT-DP checkpoint.
        """
        state = torch.load(save_path, map_location=self.device)
        if "rfm" in state and "model" in state["rfm"]:
            try:
                self.rfm_modules.load_state_dict(state["rfm"]["model"])
            except RuntimeError:
                 # Backward compatibility
                print("[DriftDPAgent] Loading legacy RFM checkpoint (core only).")
                self.rfm.load_state_dict(state["rfm"]["model"])
            self.rfm_enabled = True

    # ------------------------------------------------------------------
    # Default update/evaluate dispatchers (coarse-only by default)
    # ------------------------------------------------------------------
    def update(self, batch, training: bool = True):
        """
        By default, keep compatibility with existing training scripts by
        delegating to coarse-only update(). DRIFT-DP training scripts should
        call update_coarse / update_rfm explicitly.
        """
        return self.update_coarse(batch, training=training)

    def evaluate(self, batch):
        """
        Default evaluation path: coarse-only. DRIFT-DP training scripts should
        call evaluate_coarse / evaluate_rfm explicitly.
        """
        return self.evaluate_coarse(batch)

    # ------------------------------------------------------------------
    # Inference: coarse DP + optional RFM refinement
    # ------------------------------------------------------------------
    def act(self, obs, return_dict: bool = False, debug: bool = False):
        """
        Inference interface matching DPAgent.act:
        - Inputs:
          - state: [Ho, num_eef, eef_dim] or [Ho, B, num_eef, eef_dim]
          - pc:    list length Ho, each (N,3), or tensor [Ho, B, N, 3]
          - rgb:   dict {view: [Ho, H, W, 3]} or {view: [Ho, B, H, W, 3]}
        - Outputs:
          - np.array actions [Hpred, E*dof] or [B, Hpred, E*dof]
          - If return_dict=True, also returns raw dict from DPPolicy.

        When self.rfm_enabled is True and an RFM head is trained/loaded, the
        first 6 action dims (per EEF) are refined via rectified-flow integration;
        otherwise this reduces to coarse DPAgent.act.
        """
        self.train(False)
        has_batch_dim = True
        if len(obs["state"].shape) == 3:
            # add batch dimension
            has_batch_dim = False
            obs["state"] = obs["state"][:, None]
            if self.obs_mode.startswith("pc"):
                obs["pc"] = [[x] for x in obs["pc"]]
            elif self.obs_mode == "rgb":
                # multi-view: add batch dim per view
                if isinstance(obs["rgb"], dict):
                    for k in self.rgb_keys:
                        v = obs["rgb"][k]
                        assert (
                            v.ndim == 4
                        ), "RGB per-view must be [Ho, H, W, 3] at inference"
                        obs["rgb"][k] = v[:, None]  # [Ho, 1, H, W, 3]
                else:
                    # single-view fallback: wrap as dict
                    v = obs["rgb"]
                    assert v.ndim == 4, "RGB must be [Ho, H, W, 3] when not using dict"
                    obs["rgb"] = {"__single__": v[:, None]}
                    self.rgb_keys = ["__single__"]
        elif len(obs["state"].shape) == 4:
            has_batch_dim = True
        else:
            raise ValueError("Input state format not recognized.")

        ac_dim = self.num_eef * self.dof
        batch_size = obs["state"].shape[1]
        state_np = obs["state"].reshape(
            tuple(obs["state"].shape[:2]) + (-1,)
        )  # [Ho, B, eef_dim*num_eef]

        # ------------------------------------------------------------------
        # Coarse DP inference (identical to DPAgent.act)
        # ------------------------------------------------------------------
        if self.obs_mode.startswith("pc"):
            # process PCs similar to existing code
            xyzs = []
            if return_dict:
                ac_dict = [None for _ in range(batch_size)]
            forward_idxs = list(np.arange(batch_size))
            for pcs in obs["pc"]:
                xyzs.append([])
                for batch_idx, xyz in enumerate(pcs):
                    if batch_idx not in forward_idxs:
                        xyzs[-1].append(np.zeros((self.num_points, 3)))
                    elif xyz.shape[0] == 0:
                        forward_idxs.remove(batch_idx)
                        xyzs[-1].append(np.zeros((self.num_points, 3)))
                    elif self.shuffle_pc:
                        choice = np.random.choice(
                            xyz.shape[0], self.num_points, replace=True
                        )
                        xyz = xyz[choice, :]
                        xyzs[-1].append(xyz)
                    else:
                        step = max(1, xyz.shape[0] // self.num_points)
                        xyz = xyz[::step, :][: self.num_points]
                        xyzs[-1].append(xyz)

            if len(forward_idxs) > 0:
                pcs_arr = np.array(xyzs).swapaxes(0, 1)[forward_idxs]
                state_arr = state_np.swapaxes(0, 1)[forward_idxs]
                torch_obs = dict(
                    pc=torch.tensor(pcs_arr).to(self.device).float(),
                    state=torch.tensor(state_arr).to(self.device).float(),
                )
                raw_ac_dict = self.actor(torch_obs, debug=debug)
            else:
                raw_ac_dict = {
                    "ac": torch.zeros(
                        (batch_size, self.actor.pred_horizon, self.actor.action_dim),
                        device=self.actor.device,
                    )
                }

            # unnormalize coarse actions
            out_ac = np.zeros([batch_size, self.pred_horizon, ac_dim], dtype=np.float32)
            for i in range(batch_size):
                unnormed_action = (
                    self.ac_normalizer.unnormalize(raw_ac_dict["ac"][i])
                    .detach()
                    .cpu()
                    .numpy()
                )
                out_ac[i] = unnormed_action

            # Optional RFM refinement for valid PCs only.
            if self.rfm_enabled and len(forward_idxs) > 0:
                with torch.no_grad():
                    coarse_t = self.ac_normalizer.unnormalize(raw_ac_dict["ac"]).to(
                        self.device
                    )  # [B_valid, Hpred, action_dim]
                    # Build a minimal batch-like dict for conditioning.
                    batch_like = {
                        "eef_pose_w": torch.tensor(state_arr, device=self.device).reshape(
                            len(forward_idxs), self.obs_horizon, -1
                        ),
                        "pc": torch.tensor(pcs_arr, device=self.device).float(),
                        "action": torch.zeros(
                            len(forward_idxs),
                            self.pred_horizon,
                            self.num_eef * self.dof,
                            device=self.device,
                        ),
                    }
                    # For PC-mode DRIFT-DP agents with tactile-conditioned RFM,
                    # optionally attach tactile RGB views so that
                    # _build_rfm_cond_from_batch can use them in the conditioning.
                    can_use_rfm = True
                    if self.rfm_use_tactile:
                        rgb_src = obs.get("rgb", None)
                        if isinstance(rgb_src, dict):
                            rgb_dict = {}
                            for k in self.rfm_tactile_keys:
                                if k not in rgb_src:
                                    continue
                                v = rgb_src[k]
                                v_t = torch.tensor(v, device=self.device)
                                # Expected shapes:
                                # - [Ho, H, W, 3]  -> [B_valid, Ho, H, W, 3]
                                # - [B, Ho, H, W, 3] (already batched)
                                if v_t.ndim == 4:
                                    v_t = v_t.unsqueeze(0).expand(
                                        len(forward_idxs), -1, -1, -1, -1
                                    )
                                elif v_t.ndim == 5:
                                    # Assume [B, Ho, H, W, 3]; trim to B_valid if needed.
                                    if v_t.shape[0] >= len(forward_idxs):
                                        v_t = v_t[: len(forward_idxs)]
                                else:
                                    continue
                                rgb_dict[k] = v_t
                            if rgb_dict:
                                batch_like["rgb"] = rgb_dict
                            else:
                                can_use_rfm = False
                        else:
                            can_use_rfm = False

                    if not can_use_rfm:
                        cond = None
                    else:
                        cond = self._build_rfm_cond_from_batch(batch_like, coarse_t)

                    if cond is not None:
                        # Integrate rectified flow along straight line (Euler steps).
                        Bv = coarse_t.shape[0]
                        r = torch.zeros(
                            Bv, self.pred_horizon, 6, device=self.device
                        )
                        steps = 16
                        times = torch.linspace(
                            0.0, 1.0, steps + 1, device=self.device
                        )[:-1]
                        delta = 1.0 / steps
                        for t in times:
                            t_full = t.expand(Bv, self.pred_horizon)
                            v = self.rfm(r, t_full, cond)
                            r = r + delta * v

                        dims_se3 = 6 * self.num_eef
                        coarse6 = coarse_t[..., :dims_se3]
                        trans_refined = coarse6[..., :3] + r[..., :3]
                        rot_coarse = coarse6[..., 3:6]
                        rot_res = r[..., 3:6]
                        rot_refined = compose_axis_angles(rot_coarse, rot_res)
                        refined6 = torch.cat([trans_refined, rot_refined], dim=-1)
                        refined_all = coarse_t.clone()
                        refined_all[..., :6] = refined6[..., :6]
                        refined_np = refined_all.detach().cpu().numpy()
                        # Scatter refined predictions back to full batch.
                        for local_idx, global_idx in enumerate(forward_idxs):
                            out_ac[global_idx] = refined_np[local_idx]

        else:  # rgb
            # Build per-view [B, Ho, H, W, 3] float32 inputs (with optional resize).
            rgb_dict = {}
            for k in self.rgb_keys:
                v = torch.tensor(obs["rgb"][k].swapaxes(0, 1)).to(self.device)
                v = v.float() / 255.0
                if self.rgb_input_size is not None:
                    B, Ho, H, W, C = v.shape
                    flat = v.reshape(B * Ho, H, W, C).permute(0, 3, 1, 2)
                    flat = F.interpolate(
                        flat,
                        size=tuple(self.rgb_input_size),
                        mode="bilinear",
                        align_corners=False,
                    )
                    v = flat.permute(0, 2, 3, 1).reshape(
                        B, Ho, *tuple(self.rgb_input_size), C
                    )
                rgb_dict[k] = v

            torch_state = torch.tensor(state_np.swapaxes(0, 1)).to(self.device).float()
            torch_obs = dict(rgb=rgb_dict, state=torch_state)
            raw_ac_dict = self.actor(torch_obs, debug=debug)

            coarse_t = self.ac_normalizer.unnormalize(raw_ac_dict["ac"]).to(
                self.device
            )  # [B, Hpred, action_dim]
            out_ac = coarse_t.detach().cpu().numpy()

            # Optional RFM refinement when enabled.
            if self.rfm_enabled:
                with torch.no_grad():
                    batch_like = {
                        "eef_pose_w": torch_state.reshape(
                            batch_size, self.obs_horizon, -1
                        ),
                        "rgb": rgb_dict,
                        "action": torch.zeros(
                            batch_size,
                            self.pred_horizon,
                            self.num_eef * self.dof,
                            device=self.device,
                        ),
                    }
                    cond = self._build_rfm_cond_from_batch(batch_like, coarse_t)
                    Bv = coarse_t.shape[0]
                    r = torch.zeros(Bv, self.pred_horizon, 6, device=self.device)
                    steps = 16
                    times = torch.linspace(
                        0.0, 1.0, steps + 1, device=self.device
                    )[:-1]
                    delta = 1.0 / steps
                    for t in times:
                        t_full = t.expand(Bv, self.pred_horizon)
                        v = self.rfm(r, t_full, cond)
                        r = r + delta * v

                    dims_se3 = 6 * self.num_eef
                    coarse6 = coarse_t[..., :dims_se3]
                    trans_refined = coarse6[..., :3] + r[..., :3]
                    rot_coarse = coarse6[..., 3:6]
                    rot_res = r[..., 3:6]
                    rot_refined = compose_axis_angles(rot_coarse, rot_res)
                    refined6 = torch.cat([trans_refined, rot_refined], dim=-1)
                    refined_all = coarse_t.clone()
                    refined_all[..., :6] = refined6[..., :6]
                    out_ac = refined_all.detach().cpu().numpy()

        # Remove batch dim if original input was a single sample.
        if not has_batch_dim:
            out_ac = out_ac[0]
            if return_dict:
                raw_ac_dict = {k: v[0] for k, v in raw_ac_dict.items()}

        if return_dict:
            return out_ac, raw_ac_dict
        else:
            return out_ac


