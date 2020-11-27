import pygame


class Camera:
    def __init__(self, parentScenee, width, height):
        self.parentScene = parentScenee
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, gameObject):
        return gameObject.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.parentScene.game.display_width / 2)
        y = -target.rect.y + int(self.parentScene.game.display_height / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)