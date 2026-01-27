"""Timing utilities for synchronization."""

import time


def monotonic_ns() -> int:
    """Get current monotonic timestamp in nanoseconds."""
    return time.monotonic_ns()


def realtime_ns() -> int:
    """Get current real-time timestamp in nanoseconds."""
    return time.time_ns()


def sleep_until(target_ns: int) -> None:
    """
    Sleep until target monotonic timestamp.

    Args:
        target_ns: Target timestamp in nanoseconds (monotonic)
    """
    now_ns = monotonic_ns()
    sleep_duration_s = (target_ns - now_ns) / 1e9
    if sleep_duration_s > 0:
        time.sleep(sleep_duration_s)


def offset_ms(timestamp_ns: int, target_ns: int) -> float:
    """
    Calculate offset in milliseconds.

    Args:
        timestamp_ns: Actual timestamp
        target_ns: Target timestamp

    Returns:
        Offset in milliseconds (positive = after target, negative = before target)
    """
    return (timestamp_ns - target_ns) / 1e6
