import cv2 as cv
import numpy

camera_index = 0
camera = cv.VideoCapture(camera_index)
camera.set(3, 640)
camera.set(4, 480)
_, frame = camera.read()
cv.imwrite('./photo5.jpg', frame)

# def getCamFrame(camera):
#     _, frame = camera.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#     frame = numpy.rot90(frame)
#     # I think the color error lies in this line?
#     frame = pygame.surfarray.make_surface(frame)
#     return frame


# def blitCamFrame(frame, screen):
#     screen.blit(frame, (0, 0))
#     print(f'{screen.__class__}')
#     return screen

# This shows an image weirdly...
# screen_width, screen_height = 640, 480
# screen = pygame.display.set_mode((screen_width, screen_height))
# print(screen.__class__)

# running = True

# while running:
#     screen.fill(0)  # set pygame screen to black
#     frame = getCamFrame(camera)
#     screen = blitCamFrame(frame, screen)
#     pygame.display.flip()
#     for event in pygame.event.get():  # process events since last loop cycle
#         if event.type == QUIT or event.type == KEYDOWN:
#             running = False
# pygame.quit()
# cv.destroyAllWindows()
