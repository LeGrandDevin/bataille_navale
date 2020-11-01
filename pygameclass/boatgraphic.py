import pygame

class Boatgraphic:
    isselected = False

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.initialx = x
        self.initialy = y
        self.orientation = False
        self.placed = False
        self.gx = 0
        self.gy = 0

    def addSquare(self, square):
        self.square = square

    def coord(self):
        return [self.x, self.y]

    def newcoord(self, coord):
        self.x = coord[0] - (self.square[2]/2 if not self.orientation else 0)
        self.y = coord[1] - (self.square[3]/2 if self.orientation else 0)

    def reinitializecoord(self):
        self.x = self.initialx
        self.y = self.initialy
        self.placed = False

    def placeBoat(self,gridX,gridY,wichGrid):
        add = 50 if wichGrid else 700
        self.x = gridX * 50 + add  - (self.square[2]/2 - 25 if not self.orientation else 0)
        self.y = gridY * 50 + 50 - (self.square[3]/2 - 25 if self.orientation else 0)
        self.placed = True
        self.gx = gridX
        self.gy = gridY
    def rotate(self):
        if self.orientation:
            self.sprite = pygame.transform.rotate(self.sprite,-90)
            self.orientation = False
        else:
            self.sprite = pygame.transform.rotate(self.sprite,90)
            self.orientation = True
        print(self.orientation)