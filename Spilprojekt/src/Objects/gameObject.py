import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, parentScene):
        pygame.sprite.Sprite.__init__(self, parentScene.sprites)

        self.parentScene = parentScene
        self.pos = pygame.Vector2(0, 0)
        self.width = 0
        self.height = 0

        self.solid = False

        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()

    @property
    def x(self):
        return self.pos.x

    @x.setter
    def x(self, value):
        self.pos.x = value
        self.rect.x = value

    @property
    def y(self):
        return self.pos.y

    @y.setter
    def y(self, value):
        self.pos.y = value
        self.rect.y = value

    def update(self, deltaTime):
        pass

    def draw(self, display):
        pass

    def cleanup(self):
        pass

    @property
    def boundaries(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)