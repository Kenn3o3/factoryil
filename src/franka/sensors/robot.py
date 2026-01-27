"""Franky robot sensor implementation."""

import sys
import numpy as np
from pathlib import Path
from typing import Optional

# Support running this file directly, e.g. `python sensors/robot.py`.
if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from sensors.base import OnDemandSensor
from core import RobotConfig, RobotState
from utils.timing import monotonic_ns


class RobotSensor(OnDemandSensor):
    """Franky robot proprioception sensor."""

    def __init__(self, config: RobotConfig):
        super().__init__("robot")
        self.config = config
        self._robot = None
        self._gripper = None
        self._gripper_threshold = 0.02  # Width threshold (m) for closed (0) vs open (1)

    def initialize(self) -> None:
        """Connect to robot."""
        from franky import Robot, Gripper

        print(f"[{self.name}] Connecting to {self.config.ip}...")
        self._robot = Robot(self.config.ip)

        # Initialize gripper if gripper recording is enabled
        if self.config.record_gripper:
            try:
                self._gripper = Gripper(self.config.ip)
                print(f"[{self.name}] Gripper initialized")
            except Exception as e:
                print(f"[{self.name}] Warning: Could not initialize gripper: {e}")
                self._gripper = None

        print(f"[{self.name}] Connected")

    def shutdown(self) -> None:
        """Disconnect from robot."""
        if self._robot is not None:
            print(f"[{self.name}] Disconnecting...")
            self._robot = None

    def read(self) -> RobotState:
        """
        Read current robot state.

        Returns:
            RobotState with joint positions, velocities, and optionally cartesian pose and gripper
        """
        if self._robot is None:
            raise RuntimeError("Robot not initialized")

        timestamp_ns = monotonic_ns()
        joint_state = self._robot.current_joint_state

        # Create base state
        state = RobotState(
            joint_positions=np.array(joint_state.position),
            joint_velocities=np.array(joint_state.velocity),
            timestamp_ns=timestamp_ns,
        )

        # Add cartesian pose if requested
        if self.config.record_cartesian_pose:
            try:
                cartesian_state = self._robot.current_cartesian_state
                pose = cartesian_state.pose.ee_pose

                # Position (x, y, z)
                state.cartesian_position = np.array([pose.t[0], pose.t[1], pose.t[2]])

                # Quaternion (w, x, y, z)
                state.cartesian_quaternion = np.array([pose.q[0], pose.q[1], pose.q[2], pose.q[3]])

                # Convert quaternion to axis-angle for orientation (dx, dy, dz)
                # This is a simplified representation - you may want to use rotation matrices
                qw, qx, qy, qz = pose.q
                angle = 2 * np.arccos(np.clip(qw, -1, 1))
                if angle < 1e-10:
                    state.cartesian_orientation = np.array([0.0, 0.0, 0.0])
                else:
                    s = np.sin(angle / 2)
                    state.cartesian_orientation = np.array([qx / s, qy / s, qz / s]) * angle

            except Exception as e:
                print(f"[{self.name}] Warning: Could not read cartesian state: {e}")

        # Add gripper state if requested
        if self.config.record_gripper:
            try:
                if self._gripper is not None:
                    # Read gripper state
                    gripper_state = self._gripper.state
                    gripper_width = gripper_state.width

                    # Convert to binary: 0 = closed, 1 = open
                    # Using threshold: width < threshold means closed
                    state.gripper_state = 1.0 if gripper_width >= self._gripper_threshold else 0.0
                else:
                    state.gripper_state = None
            except Exception as e:
                print(f"[{self.name}] Warning: Could not read gripper state: {e}")
                state.gripper_state = None

        return state


if __name__ == "__main__":
    """Test script to read 10 robot states and save to sensors/test folder."""
    import time
    import numpy as np
    from pathlib import Path

    # Create test directory
    test_dir = Path(__file__).parent / "test"
    test_dir.mkdir(exist_ok=True)

    print("Initializing Robot sensor...")
    config = RobotConfig()
    sensor = RobotSensor(config)

    try:
        sensor.initialize()

        print("Connected. Reading 10 robot states...")

        for i in range(10):
            state = sensor.read()

            # Create a dictionary with all state data
            state_data = {
                "timestamp_ns": state.timestamp_ns,
                "joint_positions": state.joint_positions,
                "joint_velocities": state.joint_velocities,
            }

            if state.cartesian_position is not None:
                state_data["cartesian_position"] = state.cartesian_position
            if state.cartesian_orientation is not None:
                state_data["cartesian_orientation"] = state.cartesian_orientation
            if state.cartesian_quaternion is not None:
                state_data["cartesian_quaternion"] = state.cartesian_quaternion
            if state.gripper_state is not None:
                state_data["gripper_state"] = state.gripper_state

            # Save state
            state_path = test_dir / f"robot_state_{i:03d}.npy"
            np.save(state_path, state_data)
            print(f"Saved state {i} to {state_path}")

            time.sleep(0.1)  # Small delay between reads

        print(f"\nSuccessfully captured 10 robot states to {test_dir}")

    finally:
        sensor.shutdown()
        print("Sensor shutdown complete")

