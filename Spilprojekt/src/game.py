import pygame
from src.gameHandler import GameHandler
from src.Scenes.menuScene import MainScene


class Game:
    def __init__(self):
        pygame.init()

        self.TILE_SIZE = 16

        self.display_width = 1250
        self.display_height = 720
        self.title = "Spillet"

        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.running = True

        self.tps = 60

        self.gameHandler = GameHandler(self)
        self.gameHandler.setScene(MainScene(self))

    def update(self, deltaTime):
        self.gameHandler.update(deltaTime)

    def draw(self, display):
        self.gameHandler.draw(display)

    def start(self):

        lastTime = pygame.time.get_ticks()

        while self.running:
            now = pygame.time.get_ticks()
            deltaTime = (now - lastTime) / 1000.0
            self.update(deltaTime)
            self.draw(self.display)
            pygame.display.update()
            self.clock.tick(self.tps)
            lastTime = now

    def quitGame(self):
        pygame.quit()
        quit()

    def setTicksPerSecond(self, tps):
        self.tps = tps
