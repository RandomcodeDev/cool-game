import pygame

import globals

from typing import Tuple

from sprite import sprite_sheet

class player:
	# Display surface
	display_surface: pygame.Surface

	# Sprite
	sprite: sprite_sheet

	# Position
	x: int
	y: int
 
	# Size
	size: Tuple[int, int]
 
	# Movement speed
	speed: int

	def __init__(self, x, y):
		self.display_surface = globals.game.surface
		self.sprite = sprite_sheet("assets/textures/player.png")
		self.size = self.sprite[0].get_size()
		self.x = x
		self.y = y
		self.speed = 5

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.y -= self.speed
		elif keys[pygame.K_DOWN]:
			self.y += self.speed
		
		if keys[pygame.K_RIGHT]:
			self.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.x -= self.speed

	def draw_player(self):
		self.display_surface.blit(self.sprite[0], (self.x, self.y))