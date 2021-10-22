import pygame


class Enemy(object):
    PlayerImage = pygame.image.load('Images/alien.png')


    def __init__(self, x, y, w, h, vel):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.vel = vel


    def draw(self, win):
        #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)
        win.blit(self.PlayerImage, (self.x, self.y))





