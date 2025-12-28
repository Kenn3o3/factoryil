import argparse
import os
import math
import glob
import json
import numpy as np
import csv
from typing import List, Tuple, Optional

from PIL import Image, ImageDraw
import imageio.v2 as imageio
try:
	import matplotlib.cm as mplcm  # optional, for colored depth
except Exception:
	mplcm = None

# Default: auto-discover camera_params.json near the provided episode directory.
# (The collector writes it to the dataset root, i.e. one directory above episodeXX/.)
DEFAULT_CAMERA_PARAMS_PATH = None

def _auto_find_camera_params(episode_dir: str) -> Optional[str]:
	"""Best-effort locate `camera_params.json` for an episode.

	The collector (`factoryil.runner`) writes camera_params.json to the dataset root:
	  - <data_root>/camera_params.json for successful episodes
	  - <data_root>/FAILED/camera_params.json for failed episodes

	By default we search near the provided episode directory.
	"""
	ep = os.path.abspath(episode_dir)
	candidates = [
		os.path.join(ep, "camera_params.json"),
		os.path.join(os.path.dirname(ep), "camera_params.json"),
		os.path.join(os.path.dirname(os.path.dirname(ep)), "camera_params.json"),
	]
	for p in candidates:
		if p and os.path.exists(p):
			return p
	return None


def _sorted_frame_paths(folder: str, exts: Tuple[str, ...]) -> List[str]:
	paths: List[str] = []
	for ext in exts:
		paths.extend(glob.glob(os.path.join(folder, f"*.{ext}")))
	def key_fn(p: str) -> int:
		stem = os.path.splitext(os.path.basename(p))[0]
		try:
			return int(stem)
		except Exception:
			# Fallback to lexicographic if no numeric stem
			return int(''.join(ch for ch in stem if ch.isdigit()) or 0)
	return sorted(paths, key=key_fn)

def _stem_to_int(path: str) -> int:
	"""Best-effort numeric index from filename stem (e.g., 0007.png -> 7)."""
	stem = os.path.splitext(os.path.basename(path))[0]
	try:
		return int(stem)
	except Exception:
		return int(''.join(ch for ch in stem if ch.isdigit()) or 0)

def _quat_wxyz_to_matrix(quat: List[float]) -> np.ndarray:
	"""Convert (w, x, y, z) quaternion into a 3x3 rotation matrix."""
	if len(quat) != 4:
		return np.eye(3, dtype=np.float64)
	w, x, y, z = quat
	norm = math.sqrt(w * w + x * x + y * y + z * z)
	if norm < 1e-8:
		return np.eye(3, dtype=np.float64)
	w /= norm
	x /= norm
	y /= norm
	z /= norm
	return np.array([
		[w * w + x * x - y * y - z * z, 2.0 * (x * y - w * z), 2.0 * (x * z + w * y)],
		[2.0 * (x * y + w * z), w * w - x * x + y * y - z * z, 2.0 * (y * z - w * x)],
		[2.0 * (x * z - w * y), 2.0 * (y * z + w * x), w * w - x * x - y * y + z * z],
	], dtype=np.float64)


