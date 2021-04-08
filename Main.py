import os
import pygame
import random
from Player import *
from Enemy import *
from Platforms import *
from Physics import *

global currentDirection, dif
SCREENHEIGHT = 406
SCREENWIDTH = 500
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

pygame.init()

clock = pygame.time.Clock()
screencolor = (0, 0, 0)
screen = pygame.display.set_mode(SCREENSIZE)

startScrollPosX = (SCREENWIDTH / 2) - (84 / 2)

dif = 0

def redrawBackground():
    global dif

    backgroundWidth, backgroundHeight = background.get_rect().size
    stageWidth = backgroundWidth  
    stageHeight = backgroundHeight

    if player.x < startScrollPosX:
        if keys[pygame.K_LEFT] and dif > 0:
            player.x = startScrollPosX
            dif -= player.vel


    elif player.x > startScrollPosX:
        if keys[pygame.K_RIGHT] and dif < 200:
            player.x = startScrollPosX
            dif += player.vel

    screen.blit(background, (0 - dif, 0))

    for i in platforms:
        i.draw(screen, dif)

def redrawWindowStageOne():
    global background
    background = pygame.image.load(f'{os.getcwd()}\\images\\Background.png').convert()

    redrawBackground()
    player.move(keys, SCREENWIDTH)
    player.redraw(screen)

    pygame.draw.rect(screen, (255, 255, 255), player.hitbox, 1)

    for attack in attacks:
        attack.update()

    for e in enemies:
        screen.blit(e.enemyLeft, (e.x, e.y))

    pygame.display.update()


player = Character(50, 310, 70, 70)
attacks = []
platforms = [Basic(0, 310, SCREENWIDTH, 2)]
enemy = enemy(50, 340, 70, 10, 10)
enemies = []
enemies.append(enemy)
maxenemies = 10
physics = Physics()
physics.addEntities([[player], attacks, platforms])
#for i in range(maxenemies):
#    enemies.append(enemy(random.randint(0, screen_width), random.randint(0, screen_height), 80, 84, 650)

running = True
while running:
    global keys
    keys = pygame.key.get_pressed()

    enemy.move()

    pygame.display.set_caption("Working title")
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.currentDirection == "Left":
        direction = -1
    else:
        direction = 1
    if keys[pygame.K_f]:
        if len(attacks) < 3:
            attacks.append(
                playerAttacks(round(player.x + player.width // 2), round(player.y + player.height // 2), 10, 10, direction, 15, 1))
                       

    pygame.time.delay(50)

    redrawWindowStageOne()

pygame.quit()
