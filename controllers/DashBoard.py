import pygame
from threading import Thread
from time import perf_counter, sleep

from tel_image import vision 

from .Controller import handleController
from config import params

window_size = params["cam_size"]


class DashBoard:
    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode(window_size)

        self.running = False
        self.input_thread = Thread(target=self.handleInput)
        self.camera_thread = Thread(target=self.handleCamera)

    def start(self):
        self.running = True
        self.input_thread.start()
        self.camera_thread.start()

    def quit(self):
        self.running = False
        pygame.quit()

    def handleInput(self):
        while self.running:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    self.quit()

            handleController(pressed_keys=pressed_keys)

    def handleCamera(self):
        ticks = 0
        t0 = perf_counter()
        while self.running:
            # frame rate control
            # while perf_counter()-t0 < ticks / 30:
            #     pass
            # ticks += 1
            vision.readCam()
            self.window = self.window.blit(vision.getSurface(), (0, 0))
            pygame.display.flip()
