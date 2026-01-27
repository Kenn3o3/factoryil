"""Orbbec Gemini 335 RGB-D camera sensor implementation."""

import sys
from pathlib import Path
import numpy as np
from typing import Optional

# Support running this file directly, e.g. `python sensors/orbbec.py`.
if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from sensors.base import StreamingSensor
from core import OrbbecConfig, RGBDFrame
from streaming import CameraStream, StreamedFrame
from utils.paths import get_pyorbbecsdk_examples_path


class OrbbecSensor(StreamingSensor):
    """Orbbec Gemini 335 RGB-D camera sensor."""

    def __init__(self, config: OrbbecConfig):
        super().__init__("orbbec")
        self.config = config
        self._pipeline = None
        self._frame_to_bgr = None
        self._stream: Optional[CameraStream] = None

    def initialize(self) -> None:
        """Initialize Orbbec Gemini 335 camera."""
        from pyorbbecsdk import (
            Config,
            OBError,
            OBFormat,
            OBSensorType,
            Pipeline,
            VideoStreamProfile,
        )

        # Import frame conversion utility
        pyorbbec_examples = get_pyorbbecsdk_examples_path()
        if pyorbbec_examples.exists() and str(pyorbbec_examples) not in sys.path:
            sys.path.insert(0, str(pyorbbec_examples))

        import importlib.util
        utils_path = pyorbbec_examples / "utils.py"
        if not utils_path.exists():
            raise RuntimeError(f"Could not find pyorbbecsdk utils.py at {utils_path}")

        spec = importlib.util.spec_from_file_location("pyorbbec_utils", utils_path)
        pyorbbec_utils = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pyorbbec_utils)
        self._frame_to_bgr = pyorbbec_utils.frame_to_bgr_image

        print(f"[{self.name}] Initializing...")
        self._pipeline = Pipeline()

        # Configure streams
        config = Config()
        try:
            # Color stream
            profile_list = self._pipeline.get_stream_profile_list(OBSensorType.COLOR_SENSOR)
            try:
                format_map = {"RGB": OBFormat.RGB, "BGR": OBFormat.BGR}
                ob_format = format_map.get(self.config.color_format, OBFormat.RGB)
                color_profile: VideoStreamProfile = profile_list.get_video_stream_profile(
                    self.config.color_width,
                    self.config.color_height,
                    ob_format,
                    self.config.color_fps,
                )
            except OBError:
                print(f"[{self.name}] Using default color profile")
                color_profile = profile_list.get_default_video_stream_profile()
            config.enable_stream(color_profile)

            # Depth stream
            depth_profile_list = self._pipeline.get_stream_profile_list(OBSensorType.DEPTH_SENSOR)
            depth_profile = depth_profile_list.get_default_video_stream_profile()
            config.enable_stream(depth_profile)

        except Exception as e:
            raise RuntimeError(f"Could not configure streams: {e}")

        print(f"[{self.name}] Starting pipeline...")
        self._pipeline.start(config)

    def start_stream(self) -> None:
        """Start background frame grabbing."""
        if self._pipeline is None:
            raise RuntimeError("Pipeline not initialized")

        def grab_frame():
            frameset = self._pipeline.wait_for_frames(self.config.frame_timeout_ms)
            if frameset is None:
                raise RuntimeError("Timeout waiting for frameset")

            result = {}

            # Get color frame if requested
            if self.config.collect_color:
                color_frame = frameset.get_color_frame()
                if color_frame is None:
                    raise RuntimeError("No color frame")
                color_image = self._frame_to_bgr(color_frame)
                if color_image is None:
                    raise RuntimeError("Failed to convert color frame")
                result["color"] = color_image

            # Get depth frame if requested
            if self.config.collect_depth:
                depth_frame = frameset.get_depth_frame()
                if depth_frame is None:
                    raise RuntimeError("No depth frame")
                depth_data = np.frombuffer(depth_frame.get_data(), dtype=np.uint16)
                depth_image = depth_data.reshape((depth_frame.get_height(), depth_frame.get_width()))
                result["depth"] = depth_image

            return result

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

    def get_frame(self, target_ns: int, strategy: str = "closest") -> Optional[RGBDFrame]:
        """
        Get frame at target timestamp.

        Args:
            target_ns: Target timestamp (monotonic)
            strategy: Frame selection strategy

        Returns:
            RGBDFrame or None if no suitable frame found
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

        return RGBDFrame(
            color=streamed_frame.data.get("color"),
            depth=streamed_frame.data.get("depth"),
            timestamp_ns=streamed_frame.timestamp_ns,
            sequence=streamed_frame.sequence,
        )

    def shutdown(self) -> None:
        """Shutdown camera."""
        self.stop_stream()
        if self._pipeline is not None:
            self._pipeline.stop()
            self._pipeline = None


if __name__ == "__main__":
    """Test script to capture 10 frames and save to sensors/test folder."""
    import time
    from pathlib import Path

    import cv2

    def _try_get_intrinsics_from_obj(obj):
        """Best-effort extraction of pinhole intrinsics from various SDK objects."""
        if obj is None:
            return None

        # Common attribute names
        candidates = {
            "fx": ("fx", "focal_length_x", "f_x"),
            "fy": ("fy", "focal_length_y", "f_y"),
            "cx": ("cx", "principal_point_x", "c_x"),
            "cy": ("cy", "principal_point_y", "c_y"),
            "width": ("width", "w"),
            "height": ("height", "h"),
        }

        out = {}
        for key, names in candidates.items():
            for name in names:
                if hasattr(obj, name):
                    try:
                        out[key] = float(getattr(obj, name))
                        break
                    except Exception:
                        pass

        # Sometimes intrinsics come back as dict-like
        if hasattr(obj, "get"):
            for key in ("fx", "fy", "cx", "cy", "width", "height"):
                if key not in out:
                    try:
                        val = obj.get(key)
                        if val is not None:
                            out[key] = float(val)
                    except Exception:
                        pass

        if all(k in out for k in ("fx", "fy", "cx", "cy")):
            return out
        return None

    def _get_depth_intrinsics(sensor: "OrbbecSensor", depth_image: np.ndarray):
        """Try multiple SDK-specific ways to get depth intrinsics; fallback to approximation."""
        # 1) Some SDK versions expose camera params directly on the pipeline.
        pipeline = getattr(sensor, "_pipeline", None)
        if pipeline is not None:
            for method_name in ("get_camera_param", "get_camera_params", "get_camera_parameters"):
                if hasattr(pipeline, method_name):
                    try:
                        cam_param = getattr(pipeline, method_name)()
                        # Common nesting patterns: cam_param.depth_intrinsic
                        for attr in ("depth_intrinsic", "depthIntrinsic", "depth" ):
                            if hasattr(cam_param, attr):
                                intr = _try_get_intrinsics_from_obj(getattr(cam_param, attr))
                                if intr is not None:
                                    return intr
                        intr = _try_get_intrinsics_from_obj(cam_param)
                        if intr is not None:
                            return intr
                    except Exception:
                        pass

        # 2) Try to get it from a stream profile (if available).
        # We stored no profiles on the class, so this is a best-effort attempt.
        # If the SDK adds profile access later, this will start working.
        try:
            if pipeline is not None and hasattr(pipeline, "get_stream_profile_list"):
                from pyorbbecsdk import OBSensorType  # type: ignore

                depth_profiles = pipeline.get_stream_profile_list(OBSensorType.DEPTH_SENSOR)
                depth_profile = depth_profiles.get_default_video_stream_profile()
                for method_name in (
                    "get_intrinsic",
                    "get_intrinsics",
                    "get_camera_intrinsic",
                    "get_camera_intrinsics",
                ):
                    if hasattr(depth_profile, method_name):
                        intr_obj = getattr(depth_profile, method_name)()
                        intr = _try_get_intrinsics_from_obj(intr_obj)
                        if intr is not None:
                            return intr
        except Exception:
            pass

        # 3) Fallback approximation (good enough for visualization, not metrology).
        h, w = depth_image.shape[:2]
        f = float(max(w, h))
        return {"fx": f, "fy": f, "cx": (w - 1) / 2.0, "cy": (h - 1) / 2.0, "width": w, "height": h}

    def _write_ply_binary(path: Path, points_xyz: np.ndarray, colors_rgb: Optional[np.ndarray] = None) -> None:
        """Write a binary little-endian PLY with optional RGB colors."""
        import struct

        if colors_rgb is not None:
            if colors_rgb.dtype != np.uint8:
                colors_rgb = np.clip(colors_rgb, 0, 255).astype(np.uint8)
            if len(colors_rgb) != len(points_xyz):
                raise ValueError("colors_rgb length must match points")

        points_xyz = np.asarray(points_xyz, dtype=np.float32)
        n = points_xyz.shape[0]

        header_lines = [
            "ply",
            "format binary_little_endian 1.0",
            f"element vertex {n}",
            "property float x",
            "property float y",
            "property float z",
        ]
        if colors_rgb is not None:
            header_lines += [
                "property uchar red",
                "property uchar green",
                "property uchar blue",
            ]
        header_lines.append("end_header")

        with open(path, "wb") as f:
            f.write(("\n".join(header_lines) + "\n").encode("ascii"))
            if colors_rgb is None:
                for x, y, z in points_xyz:
                    f.write(struct.pack("<fff", float(x), float(y), float(z)))
            else:
                for (x, y, z), (r, g, b) in zip(points_xyz, colors_rgb):
                    f.write(struct.pack("<fffBBB", float(x), float(y), float(z), int(r), int(g), int(b)))

    def _save_point_cloud_ply(
        sensor: "OrbbecSensor",
        depth_u16: np.ndarray,
        color_bgr: Optional[np.ndarray],
        out_path: Path,
        depth_scale: float = 1000.0,
        depth_trunc_m: float = 3.0,
        stride: int = 1,
    ) -> None:
        """Save a point cloud from depth (+ optional color) to PLY.

        Assumes `depth_u16` is in millimeters by default (depth_scale=1000).
        """
        intr = _get_depth_intrinsics(sensor, depth_u16)
        fx, fy, cx, cy = intr["fx"], intr["fy"], intr["cx"], intr["cy"]

        try:
            import open3d as o3d  # type: ignore

            depth_o3d = o3d.geometry.Image(depth_u16)
            if color_bgr is not None:
                # Open3D expects RGB
                if color_bgr.shape[:2] != depth_u16.shape[:2]:
                    color_bgr = cv2.resize(color_bgr, (depth_u16.shape[1], depth_u16.shape[0]), interpolation=cv2.INTER_AREA)
                color_rgb = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2RGB)
                color_o3d = o3d.geometry.Image(color_rgb)
                rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
                    color_o3d,
                    depth_o3d,
                    depth_scale=depth_scale,
                    depth_trunc=depth_trunc_m,
                    convert_rgb_to_intensity=False,
                )
                intrinsic = o3d.camera.PinholeCameraIntrinsic(
                    int(depth_u16.shape[1]),
                    int(depth_u16.shape[0]),
                    float(fx),
                    float(fy),
                    float(cx),
                    float(cy),
                )
                pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)
            else:
                intrinsic = o3d.camera.PinholeCameraIntrinsic(
                    int(depth_u16.shape[1]),
                    int(depth_u16.shape[0]),
                    float(fx),
                    float(fy),
                    float(cx),
                    float(cy),
                )
                pcd = o3d.geometry.PointCloud.create_from_depth_image(
                    depth_o3d,
                    intrinsic,
                    depth_scale=depth_scale,
                    depth_trunc=depth_trunc_m,
                    stride=stride,
                )

            if not o3d.io.write_point_cloud(str(out_path), pcd, write_ascii=False, compressed=True):
                raise RuntimeError(f"Open3D failed to write PLY: {out_path}")
            return

        except ImportError:
            # Fallback: numpy projection + minimal binary PLY writer.
            pass

        depth_m = depth_u16.astype(np.float32) / float(depth_scale)
        h, w = depth_m.shape[:2]
        u = np.arange(0, w, stride, dtype=np.float32)
        v = np.arange(0, h, stride, dtype=np.float32)
        uu, vv = np.meshgrid(u, v)
        zz = depth_m[::stride, ::stride]

        valid = (zz > 0) & (zz < depth_trunc_m)
        if not np.any(valid):
            raise RuntimeError("No valid depth pixels for point cloud")

        z = zz[valid]
        x = (uu[valid] - float(cx)) * z / float(fx)
        y = (vv[valid] - float(cy)) * z / float(fy)
        points = np.stack([x, y, z], axis=1)

        colors_rgb: Optional[np.ndarray] = None
        if color_bgr is not None:
            if color_bgr.shape[:2] != (h, w):
                color_bgr = cv2.resize(color_bgr, (w, h), interpolation=cv2.INTER_AREA)
            color_rgb_full = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2RGB)
            colors_rgb = color_rgb_full[::stride, ::stride][valid]

        _write_ply_binary(out_path, points_xyz=points, colors_rgb=colors_rgb)

    # Create test directory
    test_dir = Path(__file__).parent / "test"
    test_dir.mkdir(exist_ok=True)

    print("Initializing Orbbec sensor...")
    config = OrbbecConfig()
    sensor = OrbbecSensor(config)

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

            # Save color image if available
            if frame.color is not None:
                color_path = test_dir / f"orbbec_color_{i:03d}.png"
                color_bgr = frame.color
                if color_bgr.dtype != np.uint8:
                    color_bgr = np.clip(color_bgr, 0, 255).astype(np.uint8)
                if not cv2.imwrite(str(color_path), color_bgr, [cv2.IMWRITE_PNG_COMPRESSION, 3]):
                    raise RuntimeError(f"Failed to write PNG: {color_path}")
                print(f"Saved color frame {i} to {color_path}")

            # Save depth image if available
            if frame.depth is not None:
                depth_path = test_dir / f"orbbec_depth_{i:03d}.npy"
                np.save(depth_path, frame.depth)
                print(f"Saved depth frame {i} to {depth_path}")

            # Save point cloud (PLY) if depth is available
            if frame.depth is not None:
                ply_path = test_dir / f"orbbec_cloud_{i:03d}.ply"
                try:
                    _save_point_cloud_ply(
                        sensor=sensor,
                        depth_u16=frame.depth,
                        color_bgr=frame.color,
                        out_path=ply_path,
                        depth_scale=1000.0,  # assumes depth in millimeters
                        depth_trunc_m=3.0,
                        stride=2,
                    )
                    print(f"Saved point cloud {i} to {ply_path}")
                except Exception as e:
                    print(f"Warning: Failed to save point cloud {i}: {e}")

            time.sleep(0.1)  # Small delay between captures

        print(f"\nSuccessfully captured 10 frames to {test_dir}")

    finally:
        sensor.shutdown()
        print("Sensor shutdown complete")