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
git clone --recursive https://github.com/Kenn3o3/factoryil.git
cd factoryil
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

# Expert demo collection (add --headless for headless run) (Currently only support peg insertion)
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

---

## Experiments

Experiment YAMLs live in `experiments/`.

```bash
# From the repo root:
python -m factoryil.run_experiment experiments/overfit_experiment.yaml
```

### Parallel steps

`factoryil.run_experiment` supports running *independent* steps in parallel via a `parallel:` step-group:

```yaml
steps:
  - name: A
    ...
  - name: B
    ...
  - name: my_parallel_block
    parallel:
      - name: C
        ...
      - name: D
        ...
```

This executes: **A → B → (C and D in parallel)**.

Notes:
- Parallel child processes write stdout/stderr to per-step logs under `data/<experiment_name>/logs/`.
- The `timelog` includes entries for both the group step and each child (step indices like `3.1`, `3.2`, ...).

# TODO

- Implement Method []
- Method Initial Evaluation []
- Set Seed []
- Full Experiment Runs []
- Explore expert for the two other tasks []
- Add data collection for teleoperation []
- Pipeline for the two other tasks []

Documentation: https://timschneider42.github.io/franky/