from src.Objects.Entities.GUIItems.GUIContainer import GUIContainer
from src.Objects.Entities.GUIItems.menuButton import MenuButton
from src.Scenes.GameScenes.gameScene import GameScene
from src.Scenes.scene import Scene
import pygame

class MainScene(Scene):

    def __init__(self, game):
        super().__init__(game)

        self.playMenuButton = MenuButton(self, "Play", self.playMenuButtonAction, 0, 0, 300, 80, -1)
        self.exitMenuButton = MenuButton(self, "Exit", self.exitMenuButtonAction, 0, 0, 300, 80, -1)

        self.menuButtonContainer = GUIContainer(self, 20)
        self.menuButtonContainer.addObject(self.playMenuButton)
        self.menuButtonContainer.addObject(self.exitMenuButton)

        self.menuButtonContainer.y = game.display_height - self.menuButtonContainer.height - 20
        self.menuButtonContainer.x = game.display_width - self.menuButtonContainer.width + 50
        self.addObject(self.menuButtonContainer)

        self.game.gameHandler.addKeyBinding(pygame.K_ESCAPE, self.game.quitGame)

    def update(self, deltaTime):
        super().update(deltaTime)

    def draw(self, display):
        super().draw(display)
        display.fill((84, 25, 229))
        self.sprites.draw(display)

    def playMenuButtonAction(self):
        self.game.gameHandler.setScene(GameScene(self.game))

    def exitMenuButtonAction(self):
        self.game.quitGame()
