import pygame

from typing import AnyStr, Tuple


class sprite_sheet:
    """Allows for individual images to be retrieved from a singular strip of images"""

    image: pygame.Surface  # The image to get sprites from
    sprite_count: int  # The number of sprites
    sprite_size: Tuple[int, int]  # The size of the sprites
    vertical: bool  # Whether the image is a vertical or horizontal set of sprites
    distance: int  # Number of pixels separating sprites
    __sprite__: pygame.Surface  # The current sprite

    def __init__(
        self,
        image: (AnyStr | pygame.Surface),
        sprite_count: int = 0,
        sprite_size: Tuple[int, int] = (16, 16),
        distance: int = 0,
        vertical: bool = False,
        offset_pos: Tuple[int, int] = (0, 0),
    ):
        # Either use a surface from an already loaded image, or load a file
        if type(image) == str:
            self.image = pygame.image.load(image)
        else:
            self.image = image

        # Apply an offset if there is one by copying from the offset to the bottom right corner of the image
        if offset_pos != (0, 0):
            tmp = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            tmp.blit(
                self.image,
                (0, 0),
                pygame.Rect(
                    offset_pos[0],
                    offset_pos[1],
                    self.image.get_width() - offset_pos[0],
                    self.image.get_height() - offset_pos[1],
                ),
            )
            self.image = tmp
        self.sprite_size = sprite_size
        self.distance = distance
        self.vertical = vertical

        # If the sprite count is 0, calculate it automatically
        if sprite_count == 0:
            if self.vertical:
                self.sprite_count = self.image.get_height() // (
                    self.sprite_size[1] + self.distance
                )
            else:
                self.sprite_count = self.image.get_width() // (
                    self.sprite_size[0] + self.distance
                )
        else:
            self.sprite_count = sprite_count

    def __getitem__(self, key: int):
        self.__sprite__ = pygame.Surface(self.sprite_size, pygame.SRCALPHA)

        if self.vertical:
            area = pygame.Rect(
                0,
                (self.sprite_size[1] + self.distance) * key,
                self.sprite_size[0],
                self.sprite_size[1],
            )
        else:
            area = pygame.Rect(
                (self.sprite_size[1] + self.distance) * key,
                0,
                self.sprite_size[0],
                self.sprite_size[1],
            )

        self.__sprite__.blit(self.image, (0, 0), area)
        return self.__sprite__

    def __len__(self):
        return self.sprite_count
