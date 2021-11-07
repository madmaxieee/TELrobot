import global_variables as gv
import pygame
from enemy import *
from player import *
from score import *

pygame.init()

# create window
screen = pygame.display.set_mode(screen_dimensions)

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background.jpg')

# game loop variables
running = True
frame_count = 0

num_of_enemies = 6
spaceship = player()
enemies = [enemy() for i in range(num_of_enemies)]

# game loop
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        spaceship.handle_event(event)

    spaceship.move()
    for i in range(len(enemies)):
        enemies[i].move()
        j = 0
        while j < len(spaceship.bullets):
            if spaceship.bullets[j].hit(enemies[i]):
                spaceship.bullets.pop(j)
                enemies.pop(i)
                enemies.append(enemy())
            j += 1

    screen.blit(background, (0, 0))

    # blit components
    for foe in enemies:
        foe.blit(screen)
    spaceship.blit(screen)

    show_score(screen, gv.score)

    # frame rate controller
    while pygame.time.get_ticks() < frame_count * 1000 / 120:
        pass

    # update screen
    pygame.display.update()
    frame_count += 1

pygame.quit()
