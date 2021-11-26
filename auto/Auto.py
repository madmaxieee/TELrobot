from threading import Thread
import numpy as np
from subsystems import base
from tel_image import findDoorCenter, vision
from config import params

center_x = params["cam_size"][0] / 2

class Auto:
    def __init__(self) -> None:
        self.running = False
        self.thread = Thread(target=self.loop)
        # self.stages = [self.stage1, self.stage2, self.stage3]

    def start(self):
        self.running = True
        self.thread.start()

    def quit(self):
        self.running = False

    def loop(self):
        while self.running:
            self.stage1()
            base.clearDriveSpeeds()

    def stage1(self):
        doors = ['red', 'green', 'blue']
        door_center = findDoorCenter(vision.readCam(), doors[0])
        if door_center[0] < 300:
            base.cartDrive((0, 1), spin=1)
        elif door_center[0] > 340:
            base.cartDrive((0, -1), spin=-1)
        else:
            base.cartDrive((1, 0))
