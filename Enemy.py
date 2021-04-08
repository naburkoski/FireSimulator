import pygame
import os
import random

# os.chdir(os.path.dirname(file))
pygame.init()

# Enemy images


class enemy(object):
        enemyLeft = pygame.image.load(f'{os.getcwd()}\images\EnemyOne.png')
        enemyRight = pygame.transform.flip(enemyLeft, True, False)

        def __init__(self, x, y, width, height, end):
                self.x= x
                self.y= y
                self.width = width
                self.height = height
                self.end= end
                self.vel = 3
                self.walkCount = 0
                self.path = [self.y, self.end]
                self.hitbox = (self.x + 20, self.y, 70, 60)
                self.health = 0.2
                self.visible = True
                self.hitbox = (self.x + 2, self.y, 70, 60)
                self.previous_pos = self.x
                self.travel = random.randint(-250, 250)

        def draw(self, gameDisplay):
            if self.visible:
                if self.walkCount + 1 >= 27:
                    self.walkCount = 0
                else:
                    gameDisplay.blit(self.enemyLeft, (self.x, self.y))
                    self.walkCount += 0

        
        
        def move(self):
                if abs(self.x - self.previous_pos) >= abs(self.travel):
                        self.previous_pos = self.x
                        self.travel = random.randint(-250, 250)

                self.x += self.vel * (self.travel/abs(self.travel))
        
        def collision(self):
            if self.health > 0:
                self.health-= 1
            else:
                self.visible= False
            print("HIT")
