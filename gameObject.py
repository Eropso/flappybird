import pygame as pg

class GameObject:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.color = (255, 255, 255)

    def draw(self, vindu):
        pg.draw.rect(vindu, self.color, (self._x, self._y, self._width, self._height))
