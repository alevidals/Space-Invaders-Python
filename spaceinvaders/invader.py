from .constants import ENEMIES_PER_COL, IMAGE_HEIGHT, IMAGE_WIDTH, INVADERS_A, INVADERS_B, INVADERS_C
import threading, time

class Invader():
    def __init__(self, x, y, images):
        self.actual_image = 1
        self.x = x
        self.y = y
        self.images = images
        self.rect = None
        thread = threading.Thread(target=self.animate, daemon=True)
        thread.start()

    @staticmethod
    def init_invaders():
        invaders = []
        y = 50
        x = 50
        for i in range(ENEMIES_PER_COL):
            if (i == 10):
                y += IMAGE_HEIGHT + 15
                x = 50
            invaders.append(Invader(x, y, INVADERS_A))
            x += IMAGE_WIDTH + 15

        y += IMAGE_HEIGHT + 15
        x =50

        for i in range(ENEMIES_PER_COL):
            if (i == 10):
                y += IMAGE_HEIGHT + 15
                x = 50
            invaders.append(Invader(x, y, INVADERS_B))
            x += IMAGE_WIDTH + 15

        y += IMAGE_HEIGHT + 15
        x = 50

        for i in range(ENEMIES_PER_COL):
            if (i == 10):
                y += IMAGE_HEIGHT + 15
                x = 50
            invaders.append(Invader(x, y, INVADERS_C))
            x += IMAGE_WIDTH + 15

        return invaders

    def draw(self, win):
        self.rect = win.blit(self.images[self.actual_image], (self.x, self.y))
        # self.animate()

    def move(self, x, y):
        self.x = x
        self.y = y

    def animate(self, n=2):
        while True:
            if (self.actual_image == 0):
                self.actual_image = 1
            else:
                self.actual_image = 0

            self.move(self.x + 10, self.y)
            time.sleep(.8)

    def remove(self, invaders):
        invaders.pop(invaders.index(self))

    def get_rect(self):
        return self.rect