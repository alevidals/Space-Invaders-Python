import pygame

WIDTH, HEIGHT = 900, 700
GAME_LIFES = 3
SHIP_VEL = 7
BULLET_VEL = 7
ENEMIES_PER_COL = 20
# COLS = 12
# ROWS = 12
# SQUARE_SIZE = WIDTH // COLS
# MAX_ENEMIES = 60
MAX_ENEMIES = 3

SHOOT_SOUND = pygame.mixer.Sound('assets/sounds/ShipBullet.wav')
SHOOT_SOUND.set_volume(0.2)

BG = pygame.transform.scale(pygame.image.load('assets/images/bg.png'), (WIDTH, HEIGHT))
SHIP = pygame.image.load('assets/images/Ship.png')
BULLET = pygame.image.load('assets/images/Bullet.png')

# invader_a1 = pygame.transform.scale(pygame.image.load('assets/images/InvaderA1.png'), (WIDTH // ROWS - 20, 40))
# invader_a2 = pygame.transform.scale(pygame.image.load('assets/images/InvaderA2.png'), (WIDTH // ROWS - 20, 40))
invader_a1 = pygame.image.load('assets/images/InvaderA1.png')
invader_a2 = pygame.image.load('assets/images/InvaderA2.png')

invader_b1 = pygame.image.load('assets/images/InvaderB1.png')
invader_b2 = pygame.image.load('assets/images/InvaderB2.png')

invader_c1 = pygame.image.load('assets/images/InvaderC1.png')
invader_c2 = pygame.image.load('assets/images/InvaderC2.png')

INVADERS_A = [invader_a1, invader_a2]
INVADERS_B = [invader_b1, invader_b2]
INVADERS_C = [invader_c1, invader_c2]

IMAGE_WIDTH = invader_a1.get_width()
IMAGE_HEIGHT = invader_a1.get_height()