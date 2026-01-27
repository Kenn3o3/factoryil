#!/usr/bin/env python3
"""
Multi-episode data collection with interactive controls.

Controls:
- Press 'd' + Enter: Start/stop episode recording
- Press 'e' + Enter: Exit (only when not recording)
- Press 'q' + Enter: Quit immediately

Episodes are numbered sequentially (0, 1, 2, ...)
"""

from utils.utils import activate_franka_conda_env
activate_franka_conda_env(__file__)

import sys
import argparse
from pathlib import Path
from datetime import datetime

from core import SystemConfig, DataCollectionSystem


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", type=float, default=10.0, help="Collection rate in Hz")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")
    args = parser.parse_args()

    # Create configuration
    config = SystemConfig(rate_hz=args.rate)

    # You can add multiple Orbbec sensors like this:
    # config.orbbec_sensors = []  # Clear default
    # config.add_orbbec("orbbec_left", collect_color=True, collect_depth=True)
    # config.add_orbbec("orbbec_right", collect_color=True, collect_depth=False)

    # Create system
    system = DataCollectionSystem(config)

    # Output directory
    if args.output_dir:
        base_output_dir = Path(args.output_dir)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_output_dir = Path(__file__).parent / "_out" / f"data_{timestamp}"

    try:
        # Initialize
        print("=" * 70)
        print("INITIALIZATION")
        print("=" * 70)
        system.reset()

        # Multi-episode collection loop
        episode_num = 0
        recording = False

        print("\n" + "=" * 70)
        print("MULTI-EPISODE DATA COLLECTION")
        print("=" * 70)
        print("\nControls:")
        print("  'd' + Enter: Start/stop episode recording")
        print("  'e' + Enter: Exit (when not recording)")
        print("  'q' + Enter: Quit immediately")
        print("\nReady. Press 'd' to start episode 0...")

        while True:
            try:
                inp = input("> ").strip().lower()
            except EOFError:
                break

            if inp == 'q':
                print("\nQuitting...")
                break

            elif inp == 'e':
                if recording:
                    print("Cannot exit while recording. Press 'd' to stop recording first.")
                else:
                    print("\nExiting...")
                    break

            elif inp == 'd':
                if not recording:
                    # Start recording
                    recording = True
                    system.start_episode(episode_num)
                    print(f"\n{'='*70}")
                    print(f"RECORDING EPISODE {episode_num}")
                    print(f"{'='*70}")
                    print(f"Press 'd' to stop recording...")

                else:
                    # Stop recording
                    recording = False
                    print(f"\n{'='*70}")
                    print(f"STOPPING EPISODE {episode_num}")
                    print(f"{'='*70}")

                    # Print stats
                    system.print_episode_stats()

                    # Save
                    print(f"\nSaving all data for episode {episode_num}...")
                    episode_dir = base_output_dir / f"episode_{episode_num:03d}"
                    system.save_current_episode(episode_dir)
                    print(f"Saved to: {episode_dir}")

                    # Next episode
                    episode_num += 1
                    print(f"\n{'='*70}")
                    print(f"Ready for episode {episode_num}. Press 'd' to start...")
                    print(f"{'='*70}")

            else:
                print("Invalid input. Use 'd' (record), 'e' (exit), or 'q' (quit)")

    except KeyboardInterrupt:
        print("\n\nInterrupted")
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
    finally:
        system.shutdown()

    print(f"\nAll episodes saved to: {base_output_dir}")


if __name__ == "__main__":
    main()
