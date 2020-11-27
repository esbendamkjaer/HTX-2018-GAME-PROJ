
class Utils:
    @staticmethod
    def text_object(text, color, font):
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        return textSurface, textRect

    @staticmethod
    def secToTimeText(time):
        minutes = int(time/60)
        time -= minutes * 60
        seconds = int(time)
        time -= seconds
        return str(minutes) + ":" + str(seconds)

class Timer:
    def __init__(self, time, action):
        self.time = time
        self.action = action
        self.counter = 0

    def update(self, deltaTime):
        self.counter += deltaTime

        while self.counter >= self.time:
            self.action()
            self.counter -= self.time
