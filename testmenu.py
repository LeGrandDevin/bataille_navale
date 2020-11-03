import sys

import pygameclass.menu as Menu
import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

menu = Menu.Menu(pygame.image.load("images/quitButton.png"), pygame.image.load("images/playButton.png"), pygame.image.load("images/bataillenavale.jpg"))

# Game loop.
while True:
    quitbutton = screen.blit(menu.quitbutton.image, (800, 50))
    button = []
    button.append(quitbutton)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if button[0].collidepoint(pygame.mouse.get_pos()):
                quit()


    # Update.

    # Draw.
    fond = menu.fond.convert()
    screen.blit(fond, (0, 0))
    screen.blit(menu.quitbutton.image, (800, 50))
    screen.blit(menu.playbutton.image, (800, 200))

    pygame.display.flip()
    fpsClock.tick(fps)