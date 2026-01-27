"""Configuration management for the data collection system."""

from dataclasses import dataclass, field
from typing import Literal, List


@dataclass
class RobotConfig:
    """Franky robot configuration."""
    ip: str = "172.16.0.2"
    connection_timeout_s: float = 5.0
    record_cartesian_pose: bool = True  # Record x, y, z, dx, dy, dz, quaternion
    record_gripper: bool = True  # Record gripper state (0/1)


@dataclass
class GelSightConfig:
    """GelSight Mini camera configuration."""
    name: str = "gelsight"
    device_index: int = 4
    target_width: int = 320
    target_height: int = 240
    border_fraction: float = 0.15
    warmup_frames: int = 5
    buffer_size: int = 60


@dataclass
class OrbbecConfig:
    """Orbbec Gemini 335 camera configuration."""
    name: str = "orbbec"  # Unique name for this sensor
    serial_number: str = ""  # Serial number to identify specific camera (empty = any)
    color_width: int = 1080
    color_height: int = 0  # 0 = any height
    color_format: Literal["RGB", "BGR"] = "RGB"
    color_fps: int = 30
    frame_timeout_ms: int = 200
    warmup_frames: int = 10
    buffer_size: int = 60
    # Collection flags
    collect_color: bool = True
    collect_depth: bool = True


@dataclass
class SystemConfig:
    """Data collection system configuration."""
    # Collection rate
    rate_hz: float = 10.0

    # Synchronization
    sync_strategy: Literal["closest", "latest_before"] = "closest"
    max_sync_offset_ms: float = 50.0

    # Sensor configurations
    robot: RobotConfig = field(default_factory=RobotConfig)
    gelsight_sensors: List[GelSightConfig] = field(default_factory=list)
    orbbec_sensors: List[OrbbecConfig] = field(default_factory=list)

    @property
    def period_s(self) -> float:
        """Collection period in seconds."""
        return 1.0 / self.rate_hz

    def __post_init__(self):
        """Validate configuration."""
        # Collect all sensor names
        all_names = []
        all_names.extend([gs.name for gs in self.gelsight_sensors])
        all_names.extend([orb.name for orb in self.orbbec_sensors])

        # Check for duplicates
        if len(all_names) != len(set(all_names)):
            raise ValueError(f"Duplicate sensor names detected: {all_names}")

    def add_gelsight(
        self,
        name: str,
        device_index: int = 0,
        **kwargs
    ) -> None:
        """
        Add a GelSight sensor to the configuration.

        Args:
            name: Unique name for this sensor
            device_index: Camera device index
            **kwargs: Additional GelSightConfig parameters
        """
        config = GelSightConfig(name=name, device_index=device_index, **kwargs)
        self.gelsight_sensors.append(config)

    def add_orbbec(
        self,
        name: str,
        serial_number: str = "",
        collect_color: bool = True,
        collect_depth: bool = True,
        **kwargs
    ) -> None:
        """
        Add an Orbbec sensor to the configuration.

        Args:
            name: Unique name for this sensor
            serial_number: Serial number (empty = any available)
            collect_color: Whether to collect RGB images
            collect_depth: Whether to collect depth images
            **kwargs: Additional OrbbecConfig parameters
        """
        config = OrbbecConfig(
            name=name,
            serial_number=serial_number,
            collect_color=collect_color,
            collect_depth=collect_depth,
            **kwargs
        )
        self.orbbec_sensors.append(config)

