from src.Objects.Entities.entity import Entity
from src.Objects.Statics.memeCoin import MemeCoin
import pygame


class Player(Entity):

    def __init__(self, parentScene, x, y):
        super().__init__(parentScene)
        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load("res/img/elev.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.width = self.image.get_rect().width
        self.height = 16

        self.x = x
        self.y = y

        pygame.draw.rect(self.image, (0,0,0), self.boundaries)


    def update(self, deltaTime):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.velocity.x = 300
        if keys[pygame.K_LEFT]:
            self.velocity.x = -300
        if keys[pygame.K_DOWN]:
            self.velocity.y = 300
        if keys[pygame.K_UP]:
            self.velocity.y = -300

        self.x += self.velocity.x * deltaTime

        for gObject in self.parentScene.objects:
            if gObject == self:
                continue
            if self.boundaries.colliderect(gObject.boundaries) and gObject.solid:
                if self.velocity.x > 0:
                    self.x = gObject.boundaries.left - self.width
                elif self.velocity.x < 0:
                    self.x = gObject.boundaries.right
                self.velocity.x = 0

        self.y += self.velocity.y * deltaTime

        for gObject in self.parentScene.objects:
            if gObject == self:
                continue
            if self.boundaries.colliderect(gObject.boundaries) and gObject.solid:
                if self.velocity.y > 0:
                    self.y = gObject.boundaries.top - self.rect.height
                elif self.velocity.y < 0:
                    self.y = gObject.boundaries.bottom - self.rect.height + self.height
                self.velocity.y = 0

        for gObject in self.parentScene.objects:
            if self.rect.colliderect(gObject.rect) and isinstance(gObject, MemeCoin):
                self.parentScene.removeObject(gObject)
                self.parentScene.points += 1
                self.parentScene.pointLabel.setText("Point: " + str(self.parentScene.points))

        self.velocity.x = 0
        self.velocity.y = 0

    def draw(self, display):
        pass

    @property
    def boundaries(self):
        return pygame.Rect(self.x, self.y + self.rect.height - self.height, self.width, self.height)