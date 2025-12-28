#!/usr/bin/env bash
set -euo pipefail

usage() {
	cat <<'EOF'
Usage:
  batch_episode_to_videos.sh -i EPISODES_DIR -o OUTPUT_DIR [--height H] [--fps F] [--cmap C] [--conda-env NAME]

Converts each subfolder named episodeXX under EPISODES_DIR to a video using
factoryil.tools.episode_to_video, writing OUTPUT_DIR/resultXX.mp4.

Examples:
  batch_episode_to_videos.sh \
    -i ./data/debug_expert \
    -o ./data/debug_expert/videos \
    --height 720 --fps 10
EOF
}

input_dir=""
out_dir=""
height="720"
fps="10"
cmap="gray"
conda_env="env_isaaclab"

while [[ $# -gt 0 ]]; do
	case "$1" in
		-i|--input)
			input_dir="${2:-}"; shift 2;;
		-o|--outdir|--output)
			out_dir="${2:-}"; shift 2;;
		--height)
			height="${2:-}"; shift 2;;
		--fps)
			fps="${2:-}"; shift 2;;
		--cmap)
			cmap="${2:-}"; shift 2;;
		--conda-env)
			conda_env="${2:-}"; shift 2;;
		-h|--help)
			usage; exit 0;;
		*)
			echo "Unknown argument: $1" >&2
			usage
			exit 2;;
	esac
done

if [[ -z "$input_dir" || -z "$out_dir" ]]; then
	echo "Error: both -i/--input and -o/--outdir are required." >&2
	usage
	exit 2
fi

if [[ ! -d "$input_dir" ]]; then
	echo "Input directory not found: $input_dir" >&2
	exit 1
fi

mkdir -p "$out_dir"

# Ensure we run from repository root so `python -m factoryil....` resolves
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../../.." && pwd)"
cd "$repo_root"

# Activate requested conda environment (default: env_isaaclab)
if command -v conda >/dev/null 2>&1; then
	eval "$(conda shell.bash hook)"
elif [[ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]]; then
	# Fallback for common local installs
	# shellcheck disable=SC1091
	source "$HOME/miniconda3/etc/profile.d/conda.sh"
elif [[ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]]; then
	# shellcheck disable=SC1091
	source "$HOME/anaconda3/etc/profile.d/conda.sh"
else
	echo "Conda not found. Please install conda or add it to PATH." >&2
	exit 1
fi
conda activate "$conda_env"

# Collect episode directories and version-sort them (episode0, episode1, episode10, ...)
shopt -s nullglob
episodes=( "$input_dir"/episode* )
if (( ${#episodes[@]} == 0 )); then
	echo "No subdirectories matching 'episode*' found in: $input_dir" >&2
	exit 1
fi
IFS=$'\n' episodes_sorted=( $(printf '%s\n' "${episodes[@]}" | sort -V) )
unset IFS

# Determine zero-padding width from the numeric suffix if present (fallback to width based on count)
pad_width=0
for ep in "${episodes_sorted[@]}"; do
	name="$(basename "$ep")"
	if [[ "$name" =~ episode([0-9]+)$ ]]; then
		num_part="${BASH_REMATCH[1]}"
		if (( ${#num_part} > pad_width )); then
			pad_width=${#num_part}
		fi
	fi
done
if (( pad_width == 0 )); then
	count=${#episodes_sorted[@]}
	max_index=$((count - 1))
	# length of decimal representation
	pad_width=${#max_index}
	(( pad_width == 0 )) && pad_width=1
fi

echo "[info] Found ${#episodes_sorted[@]} episode folders under: $input_dir"

seq_idx=0
for ep in "${episodes_sorted[@]}"; do
	name="$(basename "$ep")"
	if [[ "$name" =~ episode([0-9]+)$ ]]; then
		num=$((10#${BASH_REMATCH[1]}))
	else
		num=$seq_idx
	fi
	out_name=$(printf "result%0*d.mp4" "$pad_width" "$num")
	out_path="$out_dir/$out_name"
	echo "[*] Processing: $ep -> $out_path"
	if ! python -m factoryil.tools.episode_to_video \
		--episode_dir "$ep" \
		--out "$out_path" \
		--height "$height" \
		--fps "$fps" \
		--cmap "$cmap"; then
		echo "[warn] Failed to render: $ep (skipping and continuing)" >&2
		continue
	fi
	((++seq_idx))
done

echo "[done] Wrote ${#episodes_sorted[@]} videos to: $out_dir"


