import pygame


class Glaser(object):
    Apper = False
    Safty = True
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.vel = 20

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