class EEFProjector:
	"""Projects end-effector poses into camera pixel coordinates."""

	def __init__(self, metadata: dict, env_id: int):
		self._valid = False
		self.env_id = env_id
		self.width = None
		self.height = None
		self.K = None
		self.R_wc = None
		self.cam_pos = None
		self.env_origin = None

		env_origins = metadata.get("env_origins")
		camera = metadata.get("camera", {})
		if not isinstance(env_origins, list) or not camera:
			return

		self.env_origin = self._select_vector(env_origins)
		pos_list = camera.get("pos_w")
		quat_ros_list = camera.get("quat_w_ros")
		intr_list = camera.get("intrinsic_matrices")
		image_shape = camera.get("image_shape")

		if self.env_origin is None or pos_list is None or quat_ros_list is None or intr_list is None or image_shape is None:
			return

		self.cam_pos = self._to_numpy(self._select_vector(pos_list))
		quat_ros = self._select_vector(quat_ros_list)
		self.K = self._to_numpy(self._select_matrix(intr_list))

		if self.cam_pos is None or quat_ros is None or self.K is None:
			return

		self.env_origin = self._to_numpy(self.env_origin)
		self.width = int(image_shape[1])
		self.height = int(image_shape[0])
		self.R_wc = _quat_wxyz_to_matrix(quat_ros).T  # world->camera rotation

		if self.env_origin is None or self.R_wc is None or self.cam_pos is None or self.K is None:
			return

		self._valid = True

	def _to_numpy(self, value):
		if value is None:
			return None
		arr = np.asarray(value, dtype=np.float64)
		return arr

	def _select_vector(self, values):
		if values is None:
			return None
		if isinstance(values, (list, tuple)):
			if len(values) == 0:
				return None
			first = values[0]
			if isinstance(first, (list, tuple)):
				# List of per-env vectors
				if self.env_id < len(values):
					return values[self.env_id]
				if len(values) == 1:
					return values[0]
				return None
			# Single vector shared by all envs
			return values
		return values

	def _select_matrix(self, values):
		if values is None:
			return None
		if isinstance(values, (list, tuple)):
			if len(values) == 0:
				return None
			first = values[0]
			if isinstance(first, (list, tuple)):
				# Either a matrix (list of rows) or list of per-env matrices
				if len(first) > 0 and isinstance(first[0], (list, tuple)):
					# Per-env matrices
					if self.env_id < len(values):
						return values[self.env_id]
					if len(values) == 1:
						return values[0]
					return None
				# Single matrix (rows of numbers)
				return values
		return values

	def is_valid(self) -> bool:
		return self._valid

	def project(self, eef_pose: List[float]) -> Optional[Tuple[float, float]]:
		if not self._valid or eef_pose is None or len(eef_pose) < 3:
			return None
		point_local = np.asarray(eef_pose[:3], dtype=np.float64)
		if point_local.shape != (3,):
			return None
		point_world = point_local + self.env_origin
		relative = point_world - self.cam_pos
		point_camera = self.R_wc @ relative
		z = float(point_camera[2])
		if not np.isfinite(z) or z <= 1e-6:
			return None
		pixel_h = self.K @ point_camera
		u = float(pixel_h[0] / z)
		v = float(pixel_h[1] / z)
		if not (np.isfinite(u) and np.isfinite(v)):
			return None
		if u < 0 or v < 0 or u >= self.width or v >= self.height:
			return None
		return (u, v)


def _load_episode_csv(episode_dir: str):
	"""
	Load per-frame data from timestamps_robot.csv.
	Returns:
	- frame_to_action: dict[int, Tuple[float, float, float]]  (dx, dy, dz)
	- yz_scale: float, robust max scale for Y/Z components (95th percentile of max(|y|,|z|))
	- frame_to_eef_pose: dict[int, List[float]] end-effector pose values (pos + orientation)
	"""
	csv_path = os.path.join(episode_dir, "timestamps_robot.csv")
	if not os.path.exists(csv_path):
		return {}, 1.0, {}
	frame_to_action = {}
	frame_to_eef = {}
	yz_vals = []
	try:
		with open(csv_path, "r", newline="") as f:
			reader = csv.DictReader(f)
			for row in reader:
				try:
					frame_idx = int(row.get("frame", "").strip())
				except Exception:
					continue
				action_field = row.get("action", "")
				if not action_field:
					continue
				try:
					parts = [float(x) for x in action_field.split(";") if x != ""]
				except Exception:
					continue
				if len(parts) < 3:
					continue
				dx, dy, dz = parts[0], parts[1], parts[2]
				frame_to_action[frame_idx] = (dx, dy, dz)
				yz_vals.append(max(abs(dy), abs(dz)))
				eef_field = row.get("eef_pose_w", "")
				if eef_field:
					try:
						eef_parts = [float(x) for x in eef_field.split(";") if x != ""]
						if len(eef_parts) >= 3:
							frame_to_eef[frame_idx] = eef_parts
					except Exception:
						pass
	except Exception:
		# If parsing fails, fall back gracefully
		return {}, 1.0, {}
	if len(yz_vals) == 0:
		return frame_to_action, 1.0, frame_to_eef
	yz_scale = float(np.percentile(np.asarray(yz_vals, dtype=np.float32), 95))
	if not np.isfinite(yz_scale) or yz_scale <= 1e-8:
		yz_scale = 1.0
	return frame_to_action, yz_scale, frame_to_eef


def _load_env_id(episode_dir: str) -> Optional[int]:
	env_id_path = os.path.join(episode_dir, "env_id.txt")
	if not os.path.exists(env_id_path):
		return None
	try:
		with open(env_id_path, "r", encoding="utf-8") as f:
			return int(f.read().strip())
	except Exception:
		return None


def _build_projector(episode_dir: str, camera_params_path: str | None = None) -> Optional[EEFProjector]:
	env_id = _load_env_id(episode_dir)
	if env_id is None:
		return None
	meta_path = camera_params_path or _auto_find_camera_params(episode_dir) or DEFAULT_CAMERA_PARAMS_PATH
	if not meta_path or not os.path.exists(meta_path):
		return None
	try:
		with open(meta_path, "r", encoding="utf-8") as f:
			metadata = json.load(f)
	except Exception:
		return None
	projector = EEFProjector(metadata, env_id)
	if projector.is_valid():
		return projector
	return None

