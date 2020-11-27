from src.Objects.gameObject import GameObject
import pygame

#https://commons.wikimedia.org/wiki/File:MemeCoin_Crypto_Currency_Logo.png

class MemeCoin(GameObject):

    def __init__(self, parentScene, x, y):
        super().__init__(parentScene)

        self.image = pygame.image.load("res/img/MemeCoin.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

    def update(self, deltaTime):
        pass

    def draw(self, display):
        pass