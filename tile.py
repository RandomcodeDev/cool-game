import pygame

import globals
from settings import TILESIZE

from sprite import sprite_sheet

WORLD_MAP = [
['tl','b','tr'],
['ls',',','rs'],
['bl','f','br']
]

class tile:
    BACK_WALL: str = 'b'
    FRONT_WALL: str = 'f'
    TOP_LEFT: str = 'tl'
    TOP_RIGHT: str = 'tr'
    BOTTOM_LEFT: str = 'bl'
    BOTTOM_RIGHT: str = 'br'
    LEFT_SIDE: str = 'ls'
    RIGHT_SIDE: str = 'rs'
    EMPTY: str = ','
    PLAYER: str = 'p'
    TILESIZE: int = 64

    def __init__(self, map):
        self.map = map
        self.wall_sprite = sprite_sheet("assets/textures/wall_sprites.png", sprite_size = (TILESIZE, TILESIZE), distance = 10)

        self.display_surface = globals.game.draw

    def draw_map(self):
        for row_num,row in enumerate(self.map):
            for col_num,column in enumerate(row):
                x = col_num * tile.TILESIZE
                y = row_num * tile.TILESIZE
                if column == tile.BACK_WALL:
                    self.display_surface.blit(self.wall_sprite[3], (x, y))
                elif column == tile.FRONT_WALL:
                    self.display_surface.blit(self.wall_sprite[1], (x, y))
                elif column == tile.TOP_LEFT:
                    self.display_surface.blit(pygame.transform.flip(self.wall_sprite[4], True, False), (x, y))
                elif column == tile.TOP_RIGHT:
                    self.display_surface.blit(self.wall_sprite[4], (x, y))
                elif column == tile.BOTTOM_RIGHT:
                    self.display_surface.blit(pygame.transform.flip(self.wall_sprite[0], True, False), (x, y))
                elif column == tile.BOTTOM_LEFT:
                    self.display_surface.blit(self.wall_sprite[0], (x, y))
                elif column == tile.LEFT_SIDE:
                    self.display_surface.blit(self.wall_sprite[2], (x, y))
                elif column == tile.RIGHT_SIDE:
                    self.display_surface.blit(pygame.transform.flip(self.wall_sprite[2], True, False), (x, y))
                elif column == tile.EMPTY:
                    pass