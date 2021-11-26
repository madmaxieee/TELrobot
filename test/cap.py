import pygame
from pygame.locals import *
import cv2
import numpy

camera_index = 0
camera = cv2.VideoCapture(camera_index)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# This shows an image the way it should be
# cv2.namedWindow("w1")
# retval, frame = camera.read()
# if not color:
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.flip(frame, 1, frame)  # mirror the image
# cv2.imshow("w1", frame)

# This shows an image weirdly...
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))


def getCamFrame(camera):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = numpy.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    return frame


def blitCamFrame(frame, screen):
    screen.blit(frame, (0, 0))
    return screen


running = True
while running:
    screen.fill(0)  # set pygame screen to black
    frame = getCamFrame(camera)
    screen = blitCamFrame(frame, screen)
    pygame.display.flip()
    for event in pygame.event.get():  # process events since last loop cycle
        if event.type == KEYDOWN:
            running = False

pygame.quit()
cv2.destroyAllWindows()
