from threading import Thread
import pygame
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
        # self.thread.start()

    def quit(self) -> None:
        self.running = False

    def loop(self) -> None:
        while self.running:
            pass

    def readCam(self) -> None:
        _, self.raw_img = camera.read()
        return self.raw_img

    def getSurface(self):
        frame = cv.cvtColor(self.raw_img, cv.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        return frame

    def streamVideo(self):
        while self.running:
            t0 = time.perf_counter()
            _, frame = camera.read()
            cv.imshow('camera', frame)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    vision = Vision()
    running = True
    while running:
        screen.fill(0)  # set pygame screen to black
        vision.readCam()
        frame = vision.getSurface()
        screen = screen.blit(frame, (0, 0))
        print(f'{screen.__class__}')
        pygame.display.flip()
        for event in pygame.event.get():  # process events since last loop cycle
            if event.type == KEYDOWN:
                running = False
    pygame.quit()
    cv.destroyAllWindows()
