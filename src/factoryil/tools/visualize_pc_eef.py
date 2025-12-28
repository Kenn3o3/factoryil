import argparse
import os
import csv
import glob
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import json

def _sorted_frame_paths(folder: str, exts: tuple[str, ...]) -> list[str]:
	paths: list[str] = []
	for ext in exts:
		paths.extend(glob.glob(os.path.join(folder, f"*.{ext}")))
	def key_fn(p: str) -> int:
		stem = os.path.splitext(os.path.basename(p))[0]
		try:
			return int(stem)
		except Exception:
			return int(''.join(ch for ch in stem if ch.isdigit()) or 0)
	return sorted(paths, key=key_fn)


def _load_eef_positions(csv_path: str) -> dict[int, np.ndarray]:
	frame_to_eef = {}
	if not os.path.exists(csv_path):
		return frame_to_eef
	with open(csv_path, "r", newline="") as f:
		reader = csv.DictReader(f)
		for row in reader:
			try:
				frame_idx = int(row.get("frame", "").strip())
			except Exception:
				continue
			eef_field = row.get("eef_pose_w", "")
			if not eef_field:
				continue
			try:
				parts = [float(x) for x in eef_field.split(";") if x != ""]
			except Exception:
				continue
			if len(parts) >= 3:
				frame_to_eef[frame_idx] = np.array(parts[:3], dtype=np.float32)
	return frame_to_eef

def _stem_to_int(path: str) -> int:
	stem = os.path.splitext(os.path.basename(path))[0]
	try:
		return int(stem)
	except Exception:
		return int(''.join(ch for ch in stem if ch.isdigit()) or 0)

def _load_points_for_frame(folder: str, frame_idx: int) -> np.ndarray | None:
	path = os.path.join(folder, f"{frame_idx:04d}.npy")
	if not os.path.exists(path):
		# Try any name with this index
		cands = [p for p in glob.glob(os.path.join(folder, "*.npy")) if _stem_to_int(p) == frame_idx]
		if not cands:
			return None
		path = cands[0]
	try:
		pc = np.load(path).astype(np.float32)
		if pc.ndim == 2 and pc.shape[1] == 3:
			return pc
	except Exception:
		return None
	return None

# Default: auto-discover camera_params.json near the provided episode directory.
# (The collector writes it to the dataset root, i.e. one directory above episodeXX/.)
DEFAULT_CAMERA_PARAMS_PATH = None

