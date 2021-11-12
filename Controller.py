import pygame

# from Mecanum import base

commands = {
    # pygame.K_w: lambda : base.cartDrive((1, 0)),
    # pygame.K_a: lambda : base.cartDrive((0, -1)),
    # pygame.K_s: lambda : base.cartDrive((-1, 0)),
    # pygame.K_d: lambda : base.cartDrive((0, 1)),
    pygame.K_j: lambda: print('j'),
    pygame.K_k: lambda: print('k'),
}


def handleController(pressed_keys):
    for key in commands.keys():
        if pressed_keys[key]:
            commands[key]()
