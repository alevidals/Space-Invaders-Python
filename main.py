import pygame

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.init()
pygame.init()

from spaceinvaders.constants import WIDTH, HEIGHT, BG, SHIP
from spaceinvaders.game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYUP:
                if keys[pygame.K_SPACE]:
                    game.ship.shoot(game.ship_bullets)

        if keys[pygame.K_LEFT] and game.ship.x > 2:
            game.ship.move(-1)
        if keys[pygame.K_RIGHT] and game.ship.x <= WIDTH - SHIP.get_width():
            game.ship.move(1)

        game.update()

    pygame.quit()

main()
