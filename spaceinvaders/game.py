import pygame
from spaceinvaders.ship import Ship
from spaceinvaders.invader import Invader
from .constants import BG, MAX_ENEMIES, INVADERS_A, INVADERS_B, INVADERS_C, IMAGE_WIDTH, ENEMIES_PER_COL, IMAGE_HEIGHT
# import threading, time

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.ship_bullets = []
        self.enemies_left = MAX_ENEMIES
        self.enemies = Invader.init_invaders()
        self.ship = Ship()

    def update(self):
        self.win.blit(BG, (0,0))
        self.ship.draw(self.win)
        self._draw_bullets()
        self._draw_enemies()
        pygame.display.update()

    def _draw_bullets(self):
        for bullet in self.ship_bullets:
            if bullet.y >= 0:
                bullet.move()
                bullet.draw(self.win)
                bullet.kill(self.enemies, self.ship_bullets)
            else:
                bullet.remove(self.ship_bullets)

    def _draw_enemies(self):
        for enemie in self.enemies:
            enemie.draw(self.win)
