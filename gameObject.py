import pygame as pg

class GameObject:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
        self.color = (255, 255, 255)

    def draw(self, vindu):
        pg.draw.rect(vindu, self.color, self.rect)
