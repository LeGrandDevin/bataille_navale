import pygame
import sys
import pygameclass.casegraphic
import pygameclass.Grillegraphic
import Partie

import math
from pygame.locals import *

pygame.init()

# load
fps = 180
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
game = Partie.Partie(10)
p = 2
g = True




# Variables

casetest = pygameclass.Grillegraphic.grillegraphic(screen,50 ,50)
casetest2 = pygameclass.Grillegraphic.grillegraphic(screen,700 ,50)

# Game loop.
while True:
    screen.fill((4, 129, 220))
    casetest.drawgrid()
    casetest2.drawgrid()
    x, y = pygame.mouse.get_pos()
    gx, gy = casetest.coordScreenToGrid(x, y)
    gx2, gy2 = casetest2.coordScreenToGrid(x, y)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if casetest.inGrid(x,y):
                p = 1 if p == 2 else 2
                g = game.round(p,gx,gy)
            print(x, y)
            print('le 1 :::' , gx, gy)
            print('le 2 :::' , gx2, gy2)
            print('last coord' , casetest2.lastcoord)

    if casetest.inGrid(x,y):
        casetest.gridover(gx, gy)
        
    else:
        casetest.gridout(casetest.lastcoord[0],casetest.lastcoord[1])

    if casetest2.inGrid(x,y):
        casetest2.gridover(gx2, gy2)
    else:
        casetest2.gridout(casetest2.lastcoord[0],casetest2.lastcoord[1])

    # Update.

    # Draw.

    pygame.display.flip()
    fpsClock.tick(fps)
