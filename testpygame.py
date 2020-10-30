import pygame
import sys
import pygameclass.casegraphic
import pygameclass.Grillegraphic
import Partie
import pygameclass.boatgraphic

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


torpilleur = pygameclass.boatgraphic.Boatgraphic(100, 500, pygame.image.load("images/torpilleur 2 cases.png"))
sous_marin = pygameclass.boatgraphic.Boatgraphic(175, 500, pygame.image.load("images/sous_marin 3 cases.png"))
porte_avion = pygameclass.boatgraphic.Boatgraphic(250, 500, pygame.image.load("images/porte-avion 4 cases.png"))
destroyer = pygameclass.boatgraphic.Boatgraphic(325, 500, pygame.image.load("images/destroyer 3 cases.png"))
croiseur = pygameclass.boatgraphic.Boatgraphic(400, 500, pygame.image.load("images/croiseur 5 cases.png"))
casetest = pygameclass.Grillegraphic.grillegraphic(screen, 50, 50)
casetest2 = pygameclass.Grillegraphic.grillegraphic(screen, 700, 50)
team = []
team.append(torpilleur)
team.append(sous_marin)
team.append(porte_avion)
team.append(destroyer)
team.append(croiseur)
numberselected = -1

# Game loop.
while True:
    sprites = []
    screen.fill((4, 129, 220))
    casetest.drawgrid()
    casetest2.drawgrid()
    sprites.append(screen.blit(torpilleur.sprite, torpilleur.coord()))
    sprites.append(screen.blit(sous_marin.sprite, sous_marin.coord()))
    sprites.append(screen.blit(porte_avion.sprite, porte_avion.coord()))
    sprites.append(screen.blit(destroyer.sprite, destroyer.coord()))
    sprites.append(screen.blit(croiseur.sprite, croiseur.coord()))
    pygame.display.flip()
    x, y = pygame.mouse.get_pos()
    gx, gy = casetest.coordScreenToGrid(x, y)
    gx2, gy2 = casetest2.coordScreenToGrid(x, y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if pygameclass.boatgraphic.Boatgraphic.isselected:
                selected.reinitializecoord()
                pygameclass.boatgraphic.Boatgraphic.isselected = False

            for j in range(5):
                if numberselected == j:
                    numberselected = -1
                    print("test")
                    continue
                if sprites[j].collidepoint(pygame.mouse.get_pos()):
                    selected = team[j]
                    if pygameclass.boatgraphic.Boatgraphic.isselected:
                        numberselected = j
                    pygameclass.boatgraphic.Boatgraphic.isselected = True
                    print("bateau :", j)

            if casetest.inGrid(x, y):
                p = 1 if p == 2 else 2
                g = game.round(p, gx, gy)
            print(x, y)
            print('le 1 :::', gx, gy)
            print('le 2 :::', gx2, gy2)
            print('last coord', casetest2.lastcoord)

    if pygameclass.boatgraphic.Boatgraphic.isselected:
        selected.newcoord(pygame.mouse.get_pos())

    if casetest.inGrid(x,y):
        casetest.gridover(gx, gy)
        
    else:
        casetest.gridout(casetest.lastcoord[0], casetest.lastcoord[1])

    if casetest2.inGrid(x,y):
        casetest2.gridover(gx2, gy2)
    else:
        casetest2.gridout(casetest2.lastcoord[0], casetest2.lastcoord[1])

    # Update.

    # Draw.

    fpsClock.tick(fps)
