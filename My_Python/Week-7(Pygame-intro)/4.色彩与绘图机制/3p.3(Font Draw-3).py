#import pygame
import pygame
import math

#initialize game engine
pygame.init()

#Open a window
size = (800,800)
screen = pygame.display.set_mode(size)

#Set title to the window
pygame.display.set_caption("Hello World")

dead=False

#Initialize values for color (RGB format)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0, 255, 0)
BLUE=(0,0,255)
BLACK=(0,0,0)

font = pygame.font.SysFont("comicsansms" ,  100)
text = font.render("hello world", True, RED)
while(dead==False):
 for event in pygame.event.get(): 
  if event.type == pygame.QUIT:
   dead = True

  screen.fill(WHITE)
  screen.blit(text, (200,300))
  
#Shutdown display module
  pygame.display.update()