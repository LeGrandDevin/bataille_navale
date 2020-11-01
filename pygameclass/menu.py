import pygame
import pygameclass.button as Button

class Menu:
    def __init__(self, quitImage, playImage, fond):
        self.quitbutton = Button.Button(quitImage, 20, 20)
        self.playbutton = Button.Button(playImage, 50, 50)
        self.fond = fond

    def quitButton(self):
        pass

    def playButton(self):
        pass

