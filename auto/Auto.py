from threading import Thread
from subsystems.Mecanum import base

class Auto:
    def __init__(self) -> None:
        self.running = False
        self.thread = Thread(target=self.loop)
        self.stages = [self.stage1, self.stage2, self.stage3]

    def start(self):
        self.running = True
        self.thread.start()

    def quit(self):
        self.running = False

    def loop(self):
        while self.running:
            pass

    def stage1(self):
        pass

    def stage2(self):
        pass

    def stage3(self):
        pass