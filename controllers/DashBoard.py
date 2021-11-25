import pygame
from threading import Thread

from Controller import handleController

window_size = (640, 480)


class DashBoard:
    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode(window_size)
        self.running = False
        self.thread = Thread(target=self.handleInput)

    def start(self):
        self.running = True
        self.thread.start()

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
