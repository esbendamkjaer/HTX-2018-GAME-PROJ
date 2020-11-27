import pygame
from src.Objects.gameObject import GameObject


class Wall(GameObject):

    def __init__(self, parentScene, x, y, width, height):
        super().__init__(parentScene)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.solid = True
        #self.image = pygame.Surface((self.width, self.height))

        #self.image.fill((0, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, deltaTime):
        super().update(deltaTime)

    def draw(self, display):
        super().draw(display)