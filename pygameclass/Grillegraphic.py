import pygameclass.casegraphic as casegraphic
import math


class grillegraphic:
    def __init__(self, display, xStart, yStart):
        self.lastcoord = (0, 0)
        self.grid = []
        self.xStart = xStart
        self.yStart = yStart
        self.size = 50
        for g in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[g].append(casegraphic.Casegraphic(xStart+(self.size)*g, yStart+(self.size)*j, self.size-1, display))

    def drawgrid(self):
        for g in self.grid:
            for j in g:
                j.drawcase()

    def gridover(self, x, y):
        self.grid[x][y].caseover()
        if self.lastcoord != (x, y):
            self.gridout(self.lastcoord[0], self.lastcoord[1])
            self.lastcoord = (x, y)

    def gridout(self, x, y):
        self.grid[x][y].caseout()

    def coordScreenToGrid(self, x, y):
        gx = math.trunc((x - self.xStart) / self.size)
        gy = math.trunc((y - self.yStart) / self.size)
        return gx, gy
    
    def inGrid(self, x ,y ):
        if self.xStart < x < self.xStart + self.size*10 and self.yStart < y < self.yStart + self.size*10 :
            return True 

