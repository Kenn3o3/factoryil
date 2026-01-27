"""Core data types and structures for the data collection system."""

from dataclasses import dataclass
from typing import Any, Dict, Optional, List
import numpy as np


@dataclass
class RobotState:
    """Robot proprioceptive state."""
    # Joint space
    joint_positions: np.ndarray  # Shape: (7,)
    joint_velocities: np.ndarray  # Shape: (7,)

    # Cartesian space (optional)
    cartesian_position: Optional[np.ndarray] = None  # Shape: (3,) - x, y, z
    cartesian_orientation: Optional[np.ndarray] = None  # Shape: (3,) - dx, dy, dz (axis-angle)
    cartesian_quaternion: Optional[np.ndarray] = None  # Shape: (4,) - qw, qx, qy, qz

    # Gripper (optional)
    gripper_state: Optional[float] = None  # 0.0 = closed, 1.0 = open

    timestamp_ns: int = 0  # Monotonic timestamp


@dataclass
class CameraFrame:
    """Single camera frame with metadata."""
    image: np.ndarray  # Image data
    timestamp_ns: int  # Monotonic timestamp
    sequence: int  # Frame sequence number


@dataclass
class RGBDFrame:
    """RGB-D camera frame."""
    color: Optional[np.ndarray] = None  # Color image (None if not collected)
    depth: Optional[np.ndarray] = None  # Depth image (None if not collected)
    timestamp_ns: int = 0  # Monotonic timestamp
    sequence: int = 0  # Frame sequence number


@dataclass
class SyncQuality:
    """Synchronization quality metrics."""
    robot_offset_ms: float
    gelsight_offsets_ms: Dict[str, float]  # name -> offset
    orbbec_offsets_ms: Dict[str, float]  # name -> offset
    max_offset_ms: float
    is_synchronized: bool


@dataclass
class Observation:
    """Synchronized multi-modal observation."""
    # Target timestamp for this observation
    target_timestamp_ns: int

    # Robot state
    robot: RobotState

    # Camera frames
    gelsight_sensors: Dict[str, CameraFrame]  # name -> frame
    orbbec_sensors: Dict[str, RGBDFrame]  # name -> frame

    # Synchronization quality
    sync_quality: SyncQuality

    def to_dict(self) -> Dict[str, Any]:
        """Convert observation to dictionary for logging."""
        result = {
            "target_timestamp_ns": self.target_timestamp_ns,
            "robot_timestamp_ns": self.robot.timestamp_ns,
            "robot_joint_positions": self.robot.joint_positions.tolist(),
            "robot_joint_velocities": self.robot.joint_velocities.tolist(),
            "sync_robot_offset_ms": self.sync_quality.robot_offset_ms,
            "sync_max_offset_ms": self.sync_quality.max_offset_ms,
            "sync_is_synchronized": self.sync_quality.is_synchronized,
        }

        # Add cartesian pose if available
        if self.robot.cartesian_position is not None:
            result["robot_cartesian_x"] = float(self.robot.cartesian_position[0])
            result["robot_cartesian_y"] = float(self.robot.cartesian_position[1])
            result["robot_cartesian_z"] = float(self.robot.cartesian_position[2])

        if self.robot.cartesian_orientation is not None:
            result["robot_orientation_dx"] = float(self.robot.cartesian_orientation[0])
            result["robot_orientation_dy"] = float(self.robot.cartesian_orientation[1])
            result["robot_orientation_dz"] = float(self.robot.cartesian_orientation[2])

        if self.robot.cartesian_quaternion is not None:
            result["robot_quat_w"] = float(self.robot.cartesian_quaternion[0])
            result["robot_quat_x"] = float(self.robot.cartesian_quaternion[1])
            result["robot_quat_y"] = float(self.robot.cartesian_quaternion[2])
            result["robot_quat_z"] = float(self.robot.cartesian_quaternion[3])

        if self.robot.gripper_state is not None:
            result["robot_gripper"] = float(self.robot.gripper_state)

        # Add gelsight sensors
        for name, frame in self.gelsight_sensors.items():
            result[f"{name}_timestamp_ns"] = frame.timestamp_ns
            result[f"{name}_sequence"] = frame.sequence
            result[f"sync_{name}_offset_ms"] = self.sync_quality.gelsight_offsets_ms[name]

        # Add orbbec sensors
        for name, frame in self.orbbec_sensors.items():
            result[f"{name}_timestamp_ns"] = frame.timestamp_ns
            result[f"{name}_sequence"] = frame.sequence
            result[f"sync_{name}_offset_ms"] = self.sync_quality.orbbec_offsets_ms[name]

        return result


@dataclass
class Episode:
    """Collection of observations forming an episode."""
    episode_number: int
    observations: List[Observation]
    actions: List[Optional[Any]]
    action_types: List[Optional[str]]
    step_durations_ms: List[float]

    def __len__(self) -> int:
        return len(self.observations)

