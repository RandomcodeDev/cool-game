import pygame

import globals

class player:
    SPEED = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = None # put player sprite sheet direct here
        self.display_surface = globals.game.draw
        self.rect = pygame.Rect(x, y, 64, 64)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y += player.SPEED
        elif keys[pygame.K_DOWN]:
            self.y -= player.SPEED
        
        if keys[pygame.K_RIGHT]:
            self.x += player.SPEED
        elif keys[pygame.K_LEFT]:
            self.x -= player.SPEED

    def draw_player(self):
        pygame.draw.rect(self.display_surface, (255,255,255), self.rect)