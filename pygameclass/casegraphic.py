import pygame


class Casegraphic:

    def __init__(self, x, y, size, display):
        self.x = x
        self.y = y
        self.size = size
        self.display = display
        self.color = (3, 84, 143)

    def drawcase(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.size, self.size))

    def caseover(self):
        self.color = (50, 84, 143)

    def caseout(self):
        self.color = (3, 84, 143)
