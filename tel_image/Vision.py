from threading import Thread
# import pygame
import cv2 as cv
import numpy as np
from pygame.locals import *
import time


# from config import params

camera_index = 0
camera = cv.VideoCapture(camera_index)
# frame_w, frame_h = params["cam_size"]
frame_w, frame_h = 640, 480
camera.set(cv.CAP_PROP_FRAME_WIDTH, frame_w)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, frame_h)


class Vision:
    def __init__(self) -> None:
        self.running = False
        # self.thread = Thread(target=self.loop)
        self.raw_img = None
        self.ticks = 0
        self.video_thread = Thread(target=self.streamVideo)

    def start(self) -> None:
        self.running = True
        self.video_thread.start()

    def quit(self) -> None:
        self.running = False
        camera.release()
        cv.destroyAllWindows()

    def readCam(self) -> None:
        _, self.raw_img = camera.read()
        return self.raw_img

    def streamVideo(self):
        t0 = time.time()
        while self.running:
            while time.time() - t0 < self.ticks / 15:
                pass
            _, frame = camera.read()
            frame = cv.resize(frame, (320, 240))
            cv.imshow('camera', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            self.ticks += 1
        self.quit()


if __name__ == '__main__':
    vision = Vision()
    vision.start()
