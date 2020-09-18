import pygame
from .constants import GAME_LIFES, SHIP, SHIP_VEL, HEIGHT, WIDTH, SHOOT_SOUND
from spaceinvaders.bullet import Bullet

class Ship():
    def __init__(self):
        self.lifes = GAME_LIFES
        self.x = 100
        self.y = HEIGHT - 100
        self.vel = SHIP_VEL
        self.score = 0

    def draw(self, win):
        win.blit(SHIP, (self.x, self.y))

    def move(self, direction):
        self.x += self.vel * direction

    def shoot(self, bullets):
        if (len(bullets) < 2):
            SHOOT_SOUND.play()
            w, h = SHIP.get_width(), SHIP.get_height()
            bullet = Bullet(self.x + w // 2, self.y + h // 2)
            bullets.append(bullet)