"""Provides framerate-counting utility."""

import datetime
import time


class FramerateCounter():
    """Static class for managing framerate. Use frame() every frame, and framerate() to get current framerate.
    """
    _frames = []

    def frame():
        """Call this every frame to keep track of framerate.
        """
        FramerateCounter._clear_old_frames()
        FramerateCounter._frames.append(time.time_ns())

    def _clear_old_frames():
        """Clear frames older than a second
        """

        t = time.time_ns() - 1_000_000_000 #This timestamp and older are cleared.
        while True:
            if len(FramerateCounter._frames) > 0 and FramerateCounter._frames[0] <= t:
                FramerateCounter._frames.pop(0)
            else:
                return

    def framerate() -> int:
        """Return current framerate

        Returns:
            int: Number of frames in the last second.
        """

        FramerateCounter._clear_old_frames()
        return len(FramerateCounter._frames)