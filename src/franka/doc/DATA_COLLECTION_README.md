# Synchronized Data Collection System

A synchronized multi-modal data collection system for robot manipulation with tactile and visual sensing.

## System Overview

This system collects synchronized data from:
- **Franky robot proprioception** (joint positions and velocities)
- **GelSight Mini** tactile camera (3280x2464 BGR images)
- **Orbbec Gemini 335** RGB-D camera (color + depth images)

Key features:
- **Fixed-rate collection** at configurable Hz (default: 10 Hz)
- **Temporal synchronization** using monotonic timestamps
- **Background frame grabbing** with ring buffers to minimize latency
- **Automatic warmup** to discard unstable initial frames
- **Sync quality monitoring** with offset tracking

## Architecture

```
DataCollectionSystem (10 Hz master clock)
    │
    ├─> Sensors
    │     ├─> Robot (on-demand read)
    │     ├─> CameraStream (GelSight)
    │     │     └─> Background thread + ring buffer
    │     └─> CameraStream (Orbbec)
    │           └─> Background thread + ring buffer
    │
    └─> step(action) -> SensorSnapshot
```

### Key Components

1. **camera_stream.py**: Background frame grabbing with ring buffer
   - Continuously grabs frames in separate thread
   - Stores recent frames (default: 60) with timestamps
   - Provides frame selection strategies (closest, latest_before)

2. **sensors.py**: Unified sensor interface
   - Manages all sensor initialization and cleanup
   - Provides `snapshot(t_target)` for synchronized reads
   - Calculates sync quality metrics

3. **data_collection_system.py**: Main collection system
   - Runs at fixed rate (configurable Hz)
   - Calls `step(action)` to collect synchronized observations
   - Saves data to disk (images + CSV)

4. **run_demo.py**: Minimal demonstration script

## Usage

### Basic Demo

```bash
# Interactive mode (wait for 'd' input)
python run_demo.py

# Auto mode (no user input)
python run_demo.py --auto

# Custom parameters
python run_demo.py --auto --steps 50 --rate 5.0
```

### Command Line Options

```
--auto          Skip user input and start automatically
--steps N       Number of steps to collect (default: 20)
--rate HZ       Collection rate in Hz (default: 10.0)
```

### Demo Workflow

1. **Initialization**: Start all sensors and wait for warmup
2. **Wait for input**: Press 'd' to start (or use --auto)
3. **Data collection**: Collect N steps at specified rate
4. **Save data**: Save to timestamped folder in `_out/`

## Output Format

Data is saved to `_out/demo_YYYYMMDD_HHMMSS/`:

```
demo_YYYYMMDD_HHMMSS/
├── demo_data.csv          # Robot state, actions, timestamps, sync quality
├── orbbec_color/          # RGB images (JPEG)
│   ├── color_0001.jpg
│   ├── color_0002.jpg
│   └── ...
├── orbbec_depth/          # Depth images (16-bit PNG)
│   ├── depth_0001.png
│   ├── depth_0002.png
│   └── ...
└── gelsight/              # Tactile images (JPEG)
    ├── gelsight_0001.jpg
    ├── gelsight_0002.jpg
    └── ...
```

### CSV Format

The CSV file contains:
- **Timestamps**: `t_target_ns`, `robot_t_ns`, `gelsight_t_ns`, `orbbec_t_ns`
- **Sequence numbers**: `gelsight_seq`, `orbbec_seq`
- **Sync quality**: `robot_offset_ms`, `gelsight_offset_ms`, `orbbec_offset_ms`, `sync_ok`
- **Robot state**: `joint_0_pos` through `joint_6_pos`, `joint_0_vel` through `joint_6_vel`
- **Action**: `action`, `action_type`
- **Timing**: `step_duration_ms`

## Synchronization Strategy

### Time Base
- **Monotonic clock** (`time.monotonic_ns()`) for synchronization
- **Real-time clock** (`time.time_ns()`) for logging (optional)

### Frame Selection
Two strategies available:
1. **closest** (default): Select frame closest to target time
2. **latest_before**: Select latest frame before target time

