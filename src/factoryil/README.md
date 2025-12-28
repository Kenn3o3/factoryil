### FactoryIL

This package contains:

- **Simulation + data collection / evaluation**: `python -m factoryil.runner`
- **Teleoperation (keyboard / SpaceMouse / gamepad)**: `python -m factoryil.teleop` (NOT ADDED DATA COLLECTION PIPELINE YET)
- **Offline dataset conversion**: `python -m factoryil.tools.convert_to_npz`
- **IL policies (vendored)**: `python -m imitation_learning.policies.train` (NOT RELEASED)

Policies are trained/inferred directly in the simulator’s conventions (world/env frames).

### Quickstart

Make sure you installed the repo (from the repo root):

```bash
pip install -e .
# For training the vendored IL policies:
pip install -e '.[il]'
```

- **Teleoperate a task**

```bash
python -m factoryil.teleop --task peg_insert --teleop_device keyboard --device cuda:0 --enable_cameras
```

- **Collect expert demos** (optional: add `--headless` to end headless mode)

```bash
python -m factoryil.runner \
  --mode collect \
  --agent expert \
  --task peg_insert \
  --episodes 8 \
  --num_envs 8 \
  --data_dir exp_data/DEBUG/raw_demo \
  --save_pc \
  --timeout_steps 110 \
  --discard_timeouts \
  --device cuda:0 --enable_cameras
```

- Output layout:
  - Success: `exp_data/DEBUG/raw_demo/SUCCESS/episodeXX/`
  - Failed/timeout (if not `--discard_timeouts`): `exp_data/DEBUG/raw_demo/FAILED/episodeXX/`

- **Convert demos to per-frame NPZ (for training)**

```bash
python -m factoryil.tools.convert_to_npz \
  --episodes_root exp_data/DEBUG/raw_demo/SUCCESS \
  --out_dir exp_data/DEBUG/training_data \
  --pc_num_points 300 \
  --pc_random_seed 0 \
  --num_workers 16
```

- **Train a point-cloud Diffusion Policy**

```bash
python -m imitation_learning.policies.train \
  --config-name dp_pc \
  prefix=DEBUG_dp_pc \
  data_path=exp_data/DEBUG/training_data \
  log_dir=exp_data/DEBUG/models/dp_pc \
  use_wandb=false \
  training.num_epochs=10
```

- **Run IL inference inside FactoryIL**

```bash
python -m factoryil.runner \
  --mode evaluate \
  --agent il \
  --task peg_insert \
  --il_config dp_pc \
  --il_ckpt exp_data/DEBUG/models/dp_pc \
  --episodes 8 \
  --num_envs 8 \
  --data_dir exp_data/DEBUG/il_infer \
  --save_pc \
  --timeout_steps 110 \
  --device cuda:0 --enable_cameras --headless
```

- Evaluate mode prints JSON to stdout (args at start + `eval_summary` at end) and also writes:
  - `exp_data/DEBUG/il_infer/eval_summary.json`

### Run the full overfit experiment YAML

This runs **collect → convert → train (DP_PC + DP_RGB) → infer**:

```bash
python -m factoryil.run_experiment src/factoryil/experiments/overfit_experiment.yaml
```