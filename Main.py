from random import randint
import pygame
from Player import Player
from Glaser import Glaser
from Enemy import Enemy

# initiate pygame.

pygame.init()
win = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Space Wars")
clock = pygame.time.Clock()
run = True

# loading Images
bg1 = pygame.transform.scale((pygame.image.load('Images/bg1.jpg')), (600, 600))
bg2 = pygame.transform.scale((pygame.image.load('Images/bg2.jpg')), (600, 600))
bg3 = pygame.image.load('Images/bg3.jpg')


def RedrawGameWindow():
    win.blit(bg3, (0, 0))
    Ship.draw(win)
    if laser.Apper:
        laser.draw(win)
    for i in range(len(Enemies)):
        Enemies[i].draw(win)

    pygame.display.update()


def gameOverDraw():
    gameover = font.render("Game Over", 1, (255, 0, 0))
    win.blit(gameover, (150, 150))
    Choice = font.render(" Continue Y/N", 1, (255, 255, 255))
    win.blit(Choice, (150, 250))
    pygame.display.update()


font = pygame.font.SysFont('Algerian', 40, True, False)
Ship = Player(255, 500, 64, 64)
laser = Glaser(Ship.x + Ship.width // 2, Ship.y - 20, 5, 15, (0, 255, 0))
Enemies = []
level = 1
cnt = 0
points = 0

# levels
lvl1 = True
lvl2 = False
BossLvl = False

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not (laser.Safty):
        laser.y -= laser.vel
        laser.Safty = False

        if laser.y <= 0:
            laser.Safty = True
            laser.Apper = False

    # level 1
    if len(Enemies) <= 5 and lvl1:
        for i in range(10):
            Enemies.append(Enemy(randint(10, 550), randint(5, 100), 32, 32, 1))
    for E in Enemies:
        E.y += E.vel
        if E.x <= laser.x <= E.x + E.width:
            if E.y <= laser.y <= E.y + E.height:
                Enemies.pop(Enemies.index(E))
                laser.Apper = False
                laser.Safty = True
                Ship.score += 1


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and Ship.x > Ship.vel:
        Ship.x -= Ship.vel
    if keys[pygame.K_RIGHT] and Ship.x < 600 - Ship.vel - Ship.width:
        Ship.x += Ship.vel
    if laser.Safty:
        if keys[pygame.K_SPACE]:
            laser.y = Ship.y - 20
            laser.x = Ship.x + Ship.width // 2
            laser.Apper = True
            laser.Safty = False

    # checking hits
    for E in Enemies:
        if E.y >= 500:
            Enemies.pop(Enemies.index(E))
            Ship.hit()

    if Ship.GameOver:

        gameOverDraw()
        if keys[pygame.K_y]:
            run = True
            Ship.GameOver = False
            Ship.life = 5
            Ship.score = 0
            for E in Enemies:
                Enemies.pop(Enemies.index(E))
            RedrawGameWindow()
        elif keys[pygame.K_n]:
            run = False
    else:
        RedrawGameWindow()

pygame.quit()
