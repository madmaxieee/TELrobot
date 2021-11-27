from threading import Thread
import numpy as np
from subsystems import base
from tel_image import findDoorCenter, vision
from config import params
from time import sleep

center_x = params["cam_size"][0] / 2


class Auto:
    def __init__(self) -> None:
        self.running = False
        self.thread = Thread(target=self.loop)
        # self.stages = [self.stage1, self.stage2, self.stage3]
        self.door_ind = 0
        self.center_list = []
        self.avg_center = -1
        self.onTrack = False

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
        if self.door_ind > 2:
            base.cartDrive((1, 0))

        doors = ('red', 'green', 'blue')
        door_center = findDoorCenter(vision.readCam(), doors[self.door_ind])
        if len(self.center_list) == 0:
            for _ in range(10):
                while True:
                    door_center = findDoorCenter(
                        vision.readCam(), doors[self.door_ind])
                    print(door_center)
                    if door_center[0] != -1:
                        self.center_list.append(door_center[0])
                        break
            self.avg_center = sum(self.center_list) / len(self.center_list)
        elif len(self.center_list) == 10 and not self.onTrack:
            self.center_list = []
            if self.avg_center < 300:
                base.cartDrive((0, -1))
            elif self.avg_center > 340:
                base.cartDrive((0, 1), spin=0.2)
            else:
                base.cartDrive((1, 0))
            sleep(0.2)
            self.onTrack = True
        elif self.onTrack:
            base.cartDrive((1, 0))
            sleep(5)
            self.door_ind += 1
            self.onTrack = False

    def test(self):
        while True:
            t = int(input('input time: '))/10
            base.cartDrive((0, 1))
            sleep(t)
            base.clearDriveSpeeds()

            base.cartDrive((0, -1))
            sleep(t)
            base.clearDriveSpeeds()
