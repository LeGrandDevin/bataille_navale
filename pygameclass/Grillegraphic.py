import pygameclass.casegraphic as casegraphic
import math


class grillegraphic:
    def __init__(self, display):
        self.lastcoord = (0, 0)
        self.grid = []
        for g in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[g].append(casegraphic.Casegraphic(50+60*g, 50+60*j, 59, display))

    def drawgrid(self):
        for g in self.grid:
            for j in g:
                j.drawcase()

    def gridover(self, x, y):
        if x < 10 and y < 10:
            self.grid[x][y].caseover()
            if self.lastcoord != (x, y):
                self.gridout(self.lastcoord[0], self.lastcoord[1])
                self.lastcoord = (x, y)

    def gridout(self, x, y):
        self.grid[x][y].caseout()

    def coordScreenToGrid(self, x, y):
        gx = math.trunc((x - 50) / 60)
        gy = math.trunc((y - 50) / 60)
        return gx, gy