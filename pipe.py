import pygame as pg
from gameObject import GameObject

# Class for the obstacles (pipes)
class Pipe(GameObject):
    def __init__(self, x, y, width, height, speed, flip=False):
        super().__init__(x, y, width, height)
        self._speed = speed
        self._passed = False
        
        # Loads image for the pipe
        img = pg.image.load("skyscraper.png")
        self._image = pg.transform.scale(img, (width, height))
        # Flips the image if it is a top pipe
        if flip:
            self._image = pg.transform.flip(self._image, False, True)

    # Moves the pipe to the left
    def update(self):
        self.rect.x -= self._speed

    # Draws the pipe
    def draw(self, vindu):
        vindu.blit(self._image, (self.rect.x, self.rect.y))
