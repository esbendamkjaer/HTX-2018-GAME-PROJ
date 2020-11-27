import pygame

class Scene:
    def __init__(self, game):
        self.sprites = pygame.sprite.Group()

        self.TILESIZE = 16

        self.game = game
        self.keybindings = {}
        self.objects = []

    def update(self, deltaTime):
        self.sprites.update(deltaTime)
        '''for object in self.objects:
            object.update(deltaTime)'''

    def draw(self, display):
        for object in self.objects:
            object.draw(display)

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

    def addObject(self, object):
        self.objects.append(object)

    def removeObject(self, object):
        self.objects.remove(object)
        self.sprites.remove(object)
