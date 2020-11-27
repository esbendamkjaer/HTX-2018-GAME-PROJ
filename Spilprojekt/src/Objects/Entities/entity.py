from src.Objects.gameObject import GameObject
import pygame


class Entity(GameObject):

    def __init__(self, parentScene):
        super().__init__(parentScene)
        self.velocity = pygame.Vector2(0, 0)

