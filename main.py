import pygame
import sys
import pygameclass.casegraphic
import pygameclass.Grillegraphic
import Partie
import pygameclass.boatgraphic as boatGraphic
import pygameclass.gameGraphic as gameGraphic
import pygameclass.menu as Menu

import math
from pygame.locals import *

pygame.init()

# load
fps = 180
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
game = Partie.Partie(10)
p = 1
noWin = True




# Variables
confirmButtunImage = pygame.image.load("images/confirmButton.png")
menu = Menu.Menu(pygame.image.load("images/quitButton.png"), pygame.image.load("images/playButton.png"), pygame.image.load("images/bataillenavale.jpg"))
menuBool = True

torpilleur = boatGraphic.Boatgraphic(100, 600, pygame.transform.rotate(pygame.image.load("images/torpilleur 2 cases.png"), -90))
sous_marin = boatGraphic.Boatgraphic(200, 600, pygame.transform.rotate(pygame.image.load("images/sous_marin 3 cases.png"), -90))
destroyer = boatGraphic.Boatgraphic(350, 600, pygame.transform.rotate(pygame.image.load("images/destroyer 3 cases.png"), -90))
porte_avion = boatGraphic.Boatgraphic(500, 600, pygame.transform.rotate(pygame.image.load("images/porte-avion 4 cases.png"), -90))
croiseur = boatGraphic.Boatgraphic(750, 600, pygame.transform.rotate(pygame.image.load("images/croiseur 5 cases.png"), -90))
casetest = pygameclass.Grillegraphic.grillegraphic(screen, 50, 50)
casetest2 = pygameclass.Grillegraphic.grillegraphic(screen, 700, 50)
team = []
team.append(torpilleur)
team.append(sous_marin)
team.append(destroyer)
team.append(porte_avion)
team.append(croiseur)
boatPlaced = False
ggame = gameGraphic.gameGraphic(team,screen)
# Game loop.
while True:
    if menuBool:
        quitbutton = screen.blit(menu.quitbutton.image, (800, 50))
        startbutton = screen.blit(menu.playbutton.image, (800,200))
        button = []
        button.append(quitbutton)
        button.append(startbutton)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if button[0].collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif button[1].collidepoint(pygame.mouse.get_pos()):
                    menuBool = False


        # Update.

        # Draw.
        fond = menu.fond.convert()
        screen.blit(fond, (0, 0))
        screen.blit(menu.quitbutton.image, (800, 50))
        screen.blit(menu.playbutton.image, (800, 200))
        pygame.display.flip()
    else :
        screen.fill((4, 129, 220))
        if not game.started:
            confirmButton = screen.blit(confirmButtunImage,(560,5))
        ggame.drawGrid()
        ggame.updateBoatsSprite()
        if not noWin:
            playButton = screen.blit(pygame.image.load("images/playButton.png"),(500,200))
            font = pygame.font.Font('freesansbold.ttf', 32)
            theText = 'player ' + str(p) + ' win'
            text = font.render(theText, True, (220,5,25))
            textRect = text.get_rect()  
            textRect.center = ( 1280// 2, 720 // 2 + 50 ) 
            screen.blit(pygame.image.load("images/tmarker.png"),(518,360))
            
        pygame.display.flip()
        ggame.getMousePos(pygame.mouse.get_pos())
        ggame.coordScreenToGrid()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # all click event
            # right click event
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                ggame.changeOrientaion()
            # left click event
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if confirmButton.collidepoint(pygame.mouse.get_pos()):
                    if ggame.checkPlacedBoat(p) and not Partie.Partie.started:
                        for boat in ggame.team:
                            if not boat.orientation:
                                boat.rotate()
                            boat.reinitializecoord()
                        p += 1

                    if p == 3:
                        p = 1
                        Partie.Partie.started = True
                    
                if not noWin:
                    if playButton.collidepoint(pygame.mouse.get_pos()):
                        game = Partie.Partie(10)
                        p = 1
                        noWin = True
                        boatPlaced = False
                        ggame = gameGraphic.gameGraphic(team,screen)

                elif Partie.Partie.started:
                    if ggame.inGrid:
                        if(ggame.playerGrid != p):
                            if not game.getPlayer(1 if p == 2 else 2).desk[ggame.gx][ggame.gy].shoted:
                                p = 1 if p == 2 else 2
                                noWin = game.round(p, ggame.gx, ggame.gy)
                                if game.getPlayer(p).desk[ggame.gx][ggame.gy].isBoat:
                                    ggame.actualGrid.gridBoat( ggame.gx, ggame.gy)
                                else:
                                    ggame.actualGrid.gridNothing( ggame.gx, ggame.gy)


                else :  
                    if boatGraphic.Boatgraphic.isselected :
                        temp = ggame.numberselected + (2 if ggame.numberselected < 2 else 1)
                        if ggame.inGrid:
                            boatPlaced = game.getPlayer(p).checkOutGrid(temp, ggame.gx,ggame.gy,ggame.selected.orientation)
                            boatPlaced = ggame.placeBoat(p,boatPlaced)
                            if boatPlaced :
                                game.placeBoat(temp ,ggame.selected.gx, ggame.selected.gy,ggame.selected.orientation,p)
                        else:
                            ggame.placeBoat(p,True)
                            boatPlaced = False
                        
                    if not boatPlaced:
                        
                        if ggame.inGrid :
                            if not boatGraphic.Boatgraphic.isselected:
                                test  = ggame.checkBoatClick()
                                if test:
                                    size =  (2 if ggame.numberselected < 2 else 1)
                                    game.removeBoat(size + ggame.numberselected ,ggame.selected.gx, ggame.selected.gy,ggame.selected.orientation,p)
                        else:
                            ggame.checkBoatClick()
                    else:
                        boatPlaced = False

                game.player2.showBoard()
        if pygameclass.boatgraphic.Boatgraphic.isselected:
            ggame.mooveBoat()

        
        ggame.gridOver()

    # Update.

    # Draw.

    fpsClock.tick(fps)
