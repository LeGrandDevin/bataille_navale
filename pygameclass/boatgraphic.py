import pygame

class Boatgraphic:
    isselected = False

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.initialx = x
        self.initialy = y

    def addSquare(self, square):
        self.square = square

    def coord(self):
        return [self.x, self.y]

    def newcoord(self, coord, orientaion):
        self.x = coord[0] - (self.square[2]/2 if orientaion else 0)
        self.y = coord[1] - (self.square[3]/2 if not orientaion else 0)

    def reinitializecoord(self):
        self.x = self.initialx
        self.y = self.initialy


