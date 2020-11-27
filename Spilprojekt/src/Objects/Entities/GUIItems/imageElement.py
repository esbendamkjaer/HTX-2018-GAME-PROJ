from src.Objects.Entities.entity import Entity
import pygame

class ImageElement(Entity):

    def __init__(self, parentScene, x, y, file):
        super().__init__(parentScene)

        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

    def update(self, deltaTime):
        pass

    def draw(self, display):
        pass