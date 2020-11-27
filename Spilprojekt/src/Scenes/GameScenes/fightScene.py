from src.Scenes.scene import Scene
from src.Objects.Entities.GUIItems.gameButton import GameButton
import random
from src.Objects.Entities.GUIItems.textElement import TextElement
from src.utils import Utils
from src.Objects.Entities.GUIItems.imageElement import ImageElement
from src.Objects.Entities.subject import Subject
import pygame

class FightScene(Scene):

    def __init__(self, game, gameScene, player, teacher):
        super().__init__(game)
        self.gameScene = gameScene
        self.player = player
        self.teacher = teacher

        self.timer = gameScene.timer
        self.timeLabel = TextElement(self, Utils.secToTimeText(self.timer.time - self.timer.counter), 60, 30, (0, 0, 0), 30)

        self.numberOfQuestions = 3
        self.currentQuestion = 0

        self.questions = []
        self.answers = []
        self.correctAnswers = []

        for i in range(0, self.numberOfQuestions):
            index = random.randint(0, len(self.teacher.questions)-1)
            self.questions.append(self.teacher.questions[index])
            self.answers.append(self.teacher.answers[index].copy())

        for answer in self.answers:
            self.correctAnswers.append(answer[0])

        self.buttons = []
        for i in range(0, 2):
            for k in range(0, 2):
                button = GameButton(self, "", None, (self.game.display_width / 2 + 10) * k + 5, self.game.display_height - 90 * (i + 1), self.game.display_width / 2 - 10 - 10, 80)
                self.buttons.append(button)
                self.addObject(button)

        self.textElement = TextElement(self, "", self.game.display_width / 2, 100, (0, 0, 0), 30)
        self.addObject(self.textElement)

        self.pointLabel = TextElement(self, "Points: " + str(self.gameScene.points), self.game.display_width/2, 30, (0, 0, 0), 30)

        self.teacherImages = {
            Subject.MATH: "Steffen.png",
            Subject.PHYSICS: "Jesper.png",
            Subject.PROGRAMMING: "David.png"
        }

        self.teacherImage = ImageElement(self, 0, 0, "res/img/" + self.teacherImages[self.teacher.subject])

        self.teacherImage.x = self.game.display_width / 2 - self.teacherImage.rect.width / 2
        self.teacherImage.y = self.game.display_height / 2 - self.teacherImage.rect.height / 2
        self.nextQuestion()

    def finished(self):
        self.game.gameHandler.setScene(self.gameScene)

    def nextQuestion(self):
        if self.currentQuestion >= self.numberOfQuestions:
            self.finished()
            return

        random.shuffle(self.answers[self.currentQuestion])

        for i in range(0, 2):
            for k in range(0, 2):
                action = self.wrong
                if self.answers[self.currentQuestion][2 * i + k] == self.correctAnswers[self.currentQuestion]:
                    action = self.correct
                button = self.buttons[2 * i + k]
                button.action = action
                button.textElement.setText(self.answers[self.currentQuestion][2 * i + k])
        self.textElement.setText(self.questions[self.currentQuestion])

        self.currentQuestion += 1

    def update(self, deltaTime):
        super().update(deltaTime)
        self.timer.update(deltaTime)
        self.timeLabel.setText(Utils.secToTimeText(self.timer.time - self.timer.counter))
        self.pointLabel.setText("Points: " + str(self.gameScene.points))

    def draw(self, display):
        display.fill((255, 255, 255))
        super().draw(display)

        self.timeLabel.draw(display)

        self.sprites.draw(display)

        self.pointLabel.draw(display)

    def wrong(self):
        self.gameScene.points -= 10
        self.nextQuestion()

    def correct(self):
        self.gameScene.points += 5
        self.nextQuestion()