import sys

import pygame

import globals

from pygame.locals import *

from anim import animation
from level import level

from sprite import sprite_sheet
from level import level
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

    # Drawing area (1920x1080)
    draw: pygame.Surface

    def __init__(self):
        pygame.init()

        display_info = pygame.display.Info()
        self.fullscreen_width = display_info.current_w
        self.fullscreen_height = display_info.current_h

        self.screen = pygame.display.set_mode(
            (self.fullscreen_width * 0.5, self.fullscreen_height * 0.5),
            pygame.RESIZABLE,
        )
        
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        self.fullscreen = False
        
        self.draw = pygame.Surface((self.fullscreen_width, self.fullscreen_height))

        pygame.display.set_caption("Shitty Game")
        self.clock = pygame.time.Clock()

    def blit_draw(self):
        width = int(self.screen.get_height() * 1.77777778)
        height = int(self.screen.get_width() * 0.5625)
        
        if self.screen.get_size() == width:
            x = 0
            y = 0
        elif self.screen.get_width() > width:
            x = self.screen.get_width() / 2 - width / 2
            y = 0
        else:
            x = 0
            y = self.screen.get_height() / 2 - height / 2
            
        scaled = pygame.transform.smoothscale(self.draw, (width, height))
        self.screen.blit(scaled, (x, y))

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            self.fullscreen = False
        else:
            display_info = pygame.display.Info()
            self.width = display_info.current_w
            self.height = display_info.current_h
            self.screen = pygame.display.set_mode((self.fullscreen_width, self.fullscreen_height), pygame.FULLSCREEN)
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

            self.draw.fill("black")

            t = tile(WORLD_MAP, sprite_sheet("assets/textures/wall_sprites.png", sprite_size = (tile.TILESIZE, tile.TILESIZE), distance = 10))
            t.draw_map()
                
            self.blit_draw()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    globals.game = game()
    globals.game.run()
