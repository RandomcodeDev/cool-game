from dbm import dumb
import pygame
import random

import globals

from typing import AnyStr, List, Union

from sprite import sprite_sheet

WORLD_MAP = [
[',',',',',',',',',',',',',',',',',',',',',',',',',',',',','],
[',',',',',',',',',',',',',',',',',','fp',',','tl','b','tr',','],
[',',',',',',',',',',',',',',',',',',',',',','ls','fp','rs',','],
[',',',',',',',',',',',',',',',','fp',',',',','bl','f','br',','],
[',',',',',',',',',',',',',',',',',',',',',',',',',',',',','],
[',',',','fp',',',',',',',',',',',',',',',',',',',',',',',','],
[',',',',',',',',',',',',',',',',',','bp',',',',','fp',',',','],
[',',',',',',',',',',',',',',',',',',',',',',',',',',',',',']
]

GROUND_MAP = []

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
	FULL_PILLAR: str = 'fp'
	BROKEN_PILLAR: str = 'bp'
	TILESIZE: int = 128

	map: List[List[str]] # List of tiles to use
	wall_sprites: sprite_sheet # Sprite sheet to get tiles from
	display_surface: pygame.Surface # Surface to draw to

	def __init__(self, map: List[List[str]], sprites: AnyStr):
		self.map = map
		self.wall_sprites = sprite_sheet(sprites, sprite_size = (tile.TILESIZE, tile.TILESIZE), distance = 20)
		self.ground_sprites = sprite_sheet(sprites, sprite_size = (tile.TILESIZE, tile.TILESIZE), distance = 20, offset_pos=(0, 148))
		self.pillar = sprite_sheet(sprites, sprite_size = (tile.TILESIZE, tile.TILESIZE), distance = 20, offset_pos=(0, 296))

		self.display_surface = globals.game.surface

	def draw_map(self):
		for row_num,row in enumerate(self.map):
			for col_num,column in enumerate(row):
				x = col_num * tile.TILESIZE
				y = row_num * tile.TILESIZE
				if column == tile.BACK_WALL:
					self.display_surface.blit(self.wall_sprites[3], (x, y))
				elif column == tile.FRONT_WALL:
					self.display_surface.blit(self.wall_sprites[1], (x, y))
				elif column == tile.TOP_LEFT:
					self.display_surface.blit(pygame.transform.flip(self.wall_sprites[4], True, False), (x, y))
				elif column == tile.TOP_RIGHT:
					self.display_surface.blit(self.wall_sprites[4], (x, y))
				elif column == tile.BOTTOM_RIGHT:
					self.display_surface.blit(pygame.transform.flip(self.wall_sprites[0], True, False), (x, y))
				elif column == tile.BOTTOM_LEFT:
					self.display_surface.blit(self.wall_sprites[0], (x, y))
				elif column == tile.LEFT_SIDE:
					self.display_surface.blit(self.wall_sprites[2], (x, y))
				elif column == tile.RIGHT_SIDE:
					self.display_surface.blit(pygame.transform.flip(self.wall_sprites[2], True, False), (x, y))
				elif column == tile.FULL_PILLAR:
					self.display_surface.blit(self.pillar[0], (x, y))
				elif column == tile.EMPTY:
					pass
 
	def draw_ground(self):
		if globals.easter_egg:
			self.display_surface.blit(globals.vader_img, (0,0))
		else:
			x = 0
			y = 0
			for i in range(self.display_surface.get_height() // tile.TILESIZE + 1):
				x = 0
				for j in range(self.display_surface.get_width() // tile.TILESIZE + 1):
					self.display_surface.blit(self.ground_sprites[GROUND_MAP[i][j]], (x, y))
					x += tile.TILESIZE
				y += tile.TILESIZE

	def create_ground(self):
		for i in range(self.display_surface.get_height() // tile.TILESIZE + 1):
			GROUND_MAP.append([])
			for j in range(self.display_surface.get_width() // tile.TILESIZE + 1):
				GROUND_MAP[i].append(random.randint(0, len(self.ground_sprites) - 1))
