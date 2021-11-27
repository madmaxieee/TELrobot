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

    def start(self):
        self.running = True
        self.input_thread.start()
        vision.start()

    def quit(self):
        self.running = False
        pygame.quit()
        vision.quit()

    def handleInput(self):
        while self.running:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    self.quit()

            handleController(pressed_keys=pressed_keys)
