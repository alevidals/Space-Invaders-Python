from .constants import BULLET, SHIP_VEL

class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = SHIP_VEL
        self.direction = -1
        self.rect = None

    def draw(self, win):
        self.rect = win.blit(BULLET, (self.x, self.y))
        # print(self.rect)

    def move(self):
        self.y += self.vel * self.direction

    def kill(self, enemies, bullets):
        for enemy in enemies:
            if self.rect.colliderect(enemy.get_rect()):
                self.remove(bullets)
                enemy.remove(enemies)

    def remove(self, bullets):
        bullets.pop(bullets.index(self))