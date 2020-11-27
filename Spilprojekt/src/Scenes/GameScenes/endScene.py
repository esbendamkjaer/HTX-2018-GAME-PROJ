from src.Objects.Entities.GUIItems.textElement import TextElement
from src.Scenes.scene import Scene

class EndScene(Scene):

    def __init__(self, game, gameScene):
        super().__init__(game)
        self.pointLabel = TextElement(self, "Slutscore: " + str(gameScene.points), self.game.display_width/2, self.game.display_height/2, (255, 255, 255), 30)
        self.addObject(self.pointLabel)

    def update(self, deltaTime):
        pass

    def draw(self, display):
        display.fill((84, 25, 229))
        super().draw(display)