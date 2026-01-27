"""Main data collection system implementation."""

import time
from pathlib import Path
from typing import Optional, Any
import csv
import cv2
import numpy as np

from core.config import SystemConfig
from core.data_types import Observation, Episode, SyncQuality
from sensors import RobotSensor, GelSightSensor, OrbbecSensor
from utils.timing import monotonic_ns, sleep_until, offset_ms


class DataCollectionSystem:
    """
    Synchronized multi-modal data collection system.

    Collects robot proprioception and camera images at fixed rate
    with temporal synchronization across all modalities.
    """

    def __init__(self, config: SystemConfig):
        """
        Initialize data collection system.

        Args:
            config: System configuration
        """
        self.config = config

        # Initialize sensors
        self.robot = RobotSensor(config.robot)

        # Initialize GelSight sensors (0-N sensors)
        self.gelsight_sensors = {
            cfg.name: GelSightSensor(cfg)
            for cfg in config.gelsight_sensors
        }

        # Initialize Orbbec sensors (0-N sensors)
        self.orbbec_sensors = {
            cfg.name: OrbbecSensor(cfg)
            for cfg in config.orbbec_sensors
        }

        # State
        self._t0_ns: Optional[int] = None
        self._step_count = 0
        self._current_episode: Optional[Episode] = None
        self._recording = False

    def reset(self) -> Observation:
        """
        Initialize system and return initial observation.

        Returns:
            Initial synchronized observation
        """
        print("=" * 70)
        print("INITIALIZING DATA COLLECTION SYSTEM")
        print("=" * 70)
        print(f"Rate: {self.config.rate_hz} Hz")
        print(f"Period: {self.config.period_s * 1000:.1f} ms")
        print(f"Sync strategy: {self.config.sync_strategy}")
        print(f"GelSight sensors: {len(self.gelsight_sensors)}")
        print(f"Orbbec sensors: {len(self.orbbec_sensors)}")
        print("=" * 70)

        # Initialize all sensors
        self.robot.initialize()

        for name, sensor in self.gelsight_sensors.items():
            print(f"\nInitializing GelSight: {name}")
            sensor.initialize()

        for name, sensor in self.orbbec_sensors.items():
            print(f"\nInitializing Orbbec: {name}")
            sensor.initialize()

        # Start streaming sensors
        for name, sensor in self.gelsight_sensors.items():
            sensor.start_stream()

        for name, sensor in self.orbbec_sensors.items():
            sensor.start_stream()

        # Wait for streams to be ready
        if self.gelsight_sensors or self.orbbec_sensors:
            print("\nWaiting for camera streams...")

        for name, sensor in self.gelsight_sensors.items():
            if not sensor.wait_ready(timeout=10.0):
                raise RuntimeError(f"GelSight stream '{name}' failed to start")

        for name, sensor in self.orbbec_sensors.items():
            if not sensor.wait_ready(timeout=10.0):
                raise RuntimeError(f"Orbbec stream '{name}' failed to start")

        # Give streams a moment to accumulate frames
        if self.gelsight_sensors or self.orbbec_sensors:
            time.sleep(0.5)

        print("\n" + "=" * 70)
        print("ALL SENSORS READY")
        print("=" * 70)

        # Set t0 and reset state
        self._t0_ns = monotonic_ns()
        self._step_count = 0
        self._current_episode = None
        self._recording = False

        # Get initial observation
        initial_obs = self._get_observation(self._t0_ns)

        print(f"\nInitial observation acquired:")
        print(f"  Robot offset: {initial_obs.sync_quality.robot_offset_ms:.2f} ms")
        for name in self.gelsight_sensors:
            print(f"  GelSight '{name}' offset: {initial_obs.sync_quality.gelsight_offsets_ms[name]:.2f} ms")
        for name in self.orbbec_sensors:
            print(f"  Orbbec '{name}' offset: {initial_obs.sync_quality.orbbec_offsets_ms[name]:.2f} ms")
        print(f"  Synchronized: {initial_obs.sync_quality.is_synchronized}")

        return initial_obs

    def start_episode(self, episode_number: int) -> None:
        """
        Start a new episode.

        Args:
            episode_number: Episode number
        """
        if self._t0_ns is None:
            raise RuntimeError("System not initialized. Call reset() first.")

        self._current_episode = Episode(
            episode_number=episode_number,
            observations=[],
            actions=[],
            action_types=[],
            step_durations_ms=[],
        )
        self._recording = True
        self._step_count = 0
        self._t0_ns = monotonic_ns()  # Reset timing for new episode

    def step(
        self,
        action: Optional[Any] = None,
        action_type: Optional[str] = None,
    ) -> Observation:
        """
        Execute one step and return synchronized observation.

        Args:
            action: Action to execute (optional)
            action_type: Type of action for logging (optional)

        Returns:
            Synchronized observation
        """
        if self._t0_ns is None:
            raise RuntimeError("System not initialized. Call reset() first.")

        if not self._recording:
            raise RuntimeError("Not recording. Call start_episode() first.")

        step_start = time.monotonic()

        # TODO: Send action to robot if provided
        # For now, we just record the action

        # Calculate target time for this step
        self._step_count += 1
        t_target_ns = self._t0_ns + int(self._step_count * self.config.period_s * 1e9)

        # Sleep until target time
        sleep_until(t_target_ns)

        # Get synchronized observation
        obs = self._get_observation(t_target_ns)

        # Record step duration
        step_duration_ms = (time.monotonic() - step_start) * 1000

        # Store in episode
        if self._current_episode is not None:
            self._current_episode.observations.append(obs)
            self._current_episode.actions.append(action)
            self._current_episode.action_types.append(action_type)
            self._current_episode.step_durations_ms.append(step_duration_ms)

        return obs

    def _get_observation(self, target_ns: int) -> Observation:
        """
        Get synchronized observation at target timestamp.

        Args:
            target_ns: Target timestamp (monotonic)

        Returns:
            Synchronized observation
        """
        # Read robot state (on-demand)
        robot_state = self.robot.read()

        # Get GelSight frames
        gelsight_frames = {}
        for name, sensor in self.gelsight_sensors.items():
            frame = sensor.get_frame(target_ns, self.config.sync_strategy)
            if frame is None:
                raise RuntimeError(f"No suitable GelSight frame found for sensor '{name}'")
            gelsight_frames[name] = frame

        # Get Orbbec frames
        orbbec_frames = {}
        for name, sensor in self.orbbec_sensors.items():
            frame = sensor.get_frame(target_ns, self.config.sync_strategy)
            if frame is None:
                raise RuntimeError(f"No suitable Orbbec frame found for sensor '{name}'")
            orbbec_frames[name] = frame

        # Calculate sync quality
        robot_offset = offset_ms(robot_state.timestamp_ns, target_ns)

        gelsight_offsets = {
            name: offset_ms(frame.timestamp_ns, target_ns)
            for name, frame in gelsight_frames.items()
        }

        orbbec_offsets = {
            name: offset_ms(frame.timestamp_ns, target_ns)
            for name, frame in orbbec_frames.items()
        }

        # Calculate max offset across all sensors
        all_offsets = [abs(robot_offset)]
        all_offsets.extend([abs(o) for o in gelsight_offsets.values()])
        all_offsets.extend([abs(o) for o in orbbec_offsets.values()])
        max_offset = max(all_offsets) if all_offsets else 0.0

        sync_quality = SyncQuality(
            robot_offset_ms=robot_offset,
            gelsight_offsets_ms=gelsight_offsets,
            orbbec_offsets_ms=orbbec_offsets,
            max_offset_ms=max_offset,
            is_synchronized=max_offset <= self.config.max_sync_offset_ms,
        )

        return Observation(
            target_timestamp_ns=target_ns,
            robot=robot_state,
            gelsight_sensors=gelsight_frames,
            orbbec_sensors=orbbec_frames,
            sync_quality=sync_quality,
        )

    def save_current_episode(self, output_dir: Path) -> None:
        """
        Save current episode to disk.

        Args:
            output_dir: Directory to save data
        """
        if self._current_episode is None or len(self._current_episode) == 0:
            print("No data to save")
            return

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"Saving episode {self._current_episode.episode_number} to: {output_dir}")
        print(f"Total steps: {len(self._current_episode)}")

        # Create sensor directories
        for name in self.gelsight_sensors:
            (output_dir / name / "rgb").mkdir(parents=True, exist_ok=True)

        for name, sensor in self.orbbec_sensors.items():
            cfg = self.config.orbbec_sensors[[s.name for s in self.config.orbbec_sensors].index(name)]
            if cfg.collect_color:
                (output_dir / name / "rgb").mkdir(parents=True, exist_ok=True)
            if cfg.collect_depth:
                (output_dir / name / "depth").mkdir(parents=True, exist_ok=True)

        # Create robot directory
        (output_dir / "robot").mkdir(parents=True, exist_ok=True)

        # Save CSV
        self._save_csv(output_dir / "robot" / "proprioception.csv")

        # Save images
        self._save_images(output_dir)

        print(f"Episode saved successfully")

    def print_episode_stats(self) -> None:
        """Print statistics about current episode."""
        if self._current_episode is None or len(self._current_episode) == 0:
            print("No data collected")
            return

        print("\n" + "=" * 70)
        print("EPISODE STATISTICS")
        print("=" * 70)

        # Sync quality
        robot_offsets = [obs.sync_quality.robot_offset_ms for obs in self._current_episode.observations]
        sync_failures = sum(1 for obs in self._current_episode.observations if not obs.sync_quality.is_synchronized)

        print(f"\nSteps: {len(self._current_episode)}")
        print(f"Sync failures: {sync_failures}")

        print(f"\nRobot offset (ms):")
        print(f"  Mean: {np.mean(robot_offsets):.2f}")
        print(f"  Std:  {np.std(robot_offsets):.2f}")
        print(f"  Range: [{np.min(robot_offsets):.2f}, {np.max(robot_offsets):.2f}]")

        # GelSight offsets
        for name in self.gelsight_sensors:
            offsets = [obs.sync_quality.gelsight_offsets_ms[name] for obs in self._current_episode.observations]
            print(f"\nGelSight '{name}' offset (ms):")
            print(f"  Mean: {np.mean(offsets):.2f}")
            print(f"  Std:  {np.std(offsets):.2f}")
            print(f"  Range: [{np.min(offsets):.2f}, {np.max(offsets):.2f}]")

        # Orbbec offsets
        for name in self.orbbec_sensors:
            offsets = [obs.sync_quality.orbbec_offsets_ms[name] for obs in self._current_episode.observations]
            print(f"\nOrbbec '{name}' offset (ms):")
            print(f"  Mean: {np.mean(offsets):.2f}")
            print(f"  Std:  {np.std(offsets):.2f}")
            print(f"  Range: [{np.min(offsets):.2f}, {np.max(offsets):.2f}]")

        print(f"\nStep duration (ms):")
        print(f"  Mean: {np.mean(self._current_episode.step_durations_ms):.2f}")
        print(f"  Std:  {np.std(self._current_episode.step_durations_ms):.2f}")
        print(f"  Range: [{np.min(self._current_episode.step_durations_ms):.2f}, {np.max(self._current_episode.step_durations_ms):.2f}]")

        print("=" * 70)

    def _save_csv(self, csv_path: Path) -> None:
        """Save episode data to CSV."""
        if self._current_episode is None:
            return

        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)

            # Build header
            header = [
                "step",
                "target_timestamp_ns",
                "robot_timestamp_ns",
            ]

            # Add joint positions and velocities
            header.extend([f"joint_{i}_pos" for i in range(7)])
            header.extend([f"joint_{i}_vel" for i in range(7)])

            # Add cartesian pose fields
            header.extend(["cartesian_x", "cartesian_y", "cartesian_z"])
            header.extend(["orientation_dx", "orientation_dy", "orientation_dz"])
            header.extend(["quat_w", "quat_x", "quat_y", "quat_z"])
            header.extend(["gripper"])

            # Add sync quality
            header.extend(["robot_offset_ms", "max_offset_ms", "is_synchronized"])

            # Add GelSight sensor fields
            for name in sorted(self.gelsight_sensors.keys()):
                header.extend([f"{name}_timestamp_ns", f"{name}_sequence", f"sync_{name}_offset_ms"])

            # Add Orbbec sensor fields
            for name in sorted(self.orbbec_sensors.keys()):
                header.extend([f"{name}_timestamp_ns", f"{name}_sequence", f"sync_{name}_offset_ms"])

            # Add episode metadata
            header.extend(["step_duration_ms", "action", "action_type"])

            writer.writerow(header)

            # Data rows
            for i, obs in enumerate(self._current_episode.observations):
                row = [
                    i,
                    obs.target_timestamp_ns,
                    obs.robot.timestamp_ns,
                ]

                # Joint positions and velocities
                row.extend(obs.robot.joint_positions.tolist())
                row.extend(obs.robot.joint_velocities.tolist())

                # Cartesian pose
                if obs.robot.cartesian_position is not None:
                    row.extend(obs.robot.cartesian_position.tolist())
                else:
                    row.extend([None, None, None])

                if obs.robot.cartesian_orientation is not None:
                    row.extend(obs.robot.cartesian_orientation.tolist())
                else:
                    row.extend([None, None, None])

                if obs.robot.cartesian_quaternion is not None:
                    row.extend(obs.robot.cartesian_quaternion.tolist())
                else:
                    row.extend([None, None, None, None])

                # Gripper
                row.append(obs.robot.gripper_state if obs.robot.gripper_state is not None else None)

                # Sync quality
                row.extend([
                    obs.sync_quality.robot_offset_ms,
                    obs.sync_quality.max_offset_ms,
                    obs.sync_quality.is_synchronized,
                ])

                # GelSight sensors
                for name in sorted(self.gelsight_sensors.keys()):
                    frame = obs.gelsight_sensors[name]
                    row.extend([
                        frame.timestamp_ns,
                        frame.sequence,
                        obs.sync_quality.gelsight_offsets_ms[name],
                    ])

                # Orbbec sensors
                for name in sorted(self.orbbec_sensors.keys()):
                    frame = obs.orbbec_sensors[name]
                    row.extend([
                        frame.timestamp_ns,
                        frame.sequence,
                        obs.sync_quality.orbbec_offsets_ms[name],
                    ])

                # Episode metadata
                row.extend([
                    self._current_episode.step_durations_ms[i],
                    self._current_episode.actions[i],
                    self._current_episode.action_types[i],
                ])

                writer.writerow(row)

        print(f"Saved CSV: {csv_path}")

    def _save_images(self, output_dir: Path) -> None:
        """Save episode images."""
        if self._current_episode is None:
            return

        print("Saving images...")
        for i, obs in enumerate(self._current_episode.observations):
            # Use zero-indexed numbering: 0000, 0001, 0002, ...
            step_num = i

            # Save GelSight sensor images (RGB only)
            for name, frame in obs.gelsight_sensors.items():
                rgb_path = output_dir / name / "rgb" / f"{step_num:04d}.jpg"
                cv2.imwrite(str(rgb_path), frame.image, [cv2.IMWRITE_JPEG_QUALITY, 95])

            # Save Orbbec sensor images (RGB and/or depth)
            for name, frame in obs.orbbec_sensors.items():
                # Get sensor config to know what to save
                cfg = self.config.orbbec_sensors[[s.name for s in self.config.orbbec_sensors].index(name)]

                # Save RGB if available
                if cfg.collect_color and frame.color is not None:
                    rgb_path = output_dir / name / "rgb" / f"{step_num:04d}.jpg"
                    cv2.imwrite(str(rgb_path), frame.color, [cv2.IMWRITE_JPEG_QUALITY, 95])

                # Save depth if available
                if cfg.collect_depth and frame.depth is not None:
                    depth_dir = output_dir / name / "depth"

                    # Save raw depth as 16-bit PNG
                    depth_raw_path = depth_dir / f"{step_num:04d}.png"
                    cv2.imwrite(str(depth_raw_path), frame.depth.astype(np.uint16))

                    # Save depth as NPY for fast loading
                    depth_npy_path = depth_dir / f"{step_num:04d}.npy"
                    np.save(str(depth_npy_path), frame.depth)

                    # Save depth visualization as 8-bit colormap PNG
                    depth_viz_path = depth_dir / f"{step_num:04d}_viz.png"
                    # Normalize to 0-255 range for visualization
                    depth_normalized = cv2.normalize(frame.depth, None, 0, 255, cv2.NORM_MINMAX)
                    depth_viz = cv2.applyColorMap(depth_normalized.astype(np.uint8), cv2.COLORMAP_TURBO)
                    cv2.imwrite(str(depth_viz_path), depth_viz)

        print(f"Saved {len(self._current_episode)} frames")

    def shutdown(self) -> None:
        """Shutdown system and cleanup resources."""
        print("\nShutting down...")

        for name, sensor in self.gelsight_sensors.items():
            sensor.shutdown()

        for name, sensor in self.orbbec_sensors.items():
            sensor.shutdown()

        self.robot.shutdown()

        print("Shutdown complete")
