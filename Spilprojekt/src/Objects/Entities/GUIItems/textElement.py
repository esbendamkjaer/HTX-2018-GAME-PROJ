from src.Objects.Entities.entity import Entity
from src.utils import Utils
import pygame


class TextElement(Entity):

    def __init__(self, parentScene, text, x, y, color, fontSize, font="pixelVerdana.TTF"):
        super().__init__(parentScene)

        self.font = pygame.font.Font("res/" + font, fontSize)

        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.fontsize = fontSize
        self.parentScene = parentScene
        self.setText(text)


    def setText(self, text):
        self.text = text
        self.textSurface, self.textRect = Utils.text_object(text, self.color, self.font)
        self.textRect.center = (self.x, self.y)

    def update(self, deltaTime):
        pass

    def draw(self, display):
        display.blit(self.textSurface, self.textRect)