def _draw_border(img: Image.Image, rect: Tuple[int, int, int, int], color=(50, 110, 180), width: int = 4):
	draw = ImageDraw.Draw(img)
	for i in range(width):
		r = (rect[0] + i, rect[1] + i, rect[2] - i, rect[3] - i)
		draw.rectangle(r, outline=color)


def compose_frame(
	depth_img: Image.Image,
	rgb_img: Image.Image,
	tl_img: Image.Image,
	tr_img: Image.Image,
	out_h: int,
	border: int = 8,
	gap: int = 10,
	action_vec_yz: Tuple[float, float] | None = None,
	action_scale: float = 1.0,
) -> Image.Image:
	# Scale main panels to out_h
	def scale_to_h(im: Image.Image, H: int) -> Image.Image:
		w, h = im.size
		if h == 0:
			return im
		new_w = max(1, int(round(w * (H / float(h)))))
		return im.resize((new_w, H), Image.BILINEAR)

	d_img = scale_to_h(depth_img, out_h)
	r_img = scale_to_h(rgb_img, out_h)

	# Canvas size
	canvas_w = d_img.size[0] + r_img.size[0] + 3 * border
	canvas_h = out_h + 2 * border
	canvas = Image.new("RGB", (canvas_w, canvas_h), (240, 200, 170))  # light background

	# Paste main panels
	x0 = border
	y0 = border
	canvas.paste(d_img, (x0, y0))
	_draw_border(canvas, (x0, y0, x0 + d_img.size[0], y0 + d_img.size[1]))

	x1 = x0 + d_img.size[0] + border
	canvas.paste(r_img, (x1, y0))
	_draw_border(canvas, (x1, y0, x1 + r_img.size[0], y0 + r_img.size[1]))

	# Place tactile thumbnails at bottom-right inside the right panel
	# Compute thumb size as 22% of right panel height
	thumb_h = max(24, int(out_h * 0.22))
	thumb_w = thumb_h  # square
	def prep_thumb(im: Image.Image) -> Image.Image:
		return im.resize((thumb_w, thumb_h), Image.BILINEAR)

	tl = prep_thumb(tl_img)
	tr = prep_thumb(tr_img)

	tx2 = x1 + r_img.size[0] - border - thumb_w
	ty = y0 + r_img.size[1] - border - thumb_h
	tx1 = tx2 - gap - thumb_w
	tx0 = tx1 - gap - thumb_w

	canvas.paste(tl, (tx1, ty))
	_draw_border(canvas, (tx1, ty, tx1 + thumb_w, ty + thumb_h))
	canvas.paste(tr, (tx2, ty))
	_draw_border(canvas, (tx2, ty, tx2 + thumb_w, ty + thumb_h))

	# Optional: Action Y/Z indicator box to the left of tactile thumbs
	if action_vec_yz is not None:
		def render_action_box(size: int, vec_yz: Tuple[float, float], scale: float) -> Image.Image:
			bg = (252, 250, 245)
			img = Image.new("RGB", (size, size), bg)
			dr = ImageDraw.Draw(img)
			cx, cy = size // 2, size // 2
			# Axes
			axis_col = (120, 120, 120)
			dr.line([(0, cy), (size, cy)], fill=axis_col, width=1)
			dr.line([(cx, 0), (cx, size)], fill=axis_col, width=1)
			# Labels: Up = +Z, Down = -Z, Right = +Y, Left = -Y
			try:
				dr.text((cx + int(size*0.32), cy - 10), "Y", fill=(20, 20, 20))
				dr.text((cx - 6, int(size*0.05)), "Z", fill=(20, 20, 20))
				dr.text((2, cy - 10), "-Y", fill=(20, 20, 20))
				dr.text((cx - 10, size - 14), "-Z", fill=(20, 20, 20))
			except Exception:
				pass
			# Arrow for action (y, z)
			yv, zv = float(vec_yz[0]), float(vec_yz[1])
			if not np.isfinite(yv):
				yv = 0.0
			if not np.isfinite(zv):
				zv = 0.0
			s = scale if (isinstance(scale, (int, float)) and scale > 1e-8 and np.isfinite(scale)) else 1.0
			# Convert to pixels; note: +Z is up (negative screen y)
			radius = int(size * 0.40)
			vx = int(round((yv / s) * radius))
			vy = int(round((-zv / s) * radius))
			end = (cx + vx, cy + vy)
			col = (210, 60, 60)
			width = max(2, int(size * 0.06))
			dr.line([(cx, cy), end], fill=col, width=width)
			# Arrow head
			angle = math.atan2(vy, vx) if (vx != 0 or vy != 0) else 0.0
			head_len = max(6, int(size * 0.18))
			head_ang = math.radians(24)
			p1 = (end[0] - int(head_len * math.cos(angle - head_ang)),
			      end[1] - int(head_len * math.sin(angle - head_ang)))
			p2 = (end[0] - int(head_len * math.cos(angle + head_ang)),
			      end[1] - int(head_len * math.sin(angle + head_ang)))
			dr.polygon([end, p1, p2], fill=col)
			return img

		act_img = render_action_box(thumb_w, action_vec_yz, action_scale)
		canvas.paste(act_img, (tx0, ty))
		_draw_border(canvas, (tx0, ty, tx0 + thumb_w, ty + thumb_h))

	return canvas


