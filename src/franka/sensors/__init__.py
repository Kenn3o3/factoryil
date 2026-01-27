"""Sensors package.

Keep imports lightweight and avoid importing optional/hardware-backed sensors at
package import time.
"""

from __future__ import annotations

from .base import Sensor, StreamingSensor, OnDemandSensor


def __getattr__(name: str):
    """Lazy-load concrete sensors to avoid circular/optional imports."""

    if name == "RobotSensor":
        from .robot import RobotSensor as _RobotSensor

        return _RobotSensor
    if name == "GelSightSensor":
        from .gelsight import GelSightSensor as _GelSightSensor

        return _GelSightSensor
    if name == "OrbbecSensor":
        from .orbbec import OrbbecSensor as _OrbbecSensor

        return _OrbbecSensor

    raise AttributeError(f"module 'sensors' has no attribute {name!r}")


__all__ = [
    "Sensor",
    "StreamingSensor",
    "OnDemandSensor",
    "RobotSensor",
    "GelSightSensor",
    "OrbbecSensor",
]