def _auto_find_camera_params(episode_dir: str) -> str | None:
	"""Best-effort locate `camera_params.json` for an episode.

	The collector (`factoryil.runner`) writes camera_params.json to the dataset root:
	  - <data_root>/camera_params.json for successful episodes
	  - <data_root>/FAILED/camera_params.json for failed episodes
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

def _load_env_id(episode_dir: str) -> int | None:
	path = os.path.join(episode_dir, "env_id.txt")
	if not os.path.exists(path):
		return None
	try:
		with open(path, "r", encoding="utf-8") as f:
			return int(f.read().strip())
	except Exception:
		return None

def _load_env_origin(episode_dir: str, camera_params_path: str | None) -> np.ndarray:
	# 1) Prefer per-episode origin file
	local_path = os.path.join(episode_dir, "env_origin.txt")
	if os.path.exists(local_path):
		try:
			txt = open(local_path, "r", encoding="utf-8").read().strip().split()
			if len(txt) >= 3:
				return np.asarray([float(txt[0]), float(txt[1]), float(txt[2])], dtype=np.float64)
		except Exception:
			pass
	# 2) Fallback to global camera params (may be shared across envs)
	camera_params_path = camera_params_path or _auto_find_camera_params(episode_dir)
	if camera_params_path is None or (not os.path.exists(camera_params_path)):
		return np.zeros((3,), dtype=np.float64)
	env_id = _load_env_id(episode_dir)
	try:
		with open(camera_params_path, "r", encoding="utf-8") as f:
			meta = json.load(f)
	except Exception:
		return np.zeros((3,), dtype=np.float64)
	origins = meta.get("env_origins", None)
	if origins is None:
		return np.zeros((3,), dtype=np.float64)
	# Select per-env or shared
	if isinstance(origins, list) and len(origins) > 0:
		first = origins[0]
		if isinstance(first, (list, tuple)):
			if env_id is not None and env_id < len(origins):
				return np.asarray(origins[env_id], dtype=np.float64)
			if len(origins) == 1:
				return np.asarray(origins[0], dtype=np.float64)
		return np.asarray(origins, dtype=np.float64)
	return np.asarray(origins, dtype=np.float64)

def main():
	parser = argparse.ArgumentParser("Visualize 3D world + objects point clouds with EEF")
	parser.add_argument("--episode_dir", type=str, required=True, help="Path to episodeXX folder")
	parser.add_argument("--show_world", action="store_true", help="Show world point cloud")
	parser.add_argument("--show_objects", action="store_true", help="Show objects (hole+peg) point cloud")
	parser.add_argument("--max_draw_world", type=int, default=200000, help="Max points to draw for world")
	parser.add_argument("--max_draw_objects", type=int, default=80000, help="Max points to draw for objects")
	parser.add_argument(
		"--camera_params",
		type=str,
		default=DEFAULT_CAMERA_PARAMS_PATH,
		help=(
			"Optional path to camera_params.json used for env_origin fallback. "
			"If omitted, we auto-detect it next to the dataset root (one/two directories above episode_dir)."
		),
	)
	args = parser.parse_args()

	# Defaults: if nothing specified, show both world and objects
	show_world = bool(args.show_world or (not args.show_world and not args.show_objects))
	show_objects = bool(args.show_objects or (not args.show_world and not args.show_objects))

	pc_world_dir = os.path.join(args.episode_dir, "pc_world")
	pc_hole_dir = os.path.join(args.episode_dir, "pc_hole")
	pc_peg_dir = os.path.join(args.episode_dir, "pc_peg")

	eef_map = _load_eef_positions(os.path.join(args.episode_dir, "timestamps_robot.csv"))
	env_origin = _load_env_origin(args.episode_dir, args.camera_params)  # EEF in data is env-local; shift to world

	# Build frame index list from available PC files (union)
	index_set = set()
	for folder in (pc_world_dir, pc_hole_dir, pc_peg_dir):
		print("checking folder: ", folder)
		if os.path.isdir(folder):
			paths = glob.glob(os.path.join(folder, "*.npy"))
			for p in paths:
				index_set.add(_stem_to_int(p))
	frame_indices = sorted(index_set)
	if len(frame_indices) == 0:
		raise RuntimeError("No point cloud frames found (pc_world/pc_hole/pc_peg empty).")

	# Compute global bounds across frames for consistent view
	min_xyz = np.array([np.inf, np.inf, np.inf], dtype=np.float64)
	max_xyz = np.array([-np.inf, -np.inf, -np.inf], dtype=np.float64)
	def _acc_bounds(pc):
		nonlocal min_xyz, max_xyz
		if pc is None or pc.size == 0:
			return
		min_xyz = np.minimum(min_xyz, np.nanmin(pc, axis=0))
		max_xyz = np.maximum(max_xyz, np.nanmax(pc, axis=0))
	for idx in frame_indices:
		if os.path.isdir(pc_world_dir):
			_acc_bounds(_load_points_for_frame(pc_world_dir, idx))
		if os.path.isdir(pc_hole_dir):
			_acc_bounds(_load_points_for_frame(pc_hole_dir, idx))
		if os.path.isdir(pc_peg_dir):
			_acc_bounds(_load_points_for_frame(pc_peg_dir, idx))
		if idx in eef_map:
			_acc_bounds((eef_map[idx] + env_origin)[None, :])
	# Pad and set cube-like extents
	center = 0.5 * (min_xyz + max_xyz)
	extent = np.maximum(max_xyz - min_xyz, 1e-3)
	max_extent = float(np.max(extent))
	half = 0.55 * max_extent
	min_xyz = center - half
	max_xyz = center + half

	fig = plt.figure("3D PC (world + objects) + EEF")
	ax = fig.add_subplot(111, projection="3d")
	try:
		ax.set_box_aspect((1, 1, 1))  # type: ignore[attr-defined]
	except Exception:
		pass
	plt.subplots_adjust(bottom=0.1, left=0.0, right=1.0, top=0.95)

	state = {"i": 0}

	def draw(i: int):
		ax.cla()
		frame_idx = frame_indices[i]
		ax.set_title(f"Frame {frame_idx}  ({i+1}/{len(frame_indices)})")

		world_xyz = _load_points_for_frame(pc_world_dir, frame_idx) if os.path.isdir(pc_world_dir) else None
		hole_xyz = _load_points_for_frame(pc_hole_dir, frame_idx) if os.path.isdir(pc_hole_dir) else None
		peg_xyz = _load_points_for_frame(pc_peg_dir, frame_idx) if os.path.isdir(pc_peg_dir) else None
		obj_xyz = None
		if hole_xyz is not None and peg_xyz is not None:
			obj_xyz = np.concatenate([hole_xyz, peg_xyz], axis=0)
		elif hole_xyz is not None:
			obj_xyz = hole_xyz
		elif peg_xyz is not None:
			obj_xyz = peg_xyz

		# Draw world first (background)
		if show_world and world_xyz is not None and world_xyz.size > 0:
			if world_xyz.shape[0] > args.max_draw_world:
				idx = np.random.choice(world_xyz.shape[0], size=args.max_draw_world, replace=False)
				world_xyz = world_xyz[idx]
			ax.scatter(world_xyz[:, 0], world_xyz[:, 1], world_xyz[:, 2],
			           s=0.5, c="#8FAAD1", alpha=0.35, depthshade=False)
		# Draw objects on top
		if show_objects and obj_xyz is not None and obj_xyz.size > 0:
			if obj_xyz.shape[0] > args.max_draw_objects:
				idx = np.random.choice(obj_xyz.shape[0], size=args.max_draw_objects, replace=False)
				obj_xyz = obj_xyz[idx]
			ax.scatter(obj_xyz[:, 0], obj_xyz[:, 1], obj_xyz[:, 2],
			           s=1.8, c="#2ECC71", alpha=0.95, depthshade=False)
		# Draw EEF as a red dot
		eef = eef_map.get(frame_idx, None)
		if eef is not None and np.isfinite(eef).all():
			pe = (eef.astype(np.float64) + env_origin)
			ax.scatter([pe[0]], [pe[1]], [pe[2]], s=60, c="#E62D2D", depthshade=True)

		# Axes limits
		ax.set_xlim(min_xyz[0], max_xyz[0])
		ax.set_ylim(min_xyz[1], max_xyz[1])
		ax.set_zlim(min_xyz[2], max_xyz[2])
		ax.set_xlabel("X")
		ax.set_ylabel("Y")
		ax.set_zlabel("Z")
		try:
			ax.set_box_aspect((1, 1, 1))  # type: ignore[attr-defined]
		except Exception:
			pass
		plt.draw()

	def on_key(event):
		if event.key == "right":
			state["i"] = (state["i"] + 1) % len(frame_indices)
			draw(state["i"])
		elif event.key == "left":
			state["i"] = (state["i"] - 1) % len(frame_indices)
			draw(state["i"])

	fig.canvas.mpl_connect("key_press_event", on_key)
	draw(0)
	print("Use left/right arrow keys to step frames. Close the window to exit.")
	plt.show()


if __name__ == "__main__":
	main()

