import pygame
import random

import globals

from typing import AnyStr, List, Union

from sprite import sprite_sheet

WORLD_MAP = [
['tl','b','tr'],
['ls',',','rs'],
['bl','f','br']
]

class tile:
	"""Tilemap"""
	
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
	TILESIZE: int = 128

	map: List[List[str]] # List of tiles to use
	sprites: sprite_sheet # Sprite sheet to get tiles from
	display_surface: pygame.Surface # Surface to draw to

	def __init__(self, map: List[List[str]], sprites: Union[AnyStr, sprite_sheet]):
		self.map = map
		if type(sprites) == str:
			self.sprites = sprite_sheet(sprites, sprite_size = (tile.TILESIZE, tile.TILESIZE), distance = 10)
		else:
			self.sprites = sprites

		self.display_surface = globals.game.surface

	def draw_map(self):
		for row_num,row in enumerate(self.map):
			for col_num,column in enumerate(row):
				x = col_num * tile.TILESIZE
				y = row_num * tile.TILESIZE
				if column == tile.BACK_WALL:
					self.display_surface.blit(self.sprites[3], (x, y))
				elif column == tile.FRONT_WALL:
					self.display_surface.blit(self.sprites[1], (x, y))
				elif column == tile.TOP_LEFT:
					self.display_surface.blit(pygame.transform.flip(self.sprites[4], True, False), (x, y))
				elif column == tile.TOP_RIGHT:
					self.display_surface.blit(self.sprites[4], (x, y))
				elif column == tile.BOTTOM_RIGHT:
					self.display_surface.blit(pygame.transform.flip(self.sprites[0], True, False), (x, y))
				elif column == tile.BOTTOM_LEFT:
					self.display_surface.blit(self.sprites[0], (x, y))
				elif column == tile.LEFT_SIDE:
					self.display_surface.blit(self.sprites[2], (x, y))
				elif column == tile.RIGHT_SIDE:
					self.display_surface.blit(pygame.transform.flip(self.sprites[2], True, False), (x, y))
				elif column == tile.EMPTY:
					pass

	def draw_ground(self):
		x: int = 0
		y: int = 0
		for i in range(self.display_surface.get_height()/128):
			for i in range(self.display_surface.get_width()/128):
				random = random.randint(0,2)
				self.display_surface.blit("""put sprite here"""[random],(x, y))
				x += tile.TILESIZE

			y += tile.TILESIZE
