#!/usr/bin/env python3
"""
Synchronized data collection demo.

Usage:
    python collect_data.py [--auto] [--steps N] [--rate HZ]
"""

from utils.utils import activate_franka_conda_env
activate_franka_conda_env(__file__)

import sys
import argparse
from pathlib import Path
from datetime import datetime

from core import SystemConfig, DataCollectionSystem


def wait_for_user(auto: bool = False) -> None:
    """Wait for user input to start."""
    if auto:
        print("\n" + "=" * 70)
        print("STARTING (auto mode)")
        print("=" * 70)
        return

    print("\n" + "=" * 70)
    print("READY TO START")
    print("=" * 70)
    print("\nPress 'd' + Enter to start (or 'q' to quit)")

    while True:
        inp = input("> ").strip().lower()
        if inp == 'd':
            break
        elif inp == 'q':
            sys.exit(0)
        else:
            print("Invalid. Press 'd' or 'q'.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--rate", type=float, default=10.0)
    args = parser.parse_args()

    config = SystemConfig(rate_hz=args.rate)
    system = DataCollectionSystem(config)

    try:
        # Initialize
        print("=" * 70)
        print("INITIALIZATION")
        print("=" * 70)
        system.reset()

        # Wait
        wait_for_user(args.auto)

        # Collect
        print("\n" + "=" * 70)
        print(f"COLLECTING {args.steps} STEPS @ {args.rate} Hz")
        print("=" * 70)

        for i in range(args.steps):
            obs = system.step()
            sync = "✓" if obs.sync_quality.is_synchronized else "✗"
            print(f"{i+1}/{args.steps} {sync} "
                  f"R:{obs.sync_quality.robot_offset_ms:+.1f} "
                  f"G:{obs.sync_quality.gelsight_offset_ms:+.1f} "
                  f"O:{obs.sync_quality.orbbec_offset_ms:+.1f} ms")

        # Stats
        system.print_stats()

        # Save
        print("\n" + "=" * 70)
        print("SAVING")
        print("=" * 70)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(__file__).parent / "_out" / f"data_{timestamp}"
        system.save_episode(output_dir, "episode")

        print("\n" + "=" * 70)
        print("COMPLETE")
        print("=" * 70)
        print(f"Data: {output_dir}")

    except KeyboardInterrupt:
        print("\n\nInterrupted")
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
    finally:
        system.shutdown()


if __name__ == "__main__":
    main()
