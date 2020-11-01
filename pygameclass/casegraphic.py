import pygame


class Casegraphic:

    def __init__(self, x, y, size, display):
        self.x = x
        self.y = y
        self.size = size
        self.display = display
        self.color = (3, 84, 143)
        self.basecolor = self.color

    def drawcase(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.size, self.size))

    def caseover(self):
        r = self.basecolor[0]
        g = self.basecolor[1]
        b = self.basecolor[2]
        self.color = (r+30, g+30, b+30)

    def caseout(self):
        self.color = self.basecolor

    def caseclickedWithoutBoat(self):
        self.basecolor = (178, 34, 34)

    def caseclickedWithBoat(self):
        self.basecolor = (34, 139, 34)

