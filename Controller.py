import pygame

from Mecanum import Mecanum

base = Mecanum()

commands = {
    pygame.K_w: lambda _: base.cartDrive((1, 0)),
    pygame.K_a: lambda _: base.cartDrive((0, -1)),
    pygame.K_s: lambda _: base.cartDrive((-1, 0)),
    pygame.K_d: lambda _: base.cartDrive((0, 1)),
}

pygame.init()

screen_res = (640, 480)

screen = pygame.display.set_mode(screen_res)

running = True

while running:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
            running = False

    for key in commands.keys():
        if pressed_keys[key]:
            commands[key]()

pygame.quit()
