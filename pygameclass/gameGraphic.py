import pygame
from . import Grillegraphic
from . import boatgraphic

class gameGraphic:

    def __init__(self,team,screen):
        self.team = team
        self.numberSelected = -1
        self.screen = screen
        self.grid1 = Grillegraphic.Grillegraphic(screen, 50, 50)
        self.grid2 = Grillegraphic.Grillegraphic(screen, 700, 50)
        self.inGrid = False
        self.actualGrid = self.grid1
        self.g = True
        self.numberselected = 1


    def updateBoatsSprite(self):
        for boat in self.team:
            boat.addSquare(self.screen.blit(boat.sprite, boat.coord()))

    def getMousePos(self,coord):
        self.mx = coord[0]
        self.my = coord[1]

    def wichGrid(self):
        self.inGrid = True
        if self.grid1.inGrid(self.mx,self.my):
            self.actualGrid = self.grid1 
            self.playerGrid = 1
        elif self.grid2.inGrid(self.mx,self.my):
            self.actualGrid = self.grid2
            self.playerGrid = 2
        else:
            self.inGrid = False
    
    def coordScreenToGrid(self):
        self.wichGrid()
        self.gx , self.gy = self.actualGrid.coordScreenToGrid(self.mx,self.my)

    def changeOrientaion(self):
        if boatgraphic.Boatgraphic.isselected:
            self.selected.rotate()

    def placeBoat(self, p, toPlace):
        if toPlace:    
            if self.inGrid and self.playerGrid == p:
                self.selected.placeBoat(self.gx, self.gy, self.playerGrid == 1 )
                boatgraphic.Boatgraphic.isselected = False
                self.selected.addSquare(self.screen.blit(self.selected.sprite, self.selected.coord()))
                self.numberselected = -1
                return True
            else:
                self.selected.reinitializecoord()
                boatgraphic.Boatgraphic.isselected = False
                self.numberselected = -1
                if not self.selected.orientation:
                    self.selected.rotate()
                self.selected.addSquare(self.screen.blit(self.selected.sprite, self.selected.coord()))
        return False

    def checkBoatClick(self):
        for j in range(5):
            if self.team[j].square.collidepoint(pygame.mouse.get_pos()) and self.numberselected != j:
                self.selected = self.team[j]
                self.numberselected = j
                boatgraphic.Boatgraphic.isselected = True
                self.selected.placed = False
                return True
        return False

    def mooveBoat(self):
        self.selected.newcoord(pygame.mouse.get_pos())

    def gridOver(self):
        if self.inGrid:
            self.actualGrid.gridover(self.gx, self.gy)
        
        else:
            self.actualGrid.gridout(self.actualGrid.lastcoord[0], self.actualGrid.lastcoord[1])

    def drawGrid(self):
        self.grid1.drawgrid()
        self.grid2.drawgrid()

    def checkPlacedBoat(self,player):
        for boat in self.team:
            if boat.placed:
                continue
            return False
        return True