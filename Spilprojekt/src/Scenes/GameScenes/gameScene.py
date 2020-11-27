from src.Scenes.scene import Scene
from src.Objects.Entities.player import Player
from src.Objects.Statics.wall import Wall
from src.camera import Camera
from src.map import TiledMap
from src.Objects.Entities.teacher import Teacher
from src.Objects.Entities.subject import Subject
from src.Scenes.GameScenes.fightScene import FightScene
from src.Objects.Entities.GUIItems.textElement import TextElement
from src.utils import Utils
from src.utils import Timer
from src.Objects.Statics.memeCoin import MemeCoin
from src.Scenes.GameScenes.endScene import EndScene
import random
import pygame


class GameScene(Scene):

    def __init__(self, game):
        super().__init__(game)

        self.camera = Camera(self, 100, 100)

        self.map = TiledMap("res/Ze_bane.tmx")
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.rooms = []

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)
                self.addObject(self.player)
            elif tile_object.name == "wall":
                self.addObject(Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
            elif tile_object.name == "room":
                self.rooms.append(tile_object)

        self.timer = Timer(120, self.endGame)
        self.questionTimer = Timer(10, self.askQuestions)

        self.memeCoinTimer = Timer(1, self.spawnMemeCoin)

        self.timeLabel = TextElement(self, Utils.secToTimeText(self.timer.time), 60, 30, (255, 255, 255), 30)

        self.points = 0

        self.pointLabel = TextElement(self, "Points: " + str(self.points), self.game.display_width/2, 30, (255, 255, 255), 30)

    def update(self, deltaTime):
        super().update(deltaTime)
        self.memeCoinTimer.update(deltaTime)
        self.questionTimer.update(deltaTime)
        self.timer.update(deltaTime)

        self.player.update(deltaTime)
        self.camera.update(self.player)

        self.timeLabel.setText(Utils.secToTimeText(self.timer.time - self.timer.counter))
        self.pointLabel.setText("Points: " + str(self.points))

    def draw(self, display):
        display.fill((0, 0, 0))
        display.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        for sprite in self.sprites:
            display.blit(sprite.image, self.camera.apply(sprite))

        self.timeLabel.draw(display)
        self.pointLabel.draw(display)

    def askQuestions(self):
        self.game.gameHandler.setScene(FightScene(self.game, self, self.player, Teacher(self, self.player, random.choice(list(Subject)))))

    def endGame(self):
        self.game.gameHandler.setScene(EndScene(self.game, self))

    def spawnMemeCoin(self):
        room = random.choice(self.rooms)
        memeCoin = MemeCoin(self, room.x + int(random.random() * room.width), room.y + int(random.random() * room.height))
        self.addObject(memeCoin)

