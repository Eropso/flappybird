import pygame as pg
from gameObject import GameObject

class Pipe(GameObject):
    def __init__(self, x, y, width, height, speed, flip=False):
        super().__init__(x, y, width, height)
        self._speed = speed
        self.passed = False
        
        img = pg.image.load("skyscraper.png")
        self.image = pg.transform.scale(img, (width, height))
        if flip:
            self.image = pg.transform.flip(self.image, False, True)

    def update(self):
        self.rect.x -= self._speed

    def draw(self, vindu):
        vindu.blit(self.image, (self.rect.x, self.rect.y))
