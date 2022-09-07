#import pygame
import pygame
import math

#initialize game engine
pygame.init()

#Open a window
size = (400, 250)
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

clock = pygame.time.Clock()
PI=math.pi

while(dead==False):
 for event in pygame.event.get(): 
  if event.type == pygame.QUIT:
   dead = True
  
  screen.fill(WHITE)
  pygame.draw.rect(screen, BLACK, [80,10,250,200], 2)
  pygame.draw.arc(screen, RED, [80,10,250,200], PI/2, PI, 2)
  pygame.draw.arc(screen, GREEN, [80,10,250,200], 0, PI/2, 2)
  pygame.draw.arc(screen, BLUE, [80,10,250,200], 3*PI/2, 2*PI, 2)
  pygame.draw.arc(screen, BLACK, [80,10,250,200], PI, 3*PI/2, 2)
  
  pygame.display.flip()
  clock.tick(60)
   
#Shutdown display module
pygame.display.quit()