### Sync Quality
- Each modality's offset from target time is calculated
- `sync_ok` flag indicates if all offsets are within tolerance (50ms)
- Typical offsets:
  - Robot: ~0.1 ms (very fast, on-demand read)
  - GelSight: ~20-30 ms (depends on frame rate)
  - Orbbec: ~20-30 ms (depends on frame rate)

## Performance

Typical performance (20-step test at 10 Hz):

```
Steps collected: 20
Sync failures: 0

Robot offset (ms):
  Mean: 0.14, Std: 0.02, Min: 0.09, Max: 0.17

GelSight offset (ms):
  Mean: -23.61, Std: 15.32, Min: -47.30, Max: -0.02

Orbbec offset (ms):
  Mean: -19.59, Std: 15.70, Min: -33.72, Max: -0.10

Step duration (ms):
  Mean: 99.95, Std: 0.07, Min: 99.81, Max: 100.06
```

- **Step timing**: Very stable (~100ms ± 0.1ms for 10 Hz)
- **Camera sync**: Within ±50ms (acceptable for manipulation tasks)
- **Robot sync**: Sub-millisecond (negligible)

## Integration with Your Code

### Basic Usage

```python
from config import ProbeConfig
from data_collection_system import DataCollectionSystem

# Create system
config = ProbeConfig()
system = DataCollectionSystem(config, rate_hz=10.0)

# Initialize
initial_obs = system.reset()

# Collect data
for i in range(num_steps):
    # Your action here
    action = compute_action(...)

    # Step and get synchronized observation
    result = system.step(action=action, action_type="your_action_type")

    # Access data
    robot_state = result.snapshot.robot_state
    gelsight_img = result.snapshot.gelsight_frame
    orbbec_color = result.snapshot.orbbec_color
    orbbec_depth = result.snapshot.orbbec_depth

    # Check sync quality
    if not result.snapshot.sync_ok:
        print("Warning: sync quality degraded")

# Save episode
system.save_episode(output_dir, episode_name="my_episode")

# Cleanup
system.shutdown()
```

### Advanced: Custom Sensor Configuration

```python
from config import ProbeConfig, RobotConfig, GelSightMiniConfig, OrbbecGemini335Config

config = ProbeConfig(
    robot=RobotConfig(ip="172.16.0.2"),
    gelsight=GelSightMiniConfig(
        device_idx=0,
        warmup_frames=10,
    ),
    orbbec=OrbbecGemini335Config(
        color_fps=30,
        frame_timeout_ms=200,
    ),
)

system = DataCollectionSystem(
    config=config,
    rate_hz=5.0,  # 5 Hz collection
    sync_strategy="latest_before",  # Use latest frame before target
)
```

## Troubleshooting

### Camera Initialization Slow
- **Symptom**: Long warmup time
- **Solution**: Cameras need time to stabilize. This is normal (2-3 seconds).

### Sync Quality Degraded
- **Symptom**: `sync_ok=False` or large offsets
- **Cause**: Camera frame rate < collection rate, or USB bandwidth issues
- **Solution**:
  - Lower collection rate
  - Use separate USB controllers for cameras
  - Check USB 3.0 connection

### Missing Frames
- **Symptom**: "No suitable frame found" error
- **Cause**: Camera stream stopped or too slow
- **Solution**: Check camera connection, increase buffer size

### Step Timing Jitter
- **Symptom**: Step duration varies significantly
- **Cause**: System load or blocking operations
- **Solution**: Reduce background processes, check for blocking I/O

## Configuration

Edit `config.py` to change default settings:

```python
@dataclass
class ProbeConfig:
    duration_s: float = 20.0
    robot: RobotConfig = None
    gelsight: GelSightMiniConfig = None
    orbbec: OrbbecGemini335Config = None
```

## Future Enhancements

Potential improvements:
- [ ] Hardware-triggered synchronization
- [ ] Real-time action execution on robot
- [ ] Online visualization
- [ ] Compressed data storage (HDF5)
- [ ] Multi-episode management
- [ ] Replay functionality
