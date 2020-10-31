class Boatgraphic:
    isselected = False

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.initialx = x
        self.initialy = y

    def coord(self):
        return [self.x, self.y]

    def newcoord(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def reinitializecoord(self):
        self.x = self.initialx
        self.y = self.initialy


