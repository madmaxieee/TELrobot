from threading import Thread
import numpy as np
from subsystems import base
from tel_image import findDoorCenter
from config import params


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
        center = np.array(params["cam_size"]) / 2