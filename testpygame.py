import pygame
import sys
import pygameclass.casegraphic
import pygameclass.Grillegraphic
import Partie
import pygameclass.menu as Menu
import pygameclass.boatgraphic as boatGraphic

import math
from pygame.locals import *

pygame.init()

# load
fps = 180
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
#menu = ....(mettre le menu ici)
game = Partie.Partie(10)
p = 2
g = True




# Variables


torpilleur = boatGraphic.Boatgraphic(100, 550, pygame.image.load("images/torpilleur 2 cases.png"))
sous_marin = boatGraphic.Boatgraphic(175, 500, pygame.image.load("images/sous_marin 3 cases.png"))
destroyer = boatGraphic.Boatgraphic(250, 500, pygame.image.load("images/destroyer 3 cases.png"))
porte_avion = boatGraphic.Boatgraphic(325, 500, pygame.image.load("images/porte-avion 4 cases.png"))
croiseur = boatGraphic.Boatgraphic(400, 500, pygame.image.load("images/croiseur 5 cases.png"))
casetest = pygameclass.Grillegraphic.grillegraphic(screen, 50, 50)
casetest2 = pygameclass.Grillegraphic.grillegraphic(screen, 700, 50)
team = []
team.append(torpilleur)
team.append(sous_marin)
team.append(destroyer)
team.append(porte_avion)
team.append(croiseur)
numberselected = -1
orientation = True
# Game loop.
while True:
    sprites = []
    screen.fill((4, 129, 220))
    buttunStart = pygame.draw.rect(screen, (255,255,255), (560,50,40,40))
    casetest.drawgrid()
    casetest2.drawgrid()

    for boat in team:
        boat.addSquare(screen.blit(boat.sprite, boat.coord()))
    pygame.display.flip()
    x, y = pygame.mouse.get_pos()
    gx, gy = casetest.coordScreenToGrid(x, y)
    gx2, gy2 = casetest2.coordScreenToGrid(x, y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # all click event
        # right click event
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print(90 if orientation else -90)
            if boatGraphic.Boatgraphic.isselected:
                orientation = False if orientation else True
                selected.sprite = pygame.transform.rotate(selected.sprite,90 if orientation else -90)
        # left click event
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if buttunStart.collidepoint(pygame.mouse.get_pos()):
                Partie.Partie.started = True
                print("game start")

            if casetest.inGrid(x, y):
                if Partie.Partie.started:
                    p = 1 if p == 2 else 2
                    g = game.round(p, gx, gy)
                else:
                    if boatGraphic.Boatgraphic.isselected:
                        size =  (2 if numberselected < 2 else 1)
                        print("numberselected: ",numberselected, "\nsize: ",size)
                        game.placeBoat(size + numberselected ,gy,gx,orientation,1)
                        print("player 1 :")
                        game.player1.showBoard()
                print(x, y)
                print('le 1 :::', gx, gy)
                print('le 2 :::', gx2, gy2)
                print('last coord', casetest2.lastcoord)

            if boatGraphic.Boatgraphic.isselected:
                selected.reinitializecoord()
                boatGraphic.Boatgraphic.isselected = False
                if not orientation:
                    selected.sprite = pygame.transform.rotate(selected.sprite,-90)
                selected.addSquare(screen.blit(selected.sprite, selected.coord()))
                orientation = True

            for j in range(5):
                if team[j].square.collidepoint(pygame.mouse.get_pos()):
                    selected = team[j]
                    numberselected = j
                    boatGraphic.Boatgraphic.isselected = True
                    print("bateau :", numberselected)

                    

    if pygameclass.boatgraphic.Boatgraphic.isselected:
        selected.newcoord(pygame.mouse.get_pos(),orientation)

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
