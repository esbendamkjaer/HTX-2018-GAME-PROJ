import pygame


class GameHandler:

    def __init__(self, game):
        self.currentScene = None
        self.game = game
        self.keybindings = {}
        self.paused = True



    def update(self, deltaTime):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key in self.keybindings:
                    for func in self.keybindings[event.key]:
                        func()
                if self.currentScene is not None:
                    if event.key in self.currentScene.keybindings:
                        for func in self.currentScene.keybindings[event.key]:
                            func()

        if self.currentScene is not None:
            self.currentScene.update(deltaTime)

    def draw(self, display):

        if self.currentScene is not None:
            self.currentScene.draw(display)

    def setScene(self, scene):
        self.currentScene = scene

    def addKeyBinding(self, key, func):
        if not key in self.keybindings:
            self.keybindings[key] = [func]
        else:
            self.keybindings[key].append(func)

    def removeKeyBinding(self, key, func):
        if key in self.keybindings:
            if len(self.keybindings[key]) > 1:
                self.keybindings[key].remove(func)
            else:
                self.keybindings.pop(key)

    def endGame(self):
        pass
