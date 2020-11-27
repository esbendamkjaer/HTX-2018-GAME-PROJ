import pygame
from src.Objects.Entities.entity import Entity
from src.Objects.Entities.GUIItems.textElement import TextElement
from src.utils import Utils


class MenuButton(Entity):

    def __init__(self, parentScene, text, action, x, y, width, height, direction=1):
        super().__init__(parentScene)

        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect()

        self.text = text
        self.action = action
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image.fill((100, 100, 255))

        self.textElement = TextElement(self.parentScene, self.text, self.width / 2, self.height / 2, (255, 255, 255), 30, font="font.TTF")

        self.textElement.draw(self.image)

        self.animationTime = 0.2
        self.distance = 50

        self.a = -6 * (self.distance / (self.animationTime ** 3))
        self.b = 6 * (self.distance / (self.animationTime ** 2))

        self.timeSum = 0

        self.animationStarted = False

        self.direction = direction
        self.reverse = 1
        self.distanceMoved = 0

        self.clicked = False

    def update(self, deltaTime):
        super().update(deltaTime)
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos[0], mousePos[1]):
            if not self.animationStarted:
                self.animationStarted = True
            else:
                self.reverse = 1

            click = pygame.mouse.get_pressed()

            if click[0] == 1 and not self.clicked:
                self.clicked = True
                self.action()
            elif click[0] == 0:
                self.clicked = False

        else:
            if self.animationStarted and self.reverse == 1:
                self.reverse = -1

        if self.animationStarted:
            if self.timeSum > self.animationTime and self.reverse == 1:
                self.timeSum = self.animationTime
                self.x += (self.distance - self.distanceMoved) * self.direction
                self.distanceMoved = self.distance
                self.x = round(self.x, 10)
                self.velocity.x = 0

            elif self.timeSum < 0 and self.reverse == -1:
                self.x -= self.distanceMoved * self.direction
                self.distanceMoved = 0
                self.x = round(self.x, 10)
                self.timeSum = 0
                self.animationStarted = False
                self.reverse = 1
                self.velocity.x = 0

            elif self.timeSum < self.animationTime or self.reverse == -1:
                self.timeSum += deltaTime * self.reverse

                self.velocity.x = self.a * (self.timeSum ** 2) + self.b * self.timeSum
                self.x += self.reverse * self.velocity.x * deltaTime * self.direction

                self.distanceMoved += self.velocity.x * deltaTime * self.reverse

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, display):
        super().draw(display)
