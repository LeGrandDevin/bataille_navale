import sys
 
import pygame
from pygame.locals import *
 
pygame.init()

 # load
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
 
# Game loop.
while True:
  screen.fill((4, 129, 220))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.


  
  # Draw.
  


  pygame.display.flip()
  fpsClock.tick(fps)