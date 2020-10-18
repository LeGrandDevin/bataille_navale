import pygame


class Casegraphic:

    def __init__(self, x, y, size, display):
        self.x = x
        self.y = y
        self.size = size
        self.display = display

    def drawcase(self):
        pygame.draw.rect(self.display, (3, 84, 143), (self.x, self.y, self.size, self.size))
