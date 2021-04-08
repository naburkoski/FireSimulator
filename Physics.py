import pygame

class Physics:
    def __init__(self):
        self.entities = []

    def addEntities(self, x):
        for i in x:
            self.entities += i

    def run(self):
        for i in self.entities:
            colliding = pygame.Rect.collidelistall(self.entities)
