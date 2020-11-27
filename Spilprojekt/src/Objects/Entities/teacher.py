from src.Objects.Entities.subject import Subject
import pygame


class Teacher:

    def __init__(self, parentScene, player, subject):
        self.parentScene = parentScene

        self.player = player

        self.subject = subject

        self.questions = []
        self.answers = []

        self.questionFiles = {
            Subject.MATH: "mat/mat.txt",
            Subject.PROGRAMMING: "prog/prog.txt",
            Subject.PHYSICS: "fys/fys.txt"
        }

        with open("res/questions/" + self.questionFiles[self.subject], "r") as f:
            lines = f.readlines()
            for qi in range(0, int(len(lines)/5)):
                question = lines[qi * 5].strip()
                self.questions.append(question)
                ans = []
                for ai in range(1, 5):
                    ans.append(lines[qi * 5 + ai].strip())
                self.answers.append(ans)