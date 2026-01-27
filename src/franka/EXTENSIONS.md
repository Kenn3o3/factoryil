# System Extensions Summary

## Changes Made

### 1. Configuration (core/config.py)
- ✅ Added `name` field to all sensor configs
- ✅ Changed `orbbec` to `orbbec_sensors: List[OrbbecConfig]`
- ✅ Added `collect_color` and `collect_depth` flags to OrbbecConfig
- ✅ Added `record_cartesian_pose` and `record_gripper` to RobotConfig
- ✅ Added `add_orbbec()` helper method to SystemConfig

### 2. Data Types (core/data_types.py)
- ✅ Enhanced RobotState with:
  - `cartesian_position` (x, y, z)
  - `cartesian_orientation` (dx, dy, dz)
  - `cartesian_quaternion` (qw, qx, qy, qz)
  - `gripper_state` (0.0-1.0)
- ✅ Changed `orbbec: RGBDFrame` to `orbbec_sensors: Dict[str, RGBDFrame]`
- ✅ Made RGBDFrame.color and .depth Optional
- ✅ Changed SyncQuality to support multiple Orbbec sensors
- ✅ Added `episode_number` to Episode dataclass

### 3. Robot Sensor (sensors/robot.py)
- ✅ Implemented cartesian pose reading
- ✅ Implemented quaternion to axis-angle conversion
- ✅ Added gripper state placeholder (TODO: implement actual reading)

### 4. Orbbec Sensor (sensors/orbbec.py)
- ✅ Modified to support optional color/depth collection
- ✅ Returns dict with only requested modalities

### 5. Multi-Episode Script (collect_episodes.py)
- ✅ Created new script with 'd'/'e'/'q' controls
- ✅ Sequential episode numbering
- ✅ Interactive start/stop recording

## Still TODO

### Update core/system.py
The DataCollectionSystem needs major updates:

1. **Support multiple Orbbec sensors**:
```python
def __init__(self, config):
    self.robot = RobotSensor(config.robot)
    self.gelsight = GelSightSensor(config.gelsight)
    self.orbbec_sensors = {
        cfg.name: OrbbecSensor(cfg)
        for cfg in config.orbbec_sensors
    }
```

2. **Add episode management**:
```python
def start_episode(self, episode_num):
    """Start recording a new episode."""
    self._current_episode = Episode(
        episode_number=episode_num,
        observations=[],
        actions=[],
        action_types=[],
        step_durations_ms=[],
    )
    self._recording = True

def stop_episode(self):
    """Stop recording current episode."""
    self._recording = False

def step(self, action=None, action_type=None):
    """Only record if self._recording is True."""
    if not self._recording:
        return None
    # ... existing step logic
```

3. **Update _get_observation()**:
```python
def _get_observation(self, target_ns):
    # ... existing robot and gelsight code ...

    # Get frames from all Orbbec sensors
    orbbec_frames = {}
    orbbec_offsets = {}
    for name, sensor in self.orbbec_sensors.items():
        frame = sensor.get_frame(target_ns, self.config.sync_strategy)
        if frame is None:
            raise RuntimeError(f"No suitable {name} frame found")
        orbbec_frames[name] = frame
        orbbec_offsets[name] = offset_ms(frame.timestamp_ns, target_ns)

    # Calculate sync quality
    all_offsets = [
        abs(robot_offset),
        abs(gelsight_offset),
        *[abs(o) for o in orbbec_offsets.values()]
    ]
    max_offset = max(all_offsets)

    sync_quality = SyncQuality(
        robot_offset_ms=robot_offset,
        gelsight_offset_ms=gelsight_offset,
        orbbec_offsets_ms=orbbec_offsets,
        max_offset_ms=max_offset,
        is_synchronized=max_offset <= self.config.max_sync_offset_ms,
    )

    return Observation(
        target_timestamp_ns=target_ns,
        robot=robot_state,
        gelsight=gelsight_frame,
        orbbec_sensors=orbbec_frames,
        sync_quality=sync_quality,
    )
```

4. **Update save methods**:
```python
def save_current_episode(self, output_dir):
    """Save the current episode."""
    if self._current_episode is None:
        return

    # Create subdirectories for each Orbbec sensor
    for name in self.orbbec_sensors.keys():
        if self.orbbec_sensors[name].config.collect_color:
            (output_dir / f"{name}_color").mkdir(parents=True, exist_ok=True)
        if self.orbbec_sensors[name].config.collect_depth:
            (output_dir / f"{name}_depth").mkdir(parents=True, exist_ok=True)

    # Save CSV with all fields
    # Save images for all sensors
```

5. **Update CSV headers**:
```python
header = [
    "step", "target_timestamp_ns", "robot_timestamp_ns",
    # Joint space
    *[f"joint_{i}_pos" for i in range(7)],
    *[f"joint_{i}_vel" for i in range(7)],
    # Cartesian space (if enabled)
    "cartesian_x", "cartesian_y", "cartesian_z",
    "orientation_dx", "orientation_dy", "orientation_dz",
    "quat_w", "quat_x", "quat_y", "quat_z",
    # Gripper (if enabled)
    "gripper_state",
    # GelSight
    "gelsight_timestamp_ns", "gelsight_sequence",
    # Orbbec sensors (dynamic based on config)
    *[f"{name}_timestamp_ns" for name in orbbec_sensors],
    *[f"{name}_sequence" for name in orbbec_sensors],
    # Sync quality
    "robot_offset_ms", "gelsight_offset_ms",
    *[f"{name}_offset_ms" for name in orbbec_sensors],
    "max_offset_ms", "is_synchronized",
    # Meta
    "step_duration_ms", "action", "action_type",
]
```

## Usage Example

```python
# Single Orbbec (default)
config = SystemConfig(rate_hz=10.0)

# Multiple Orbbec sensors
config = SystemConfig(rate_hz=10.0)
config.orbbec_sensors = []  # Clear default
config.add_orbbec("orbbec_left", collect_color=True, collect_depth=True)
config.add_orbbec("orbbec_right", collect_color=True, collect_depth=False)
config.add_orbbec("orbbec_top", collect_color=False, collect_depth=True)

# Disable cartesian/gripper recording
config.robot.record_cartesian_pose = False
config.robot.record_gripper = False

# Run multi-episode collection
python collect_episodes.py --rate 10.0
```

## Testing Checklist

- [ ] Test with single Orbbec sensor
- [ ] Test with multiple Orbbec sensors
- [ ] Test with color-only collection
- [ ] Test with depth-only collection
- [ ] Test cartesian pose recording
- [ ] Test gripper state recording (when implemented)
- [ ] Test multi-episode collection
- [ ] Test 'd'/'e'/'q' controls
- [ ] Verify CSV format with all fields
- [ ] Verify image saving for all sensors

## Next Steps

1. Complete the system.py updates (see TODO section above)
2. Test with actual hardware
3. Implement gripper state reading in robot.py
4. Add serial number filtering for Orbbec sensors
5. Add visualization tools for multi-sensor data
