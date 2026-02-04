import pygame as pg

# Class representing a general game object
class GameObject:
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.rect = pg.Rect(x, y, width, height)
        self._color = color

    # Draws the object on the screen
    def draw(self, vindu):
        pg.draw.rect(vindu, self._color, self.rect)
