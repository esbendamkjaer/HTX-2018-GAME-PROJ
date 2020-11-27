import pygame

from src.Objects.Entities.GUIItems.textElement import TextElement
from src.Objects.Entities.entity import Entity


class GameButton(Entity):

    def __init__(self, parentScene, text, action, x, y, width, height):
        super().__init__(parentScene)
        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect()

        self.color = (100, 100, 255)

        self.text = text
        self.action = action
        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.font = pygame.font.Font("res/font.TTF", 30)

        self.textElement = TextElement(self.parentScene, self.text, self.width / 2, self.height / 2, (255, 255, 255), 15)

        self.clicked = False

    def update(self, deltaTime):
        super().update(deltaTime)
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos[0], mousePos[1]):
            self.color = (0, 255, 0)

            click = pygame.mouse.get_pressed()

            if click[0] == 1 and not self.clicked:
                self.clicked = True
                self.action()
            elif click[0] == 0:
                self.clicked = False
        else:
            self.color = (255, 0, 0)

    def draw(self, display):
        super().draw(display)
        self.image.fill(self.color)
        self.textElement.draw(self.image)