def main():
	parser = argparse.ArgumentParser("Convert a collected episode folder to a composite video")
	parser.add_argument("--episode_dir", type=str, required=True, help="Path to episode folder")
	parser.add_argument("--out", type=str, default="result.mp4", help="Output video path")
	parser.add_argument("--height", type=int, default=720, help="Output video height (pixels) for main panels")
	parser.add_argument("--fps", type=int, default=10, help="Frames per second")
	parser.add_argument("--cmap", type=str, default="gray",
	                    help="Colormap for depth (e.g., gray, viridis, magma, plasma, inferno, turbo, jet).")
	parser.add_argument(
		"--camera_params",
		type=str,
		default=DEFAULT_CAMERA_PARAMS_PATH,
		help=(
			"Optional path to camera_params.json used for EEF projection. "
			"If omitted, we auto-detect it next to the dataset root (one/two directories above episode_dir)."
		),
	)
	args = parser.parse_args()

	ep = args.episode_dir
	rgb_paths = _sorted_frame_paths(os.path.join(ep, "rgb_cam"), ("png", "jpg", "jpeg"))
	# Prefer PNG depth saved by the collector; fallback to raw .npy
	depth_paths = _sorted_frame_paths(os.path.join(ep, "depth_cam"), ("png",))
	tl_paths = _sorted_frame_paths(os.path.join(ep, "rgb_tactile_left"), ("png", "jpg", "jpeg"))
	tr_paths = _sorted_frame_paths(os.path.join(ep, "rgb_tactile_right"), ("png", "jpg", "jpeg"))

	# Load actions for Y/Z arrow visualization
	frame_to_action, yz_scale, frame_to_eef = _load_episode_csv(ep)
	projector = _build_projector(ep, args.camera_params)

	n = min(len(rgb_paths), len(depth_paths), len(tl_paths), len(tr_paths))
	if n == 0:
		raise RuntimeError("No frames found; ensure episode_dir has rgb_cam, depth_cam, rgb_tactile_left/right")

	writer = imageio.get_writer(args.out, fps=args.fps, codec="libx264", quality=8)
	try:
		for i in range(n):
			# Load images
			rgb_img = Image.open(rgb_paths[i]).convert("RGB")
			depth_img = Image.open(depth_paths[i]).convert("RGB")
			tl_img = Image.open(tl_paths[i]).convert("RGB")
			tr_img = Image.open(tr_paths[i]).convert("RGB")
			# Project end-effector position (if available)
			frame_idx = _stem_to_int(rgb_paths[i])
			if projector is not None and frame_idx in frame_to_eef:
				pixel = projector.project(frame_to_eef[frame_idx])
				if pixel is not None:
					u, v = pixel
					# If the video RGB resolution differs from the camera's native
					# resolution used in calibration, rescale pixel coordinates.
					try:
						W0, H0 = float(projector.width), float(projector.height)
						W1, H1 = float(rgb_img.size[0]), float(rgb_img.size[1])
						if W0 > 0 and H0 > 0 and (W0 != W1 or H0 != H1):
							sx = W1 / W0
							sy = H1 / H0
							u *= sx
							v *= sy
					except Exception:
						pass
					draw = ImageDraw.Draw(rgb_img)
					radius = max(4, rgb_img.size[0] // 150)
					draw.ellipse(
						(u - radius, v - radius, u + radius, v + radius),
						fill=(230, 45, 45),
						outline=(0, 0, 0),
						width=2,
					)
			# Determine frame index and action (dy, dz)
			act_yz = None
			if frame_idx in frame_to_action:
				_, dy, dz = frame_to_action[frame_idx]
				act_yz = (dy, dz)
			# Compose
			frame = compose_frame(
				depth_img,
				rgb_img,
				tl_img,
				tr_img,
				out_h=args.height,
				action_vec_yz=act_yz,
				action_scale=yz_scale
			)
			writer.append_data(np.array(frame))
	finally:
		writer.close()
	print(f"[done] wrote {args.out} with {n} frames")

if __name__ == "__main__":
	main()