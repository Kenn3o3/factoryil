"""Abstract sensor interfaces."""

from abc import ABC, abstractmethod
from typing import Any


class Sensor(ABC):
    """Abstract base class for all sensors."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the sensor."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown and cleanup the sensor."""
        pass


class StreamingSensor(Sensor):
    """Abstract base class for streaming sensors (cameras)."""

    @abstractmethod
    def start_stream(self) -> None:
        """Start background streaming."""
        pass

    @abstractmethod
    def stop_stream(self) -> None:
        """Stop background streaming."""
        pass

    @abstractmethod
    def wait_ready(self, timeout: float) -> bool:
        """Wait for stream to be ready."""
        pass

    @abstractmethod
    def get_frame(self, target_ns: int, strategy: str) -> Any:
        """Get frame at target timestamp."""
        pass


class OnDemandSensor(Sensor):
    """Abstract base class for on-demand sensors (robot)."""

    @abstractmethod
    def read(self) -> Any:
        """Read current sensor state."""
        pass
