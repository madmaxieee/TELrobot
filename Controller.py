import pygame

from Mecanum import base

commands = {
    pygame.K_w: lambda: base.cartDrive((1, 0)),
    pygame.K_a: lambda: base.cartDrive((0, -1)),
    pygame.K_s: lambda: base.cartDrive((-1, 0)),
    pygame.K_d: lambda: base.cartDrive((0, 1)),
    pygame.K_q: lambda: base.cartDrive(spin=-1),
    pygame.K_e: lambda: base.cartDrive(spin=1),
    pygame.K_SPACE: lambda: base.stop(),
}


def handleController(pressed_keys):
    isPressing = False
    for key in commands.keys():
        if pressed_keys[key]:
            commands[key]()
            isPressing = True

    if not isPressing:
        base.stop()

    base.clearDriveSpeeds()
