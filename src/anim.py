import pygame

from sprite import sprite_sheet
from typing import Tuple

class animation:
    """Keeps track of the current frame of a spritesheet animation"""

    frames: sprite_sheet  # The spritesheet to get frames from
    frame_time: float  # The number of seconds per frame (usually less than 1)
    frame_size: Tuple[int, int]  # The size of the frames

    __frame__: int  # The current frame
    __timer__: int  # The timer

    def __init__(self, frames: sprite_sheet, frame_time: float = 0.016):
        self.frames = frames
        self.frame_time = frame_time
        self.frame_size = self.frames.sprite_size

        self.__frame__ = 0
        self.__timer__ = 0

    def frame(self, delta_millis: int) -> pygame.Surface:
        """Returns the current frame of the animation after advancing the timer by the delta given"""
        self.__timer__ += delta_millis
        if self.__timer__ / 1000 >= self.frame_time:
            self.__timer__ = 0
            self.__frame__ = (self.__frame__ + 1) % len(self.frames)

        return self.frames[self.__frame__]