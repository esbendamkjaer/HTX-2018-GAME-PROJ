from src.Objects.Entities.entity import Entity
import pygame

class GUIContainer(Entity):

    def __init__(self, parentScene, gap):
        super().__init__(parentScene)
        self.gap = gap
        self.menuItems = []

    def update(self, deltaTime):
        for menuItem in self.menuItems:
            menuItem.update(deltaTime)

    def draw(self, display):
        for menuItem in self.menuItems:
            menuItem.draw(display)

    def addObject(self, menuItem):
        if len(self.menuItems) <= 0:
            menuItem.y += self.height + self.y
        else:
            menuItem.y += self.height + self.gap + self.y

        menuItem.x += self.x
        self.menuItems.append(menuItem)
        self.updateHeight()

    def removeObject(self, menuItem):
        self.menuItems.remove(menuItem)
        self.updateWidth()

    def updateHeight(self):
        if len(self.menuItems) <= 0: return 0
        return max((menuItem.height + menuItem.pos.y) for menuItem in self.menuItems) - min(menuItem.pos.y for menuItem in self.menuItems)

    def updateWidth(self):
        if len(self.menuItems) <= 0: return 0
        return max((menuItem.width + menuItem.pos.x) for menuItem in self.menuItems) - min(menuItem.pos.x for menuItem in self.menuItems)

    @property
    def width(self):
        return self.updateWidth()

    @property
    def height(self):
        return self.updateHeight()

    @width.setter
    def width(self, value):
        pass

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        if len(self.menuItems) <= 0: return self.pos.x
        return min(menuItem.pos.x for menuItem in self.menuItems)

    @x.setter
    def x(self, value):
        for menuItem in self.menuItems:
            menuItem.x = menuItem.pos.x - self.pos.x + value
        self.pos.x = value

    @property
    def y(self):
        if len(self.menuItems) <= 0: return self.pos.y
        return min(menuItem.pos.y for menuItem in self.menuItems)

    @y.setter
    def y(self, value):
        for menuItem in self.menuItems:
            menuItem.y = menuItem.pos.y - self.pos.y + value
        self.pos.y = value
