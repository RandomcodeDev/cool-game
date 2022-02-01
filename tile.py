import pygame

import globals

WORLD_MAP = [
['l','b','r'],
['l',',','r'],
['l','f','r']
]

class tile:
    BACK_WALL: str = 'b'
    FRONT_WALL: str = 'f'
    LEFT_WALL: str = 'l'
    RIGHT_WALL: str = 'r'
    EMPTY: str = ','
    PLAYER: str = 'p'
    TILESIZE: int = 64
    def __init__(self, map):
        self.map = map

        self.display_surface = globals.game.draw

    def draw_map(self):
        for row_num,row in enumerate(self.map):
            for col_num,column in enumerate(row):
                x = col_num * tile.TILESIZE
                y = row_num * tile.TILESIZE
                if column == tile.BACK_WALL:
                    pygame.draw.rect(self.display_surface, ('red'), (x, y, tile.TILESIZE, tile.TILESIZE))
                elif column == tile.FRONT_WALL:
                    pygame.draw.rect(self.display_surface, ('red'), (x, y, tile.TILESIZE, tile.TILESIZE))
                elif column == tile.RIGHT_WALL:
                    pygame.draw.rect(self.display_surface, ('red'), (x, y, tile.TILESIZE, tile.TILESIZE))
                elif column == tile.LEFT_WALL:
                    pygame.draw.rect(self.display_surface, ('red'), (x, y, tile.TILESIZE, tile.TILESIZE))
                elif column == tile.EMPTY:
                    pass