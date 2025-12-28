## FactoryIL

FactoryIL is a **teleoperation / imitation-learning oriented** set of Isaac Lab environments for “factory” manipulation tasks (peg insertion, gear meshing, nut threading), with **GelSight Mini** tactile sensors + an overhead RGB/Depth camera.

## Installation

### 0) Prerequisites
- Ubuntu + NVIDIA GPU drivers compatible with your Isaac Sim version.
- An Isaac Lab + Isaac Sim install.

```bash
git lfs install
```

### 1) Install the IsaacLab conda env (`env_isaaclab`)

Follow https://github.com/DH-Ng/TacEx

### 2) Install FactoryIL

```bash
cd /path/to/factoryil
conda activate env_isaaclab
pip install -e .
```

## Quickstart

### Run the unified runner (expert / replay / IL)

The unified runner is `factoryil.runner` and uses Isaac Lab’s `AppLauncher`.
Recommended launch style is via the IsaacLab wrapper:

```bash
conda activate env_isaaclab
cd /path/to/factoryil

# Expert demo collection (add --headless for headless run)
python -m factoryil.runner \
  --agent expert \
  --task peg_insert \
  --episodes 10 \
  --num_envs 10 \
  --timeout_steps 110 --discard_timeouts \
  --rand_eef 0.05 --rand_hole 0.05 --rand_peg 0.005 \
  --data_dir ./data/debug_expert \
  --save_pc --pc_max_points 4096 \
  --device cuda:0 --enable_cameras --headless
```

### Teleoperate (keyboard / SpaceMouse / gamepad)

Use `factoryil.teleop` to manually control the Franka end-effector in any FactoryIL task:

```bash
conda activate env_isaaclab
cd /path/to/factoryil

# Keyboard teleop (interactive viewer)
python -m factoryil.teleop --task peg_insert --teleop_device keyboard --device cuda:0

# SpaceMouse teleop
python -m factoryil.teleop --task gear_mesh --teleop_device spacemouse --device cuda:0

# Gamepad teleop
python -m factoryil.teleop --task nut_thread --teleop_device gamepad --device cuda:0
```

The script prints the active key/button mapping on startup. Press `R` to reset the environment.
To keep commands clean, tune step sizes / clamps by editing the globals at the top of `src/factoryil/teleop.py`.

If the SpaceMouse is not detected, you may need to grant additional permissions for `/dev/hidraw*`
(see [Isaac Lab teleop docs](https://isaac-sim.github.io/IsaacLab/v2.0.1/source/overview/teleop_imitation.html)).

#### Output format

For the run above, episodes are written to:
- **Success**: `./data/debug_expert/episodeXX/`
- **Failed/timeouts**: `./data/debug_expert/FAILED/episodeXX/`
- A temporary staging area is used: `./data/debug_expert/.staging/`

Each `episodeXX/` contains `timestamps_robot.csv` and modality folders like `rgb_cam/`, `depth_cam/`, `rgb_tactile_left/`, `rgb_tactile_right/`, and optionally `pc/` (only populated when you pass `--save_pc`).

The dataset root (i.e., your `--data_dir`) also stores **`camera_params.json`** with the camera intrinsics/extrinsics + env origins from the collection run. Offline tools like `factoryil.tools.episode_to_video` will auto-discover this file to project the EEF marker correctly.

### Replay a saved episode

You have two options:

1) **Replay inside the unified runner** (also logs a new episode):

```bash
python -m factoryil.runner \
  --agent replay \
  --task peg_insert \
  --episodes 1 \
  --num_envs 1 \
  --timeout_s 3.0 \
  --episode_dir ./data/debug_expert/episode00 \
  --device cuda:0 --headless --enable_cameras
```

2) **Replay-only script** (does not save new data): `factoryil.replay_actions`

```bash
python -m factoryil.replay_actions \
  --episode_dir ./data/debug_expert/episode00 \
  --timeout_s 3.0 \
  --device cuda:0 --headless --enable_cameras
```

---

## Debugging helpers

### Segmentation / pointcloud debug dumps

In `factoryil.utils.data.vision`, you can enable debug dumps for env-0:

```bash
export VT_DEBUG_SEG=1
export VT_DEBUG_DIR=/tmp/vt_debug   # optional (defaults to ./vt_debug)
```

---

## Troubleshooting

### `ModuleNotFoundError: torch`
You are not in your Isaac Lab environment. Run:

```bash
conda activate env_isaaclab
```

### `ModuleNotFoundError: cv2` or `matplotlib`
Install tactile runtime deps:

```bash
pip install opencv-python matplotlib
```

### `import tacex_assets` fails
Make sure you installed this repo in editable mode:

```bash
cd /path/to/factoryil
pip install -e .
```




## Experiments

Experiment YAMLs live in `src/factoryil/experiments/`.

```bash
# From the repo root:
python -m factoryil.run_experiment src/factoryil/experiments/overfit_experiment.yaml
```