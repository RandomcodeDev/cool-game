import sys

import pygame
from pygame.locals import *

from settings import *
from level import Level
from tile import *


class Game:
    def __init__(self):

        pygame.init()

        display_info = pygame.display.Info()
        width = display_info.current_w * 0.5
        height = display_info.current_h * 0.5

        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("Main")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        # toggle fullscreen
                        pass

            self.screen.fill("black")
            t = tile(WORLD_MAP)
            t.draw_map()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
