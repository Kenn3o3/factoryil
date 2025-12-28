"""Centralized CLI utilities for FactoryIL."""

import argparse
from typing import Optional

from . import config as C
from isaaclab.app import AppLauncher


def build_tacex_runner_parser() -> argparse.ArgumentParser:
    """Build the parser used by the TacEx RL runner (LSTM policies)."""
    parser = argparse.ArgumentParser("TacEx runner (RL-only, LSTM policies)")
    parser.add_argument(
        "--mode",
        type=str,
        default="debug",
        choices=[
            "debug",
            "train",
            "train_rl",
            "collect",
            "collect_data",
            "il_infer",
            "eval_il",
            "eval",
            "probe",
        ],
        help=(
            "Runner mode. Preferred: train/train_rl, collect/collect_data, "
            "il_infer/eval_il."
        ),
    )
    parser.add_argument(
        "--task",
        type=str,
        default="TacEx-Factory-PegInsert-Direct-v0",
        help="Gym task name.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="lstm_rgb_proprio",
        choices=list(C.MODEL_TO_MODALITY.keys()),
        help="Which RL model/policy to run.",
    )
    parser.add_argument(
        "--num_envs",
        type=int,
        default=1,
        help="Number of parallel envs.",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--out_dir",
        type=str,
        default=C.OUT_DIR,
        help="Output root directory.",
    )
    parser.add_argument(
        "--run_name",
        type=str,
        default=None,
        help="Name for this run (folder).",
    )

    # Training controls
    parser.add_argument(
        "--total_steps",
        type=int,
        default=200_000,
        help="Total env steps across all envs.",
    )
    parser.add_argument(
        "--log_interval_updates",
        type=int,
        default=10,
        help="Print/log every N PPO updates.",
    )
    parser.add_argument(
        "--save_interval_updates",
        type=int,
        default=5,
        help="Save checkpoint every N PPO updates.",
    )
    parser.add_argument(
        "--max_iterations",
        type=int,
        default=None,
        help="RL-Games max_epochs override (train).",
    )

    # RL checkpoints
    parser.add_argument(
        "--checkpoint",
        type=str,
        default=None,
        help="Policy checkpoint path for RL models (train resume/eval).",
    )

    # Exploration fallback (used when --mode train with no checkpoint)
    parser.add_argument(
        "--exploration_policy",
        type=str,
        default="gaussian",
        choices=["zero", "gaussian", "uniform"],
        help="Exploration policy when training without a checkpoint.",
    )
    parser.add_argument(
        "--exploration_scale",
        type=float,
        default=0.1,
        help=(
            "Scale for exploration actions (stdev for gaussian; range for "
            "uniform)."
        ),
    )

    # Probe mode args (deterministic actuation tests)
    parser.add_argument(
        "--probe_amplitude",
        type=float,
        default=0.2,
        help="Constant magnitude for actuation probe.",
    )
    parser.add_argument(
        "--probe_steps",
        type=int,
        default=20,
        help="Steps per sign (+/-) for each action dimension.",
    )

    # Evaluation episodes (for eval mode)
    parser.add_argument(
        "--episodes",
        type=int,
        default=10,
        help="Episodes to run in eval mode.",
    )

    # Progress/log toggles
    parser.add_argument(
        "--no_progress_bar",
        action="store_true",
        help="Disable progress bar during training.",
    )

    # Success criteria overrides
    parser.add_argument(
        "--success_frac",
        type=float,
        default=0.03,
        help=(
            "Override vertical success threshold as a fraction of "
            "socket/thread height (e.g., 0.01)."
        ),
    )
    parser.add_argument(
        "--success_xy_tol_mm",
        type=float,
        default=3.0,
        help=(
            "Override XY centering tolerance for success in millimeters "
            "(e.g., 1.0)."
        ),
    )
    # Deterministic initial poses (disable all reset-time randomization)
    parser.add_argument(
        "--deterministic_init",
        action="store_true",
        help=(
            "If set, zero-out all reset-time noise so peg, hole, and robot "
            "start identically."
        ),
    )

    # Dataset collection
    parser.add_argument(
        "--data_dir",
        type=str,
        default="data/peg_insertion",
        help="Root directory to store collected episodes (folders episodeXX).",
    )
    parser.add_argument(
        "--rlg_ckpt",
        type=str,
        default=None,
        help=(
            "Path to RL-Games checkpoint (.pth). When provided in --mode "
            "collect, uses RL-Games policy instead of local PPO."
        ),
    )
    parser.add_argument(
        "--rlg_agent_cfg",
        type=str,
        default=None,
        help=(
            "Path to RL-Games agent YAML config used to construct the policy "
            "during collection."
        ),
    )

    # Optional video recording with official gym RecordVideo wrapper
    parser.add_argument(
        "--record_video_dir",
        type=str,
        default=None,
        help=(
            "If set, wrap env with gym.wrappers.RecordVideo and save mp4s "
            "here."
        ),
    )
    parser.add_argument(
        "--record_video_length",
        type=int,
        default=1000,
        help="Number of steps per recorded video.",
    )
    parser.add_argument(
        "--record_video_every",
        type=int,
        default=1,
        help="Record trigger period in steps (1 records every episode).",
    )

    parser.add_argument(
        "--save_pc",
        action="store_true",
        help=(
            "If set, save per-frame object point clouds from the camera "
            "(uses instance-id segmentation)."
        ),
    )
    parser.add_argument(
        "--pc_object",
        type=str,
        default="hole",
        choices=["hole", "peg", "both"],
        help=(
            "Which object clouds to save: hole=FixedAsset, peg=HeldAsset, "
            "both=save both."
        ),
    )
    parser.add_argument(
        "--pc_max_points",
        type=int,
        default=4096,
        help=(
            "Uniformly downsample each per-env cloud to at most this many "
            "points."
        ),
    )
    parser.add_argument(
        "--save_pc_world",
        action="store_true",
        help=(
            "If set, also save per-frame world point clouds reconstructed "
            "from depth."
        ),
    )
    parser.add_argument(
        "--pc_world_max_points",
        type=int,
        default=10000,
        help="Downsample each per-env world cloud to at most this many points.",
    )

    # IL inference
    parser.add_argument(
        "--il_config",
        type=str,
        default=None,
        help=(
            "IL config name under src/third_party/imitation_learning/policies/"
            "configs (e.g., dp_pc, dp_rgb_cam, dp_rgb_cam_tl, "
            "dp_rgb_cam_tl_tr, equibot)."
        ),
    )
    parser.add_argument(
        "--il_ckpt",
        type=str,
        default=None,
        help="Path to IL checkpoint .pth saved by IL training.",
    )
    parser.add_argument(
        "--il_max_steps",
        type=int,
        default=None,
        help="If set, cap each inference episode to this many env steps (per env).",
    )

    # Weights & Biases (optional)
    parser.add_argument(
        "--wandb",
        action="store_true",
        help="Enable Weights & Biases logging.",
    )
    parser.add_argument(
        "--wandb_project",
        type=str,
        default="visuotact",
        help="W&B project name.",
    )
    parser.add_argument(
        "--wandb_entity",
        type=str,
        default=None,
        help="W&B entity (team/user).",
    )
    parser.add_argument(
        "--wandb_run_name",
        type=str,
        default=None,
        help="W&B run name (defaults to run_name).",
    )
    parser.add_argument(
        "--wandb_mode",
        type=str,
        default="online",
        choices=["online", "offline", "disabled"],
        help="W&B mode.",
    )

    # Isaac app args (device, headless, etc.)
    AppLauncher.add_app_launcher_args(parser)
    return parser


