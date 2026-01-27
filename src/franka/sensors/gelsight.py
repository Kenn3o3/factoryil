"""GelSight Mini tactile camera sensor implementation."""

import sys
from pathlib import Path
from typing import Optional

# Support running this file directly, e.g. `python sensors/gelsight.py`.
# When run that way, Python sets sys.path[0] to the `sensors/` directory,
# so the project root (containing `sensors/`, `core/`, etc.) is not importable.
if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from sensors.base import StreamingSensor
from core import GelSightConfig, CameraFrame
from streaming import CameraStream, StreamedFrame
from utils.paths import get_gsrobotics_path


class GelSightSensor(StreamingSensor):
    """GelSight Mini tactile camera sensor."""

    def __init__(self, config: GelSightConfig):
        super().__init__("gelsight")
        self.config = config
        self._camera = None
        self._stream: Optional[CameraStream] = None

    def initialize(self) -> None:
        """Initialize GelSight Mini camera."""
        # Add gsrobotics to path
        gs_path = get_gsrobotics_path()
        if gs_path.exists() and str(gs_path) not in sys.path:
            sys.path.insert(0, str(gs_path))

        from utilities.gelsightmini import GelSightMini

        print(f"[{self.name}] Initializing...")
        cam = GelSightMini(
            target_width=self.config.target_width,
            target_height=self.config.target_height,
            border_fraction=self.config.border_fraction,
        )

        # Select device
        devices = cam.get_device_list()
        if not devices:
            raise RuntimeError("No GelSight Mini devices found")

        device_idx = self.config.device_index
        if device_idx not in devices:
            raise RuntimeError(
                f"Device {device_idx} not found. Available: {list(devices.keys())}"
            )

        print(f"[{self.name}] Using device {device_idx}")
        cam.select_device(device_idx=device_idx)
        cam.start()

        self._camera = cam

    def start_stream(self) -> None:
        """Start background frame grabbing."""
        if self._camera is None:
            raise RuntimeError("Camera not initialized")

        def grab_frame():
            frame = self._camera.camera.read_frame()
            if frame is None or frame.shape[0] == 0:
                raise RuntimeError("Failed to capture frame")
            return frame

        self._stream = CameraStream(
            name=self.name,
            grab_func=grab_frame,
            buffer_size=self.config.buffer_size,
            warmup_frames=self.config.warmup_frames,
        )
        self._stream.start()

    def stop_stream(self) -> None:
        """Stop background frame grabbing."""
        if self._stream is not None:
            self._stream.stop()

    def wait_ready(self, timeout: float = 10.0) -> bool:
        """Wait for stream to be ready."""
        if self._stream is None:
            return False
        return self._stream.wait_ready(timeout=timeout)

    def get_frame(self, target_ns: int, strategy: str = "closest") -> Optional[CameraFrame]:
        """
        Get frame at target timestamp.

        Args:
            target_ns: Target timestamp (monotonic)
            strategy: Frame selection strategy

        Returns:
            CameraFrame or None if no suitable frame found
        """
        if self._stream is None:
            raise RuntimeError("Stream not started")

        streamed_frame = self._stream.get_frame(
            target_ns=target_ns,
            strategy=strategy,
            max_age_ns=int(100 * 1e6),  # 100ms max age
        )

        if streamed_frame is None:
            return None

        return CameraFrame(
            image=streamed_frame.data,
            timestamp_ns=streamed_frame.timestamp_ns,
            sequence=streamed_frame.sequence,
        )

    def shutdown(self) -> None:
        """Shutdown camera."""
        self.stop_stream()
        if self._camera is not None:
            try:
                if hasattr(self._camera, "camera") and self._camera.camera is not None:
                    self._camera.camera.release()
            except Exception as e:
                print(f"[{self.name}] Error during cleanup: {e}")
            self._camera = None


if __name__ == "__main__":
    """Test script to capture 10 frames and save to sensors/test folder."""
    import os
    import time
    import numpy as np
    from pathlib import Path
    import cv2

    # Create test directory
    test_dir = Path(__file__).parent / "test"
    test_dir.mkdir(exist_ok=True)

    print("Initializing GelSight sensor...")
    config = GelSightConfig()
    sensor = GelSightSensor(config)

    try:
        sensor.initialize()
        sensor.start_stream()

        # Wait for stream to be ready
        if not sensor.wait_ready(timeout=10.0):
            print("Error: Stream failed to become ready")
            exit(1)

        print("Stream ready. Capturing 10 frames...")

        for i in range(10):
            # Get current timestamp
            target_ns = time.monotonic_ns()
            frame = sensor.get_frame(target_ns=target_ns, strategy="closest")

            if frame is None:
                print(f"Warning: Frame {i} is None, retrying...")
                time.sleep(0.1)
                continue

            # Save image
            image_path = test_dir / f"gelsight_{i:03d}.png"
            img = frame.image
            if img.dtype != np.uint8:
                img = np.clip(img, 0, 255).astype(np.uint8)

            cv2.imwrite(str(image_path), img)
            print(f"Saved frame {i} to {image_path}")

            time.sleep(0.1)  # Small delay between captures

        print(f"\nSuccessfully captured 10 frames to {test_dir}")

    finally:
        sensor.shutdown()
        print("Sensor shutdown complete")
