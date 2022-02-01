import sys

import pygame

import globals

from pygame.locals import *

from anim import animation
from level import level
from settings import *
<<<<<<< HEAD

from sprite import sprite_sheet
from level import level
=======
from level import Level
>>>>>>> c32998a45dc525023df96e9eb4f750327904ca0a
from tile import *


class game:
    """Main class"""

    # Screen
    screen: pygame.Surface

    # Clock
    clock: pygame.time.Clock

    # Drawing area (16:9)
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

        self.refresh_size()

        pygame.display.set_caption("Shitty Game")
        self.clock = pygame.time.Clock()

    def refresh_size(self):
        # Magic constantants for 16:9
        self.draw = pygame.Surface(
            (
                int(self.screen.get_height() * 1.77777778),
                int(self.screen.get_width() * 0.5625),
            )
        )
        self.draw.fill("black")

    def blit_draw(self):
        if self.screen.get_size() == self.draw.get_size():
            x = 0
            y = 0
        elif self.screen.get_width() > self.draw.get_width():
            x = self.screen.get_width() / 2 - self.draw.get_width() / 2
            y = 0
        else:
            x = 0
            y = self.screen.get_height() / 2 - self.draw.get_height() / 2
            
        self.screen.blit(self.draw, (x, y))

    def toggle_fullscreen(self):
        display_info = pygame.display.Info()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()

            self.screen.fill("black")
            self.refresh_size()

            t = tile(WORLD_MAP)
            t.draw_map()
                
            self.blit_draw()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    globals.game = game()
    globals.game.run()
