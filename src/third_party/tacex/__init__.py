"""
Python module for simulating GelSight sensors inside Isaac Sim/Lab
"""

from .gelsight_sensor import GelSightSensor
from .gelsight_sensor_cfg import GelSightSensorCfg
from .gelsight_sensor_data import GelSightSensorData

# Register UI extensions only when available (headless runs may not ship omni.ui).
try:
    from .ui_extension_example import UsdrtExamplePythonExtension
    _HAS_UI_EXT = True
except Exception:
    UsdrtExamplePythonExtension = None
    _HAS_UI_EXT = False

__all__ = ["GelSightSensor", "GelSightSensorCfg", "GelSightSensorData"]
if _HAS_UI_EXT:
    __all__.append("UsdrtExamplePythonExtension")
