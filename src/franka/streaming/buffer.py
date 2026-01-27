"""Ring buffer implementation for frame storage."""

from collections import deque
from typing import Generic, TypeVar, Optional
import threading

T = TypeVar('T')


class RingBuffer(Generic[T]):
    """
    Thread-safe ring buffer with fixed capacity.

    When full, oldest items are automatically discarded.
    """

    def __init__(self, maxlen: int):
        """
        Initialize ring buffer.

        Args:
            maxlen: Maximum number of items to store
        """
        self._buffer = deque(maxlen=maxlen)
        self._lock = threading.Lock()
        self._new_item_event = threading.Event()

    def append(self, item: T) -> None:
        """
        Add item to buffer.

        Args:
            item: Item to add
        """
        with self._lock:
            self._buffer.append(item)
            self._new_item_event.set()

    def get_latest(self) -> Optional[T]:
        """Get most recent item."""
        with self._lock:
            if len(self._buffer) == 0:
                return None
            return self._buffer[-1]

    def get_all(self) -> list[T]:
        """Get all items in buffer (oldest to newest)."""
        with self._lock:
            return list(self._buffer)

    def clear(self) -> None:
        """Clear all items from buffer."""
        with self._lock:
            self._buffer.clear()
            self._new_item_event.clear()

    def wait_for_new_item(self, timeout: Optional[float] = None) -> bool:
        """
        Wait for a new item to be added.

        Args:
            timeout: Maximum time to wait in seconds

        Returns:
            True if new item arrived, False if timeout
        """
        result = self._new_item_event.wait(timeout=timeout)
        self._new_item_event.clear()
        return result

    def __len__(self) -> int:
        with self._lock:
            return len(self._buffer)
