import sys
import pygameclass.casegraphic
import pygameclass.Grillegraphic

import math
import pygame
from pygame.locals import *

pygame.init()

# load
fps = 180
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
# Variables
casetest = pygameclass.Grillegraphic.grillegraphic(screen)

# Game loop.
while True:
    screen.fill((4, 129, 220))
    casetest.drawgrid()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x, y = pygame.mouse.get_pos()
    gx, gy = casetest.coordScreenToGrid(x, y)

    if pygame.mouse.get_pressed()[0]:
        print(x, y)
        print(gx, gy)

    casetest.gridover(gx, gy)
    # Update.

    # Draw.

    pygame.display.flip()
    fpsClock.tick(fps)
