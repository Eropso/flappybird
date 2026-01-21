import pygame as pg

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE = 600
hvit = (255, 255, 255)

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class GameObject:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def draw(self):
        pg.draw.rect(vindu, hvit, (self._x, self._y, self._width, self._height))
