import pygame


class Player(object):
    PlayerImage = pygame.image.load('Images/spaceship.png')

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.vel = 10
        self.score = 0
        self.life = 5
        self.GameOver = False


    def draw(self, win):
        font = pygame.font.SysFont('Algerian', 20, True, False)
        text = font.render("SCORE: " + str(self.score), 1, (255, 255, 255))
        text1 = font.render("LIVES: " + str(self.life), 1, (255, 255, 255))
        win.blit(self.PlayerImage, (self.x, self.y))
        win.blit(text, (450, 10))
        win.blit(text1, (20, 10))

    def hit(self):
        self.life -= 1
        if self.life == 0:
            self.GameOver = True



