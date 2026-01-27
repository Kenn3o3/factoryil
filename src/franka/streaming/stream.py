"""Background camera streaming with frame buffering."""

import time
import threading
from typing import Callable, Optional, Literal
from dataclasses import dataclass

from streaming.buffer import RingBuffer
from utils.timing import monotonic_ns


@dataclass
class StreamedFrame:
    """Frame with timestamp from stream."""
    data: any  # Frame data
    timestamp_ns: int  # Monotonic timestamp
    sequence: int  # Sequence number


class CameraStream:
    """
    Background camera stream with ring buffer.

    Continuously grabs frames in a background thread and stores them
    in a ring buffer for synchronized access.
    """

    def __init__(
        self,
        name: str,
        grab_func: Callable[[], any],
        buffer_size: int = 60,
        warmup_frames: int = 10,
    ):
        """
        Initialize camera stream.

        Args:
            name: Stream name for logging
            grab_func: Function that grabs one frame
            buffer_size: Ring buffer capacity
            warmup_frames: Number of frames to discard during warmup
        """
        self.name = name
        self._grab_func = grab_func
        self._warmup_frames = warmup_frames

        self._buffer = RingBuffer[StreamedFrame](maxlen=buffer_size)
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._ready_event = threading.Event()

        self._sequence = 0
        self._error_count = 0
        self._is_running = False

    def start(self) -> None:
        """Start background grabbing thread."""
        if self._is_running:
            return

        print(f"[{self.name}] Starting stream...")
        self._stop_event.clear()
        self._ready_event.clear()
        self._is_running = True

        self._thread = threading.Thread(
            target=self._grab_loop,
            name=f"Stream-{self.name}",
            daemon=True,
        )
        self._thread.start()

    def _grab_loop(self) -> None:
        """Background loop that continuously grabs frames."""
        warmup_count = 0

        while not self._stop_event.is_set():
            try:
                # Grab frame
                data = self._grab_func()
                timestamp_ns = monotonic_ns()

                # Warmup phase: discard frames
                if warmup_count < self._warmup_frames:
                    warmup_count += 1
                    if warmup_count == self._warmup_frames:
                        print(f"[{self.name}] Warmup complete")
                        self._ready_event.set()
                    continue

                # Create frame and add to buffer
                frame = StreamedFrame(
                    data=data,
                    timestamp_ns=timestamp_ns,
                    sequence=self._sequence,
                )
                self._sequence += 1
                self._buffer.append(frame)

            except Exception as e:
                self._error_count += 1
                if self._error_count % 10 == 1:
                    print(f"[{self.name}] Error: {e}")
                time.sleep(0.01)  # Backoff

    def stop(self) -> None:
        """Stop background grabbing thread."""
        if not self._is_running:
            return

        print(f"[{self.name}] Stopping stream...")
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=2.0)
        self._is_running = False

    def wait_ready(self, timeout: float = 10.0) -> bool:
        """
        Wait for stream to be ready.

        Args:
            timeout: Maximum time to wait

        Returns:
            True if ready, False if timeout
        """
        return self._ready_event.wait(timeout=timeout)

    def get_frame(
        self,
        target_ns: int,
        strategy: Literal["closest", "latest_before"] = "closest",
        max_age_ns: Optional[int] = None,
    ) -> Optional[StreamedFrame]:
        """
        Get frame based on target timestamp and strategy.

        Args:
            target_ns: Target timestamp (monotonic)
            strategy: Frame selection strategy
            max_age_ns: Maximum allowed age from target

        Returns:
            Selected frame or None if no suitable frame found
        """
        frames = self._buffer.get_all()
        if len(frames) == 0:
            return None

        if strategy == "closest":
            # Find frame closest to target
            best_frame = min(frames, key=lambda f: abs(f.timestamp_ns - target_ns))
        elif strategy == "latest_before":
            # Find latest frame before or at target
            before_frames = [f for f in frames if f.timestamp_ns <= target_ns]
            if not before_frames:
                return None
            best_frame = max(before_frames, key=lambda f: f.timestamp_ns)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        # Check age constraint
        if max_age_ns is not None:
            age = abs(best_frame.timestamp_ns - target_ns)
            if age > max_age_ns:
                return None

        return best_frame

    @property
    def error_count(self) -> int:
        """Get number of errors encountered."""
        return self._error_count

    @property
    def buffer_size(self) -> int:
        """Get current buffer size."""
        return len(self._buffer)
