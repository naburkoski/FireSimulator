from abc import ABC
import pygame

dif = 0

def spikes(entity):
    entity.health -= 10

def bounce(entity):
    pass

def collide(entity):
    pass

class Platform():
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = None

    def collision(self):
        pass

    def draw(self, screen, dif):
#        self.rect[0] = (self.x, -dif)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)

class Spikes(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.damage = spikes

    def collision(self, entity):
        self.damage(entity)

class Bounce(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.bounce = bounce

    def collision(self):
        self.bounce(entity)

class Basic(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.collide = Basic

    def collision(entity):
        self.collide()
        
