from threading import Thread
import sys


class Auto:
    def __init__(self) -> None:
        self.running = False
        self.thread = Thread(target=self.loop)

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
