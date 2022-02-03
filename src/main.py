import sys

import pygame

import globals

from pygame.locals import *

from anim import animation
from level import level

from sprite import sprite_sheet
from level import level
from player import player
from tile import *


class game:
	"""Main class"""

	# Screen
	screen: pygame.Surface

	# Whether fullscreen is enabled
	fullscreen: bool

	# Fullscreen size
	fullscreen_width: int
	fullscreen_height: int

	# Pre-fullscreen size
	width: int
	height: int

	# Clock
	clock: pygame.time.Clock

	# FPSs
	fps: int

	# Drawing area
	surface: pygame.Surface

	def __init__(self):
		pygame.init()

		display_info = pygame.display.Info()
		self.fullscreen_width = display_info.current_w
		self.fullscreen_height = display_info.current_h

		self.screen = pygame.display.set_mode(
			(self.fullscreen_width * 0.5, self.fullscreen_height * 0.5),
			pygame.RESIZABLE,
			vsync=1,
		)

		self.width = self.screen.get_width()
		self.height = self.screen.get_height()

		self.fullscreen = False

		self.surface = pygame.Surface((1920, 1080))

		pygame.display.set_caption("Shitty Game")
		self.clock = pygame.time.Clock()
		self.fps = 0

	def blit_draw(self):
		width = self.screen.get_width()
		height = int(width * 0.5625)
		if height > self.screen.get_height():
			width = int(self.screen.get_height() * 1.7777778)
			height = self.screen.get_height()

		if self.screen.get_size() == width:
			x = 0
			y = 0
		elif self.screen.get_width() > width:
			x = self.screen.get_width() / 2 - width / 2
			y = 0
		else:
			x = 0
			y = self.screen.get_height() / 2 - height / 2

		scaled = pygame.transform.scale(self.surface, (width, height))
		self.screen.blit(scaled, (x, y))

	def toggle_fullscreen(self):
		if self.fullscreen:
			self.screen = pygame.display.set_mode(
				(self.width, self.height), pygame.RESIZABLE, vsync=1
			)
			self.fullscreen = False
		else:
			size = pygame.display.get_window_size()
			self.width = size[0]
			self.height = size[1]
			self.screen = pygame.display.set_mode(
				(self.fullscreen_width, self.fullscreen_height),
				pygame.FULLSCREEN | pygame.RESIZABLE,
			)
			self.fullscreen = True

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_F11:
						self.toggle_fullscreen()

			self.surface.fill((15, 10, 15))

			globals.tiles.draw_ground()
			globals.tiles.draw_map()

			globals.player.input()
			globals.player.draw_player()

			self.blit_draw()

			pygame.display.update()
			self.clock.tick(60)
			self.fps = self.clock.get_fps()
			print(f"\r{round(self.fps, 2)}", end="")


# Start all the things
if __name__ == "__main__":
	globals.game = game()

	globals.player = player(100, 100)

	globals.tiles = tile(
				WORLD_MAP, "assets/textures/tiles.png"
			)

	globals.tiles.create_ground()
	
	globals.vader_img = pygame.image.load("assets/textures/vader.png")

	globals.game.run()