def parse_tacex_args() -> argparse.Namespace:
    """Convenience wrapper to parse TacEx runner CLI arguments."""
    parser = build_tacex_runner_parser()
    args, _ = parser.parse_known_args()

    if getattr(args, "run_name", None) is None:
        from .config import default_run_name

        args.run_name = default_run_name()
    return args


def parse_args() -> argparse.Namespace:
    """Backward-compatible alias for TacEx runner argument parsing."""
    return parse_tacex_args()


def build_factoryil_runner_parser() -> argparse.ArgumentParser:
    """Parser for FactoryIL unified runner (expert / replay / IL)."""
    parser = argparse.ArgumentParser(
        description="IL inference + data collection for FactoryIL peg-insertion."
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="expert",
        choices=["expert", "replay", "il"],
        help=(
            "Agent to run: 'expert' (analytic controller), "
            "'replay' (episode replay), or 'il' (Diffusion Policy / EquiBot)."
        ),
    )
    parser.add_argument(
        "--task",
        type=str,
        default="peg_insert",
        choices=["peg_insert", "gear_mesh", "nut_thread"],
        help="Task to run.",
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="collect",
        choices=["collect", "evaluate"],
        help=(
            "Runner mode. "
            "'collect': run until --episodes SUCCESSFUL episodes are saved. "
            "'evaluate': run exactly --episodes total episodes (success+fail), "
            "save them under SUCCESS/ and FAILED/, and report success rate as JSON."
        ),
    )
    parser.add_argument(
        "--episodes",
        type=int,
        default=32,
        help=(
            "Episode budget. "
            "In --mode collect: number of SUCCESSFUL episodes to save. "
            "In --mode evaluate: number of TOTAL episodes to run (success+fail)."
        ),
    )
    parser.add_argument(
        "--num_envs",
        type=int,
        default=8,
        help="Number of parallel FactoryIL environments.",
    )
    parser.add_argument(
        "--timeout_s",
        type=float,
        default=10.0,
        help=(
            "Per-episode time limit in seconds (used to configure FactoryIL "
            "env)."
        ),
    )
    parser.add_argument(
        "--timeout_steps",
        type=int,
        default=None,
        help=(
            "Optional per-episode time limit in *environment steps* (preferred "
            "for deterministic datasets). If set, this overrides --timeout_s."
        ),
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default="data/peg_insertion_demo/il_infer",
        help=(
            "Root directory to store collected episodes (expert/IL/replay). "
            "SUCCESS -> <data_dir>/SUCCESS/episodeXX/, "
            "FAILED -> <data_dir>/FAILED/episodeXX/, "
            "staging -> <data_dir>/.staging/."
        ),
    )
    parser.add_argument(
        "--discard_timeouts",
        action="store_true",
        help=(
            "If set, episodes that time out (non-success) are discarded instead "
            "of being saved under FAILED/."
        ),
    )

    # IL-policy configuration (used when --agent=il).
    parser.add_argument(
        "--il_config",
        type=str,
        default=None,
        help=(
            "IL config name under "
            "your EquiBot/DiffusionPolicy configs directory "
            "(e.g., dp_pc, dp_rgb_cam, dp_rgb_cam_tl, dp_rgb_cam_tl_tr, "
            "equibot). Required when --agent=il."
        ),
    )
    parser.add_argument(
        "--il_ckpt",
        type=str,
        default=None,
        help=(
            "Path to IL checkpoint .pth saved by IL training (required when "
            "--agent=il)."
        ),
    )

    # Replay-specific options.
    parser.add_argument(
        "--episode_dir",
        type=str,
        default=None,
        help=(
            "For ReplayAgent: path to an 'episodeXX' directory containing "
            "'timestamps_robot.csv' to replay."
        ),
    )

    parser.add_argument(
        "--il_max_steps",
        type=int,
        default=None,
        help="If set, cap each inference rollout to this many env steps.",
    )

    # Point clouds (for saving + optional agent input when obs_mode == 'pc').
    parser.add_argument(
        "--save_pc",
        action="store_true",
        help=(
            "If set, save per-frame object point clouds for the hole "
            "(pc_hole)."
        ),
    )
    parser.add_argument(
        "--save_pc_world",
        action="store_true",
        help=(
            "If set, also save per-frame world point clouds (pc_world)."
        ),
    )
    parser.add_argument(
        "--pc_max_points",
        type=int,
        default=4096,
        help=(
            "Max points per fixed-object point cloud used for agent/saving."
        ),
    )
    parser.add_argument(
        "--pc_world_max_points",
        type=int,
        default=8192,
        help="Max points per world point cloud.",
    )
    parser.add_argument(
        "--pc_object",
        type=str,
        default="hole",
        choices=["hole", "world"],
        help=(
            "Which point cloud to feed the IL agent when obs_mode == 'pc'. "
            "Note: only 'hole' and 'world' are supported by FactoryIL "
            "collectors."
        ),
    )

    # Environment initialization randomization (must match collection for consistency).
    parser.add_argument(
        "--rand_eef",
        type=float,
        default=0.0,
        help=(
            "Max absolute EE translation noise per axis (meters) applied at "
            "reset. Sets env_cfg.eef_init_pos_noise = "
            "[rand_eef, rand_eef, rand_eef]."
        ),
    )
    parser.add_argument(
        "--rand_peg",
        type=float,
        default=0.0,
        help=(
            "Max absolute peg pose noise (meters). When "
            "spawn_in_gripper=True this is applied in the gripper frame; "
            "otherwise in world frame. Sets "
            "env_cfg.held_init_pos_noise = [rand_peg, rand_peg, rand_peg]."
        ),
    )
    parser.add_argument(
        "--rand_hole",
        type=float,
        default=0.0,
        help=(
            "Max absolute hole pose noise (meters) in world frame at reset. "
            "Sets env_cfg.fixed_init_pos_noise = "
            "[rand_hole, rand_hole, rand_hole]."
        ),
    )
    parser.add_argument(
        "--ac_horizon",
        type=int,
        default=None,
        help=(
            "If set, override the agent's ac_horizon (number of env steps to "
            "execute before re-inferring). The effective value is clamped to "
            "pred_horizon."
        ), 
    )

    # Isaac app args (device, headless, etc.).
    AppLauncher.add_app_launcher_args(parser)
    return parser