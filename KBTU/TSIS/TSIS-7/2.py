####### Animation
import pygame
import math
import time
import sys


Width = 640
Height = 480

color = pygame.Color(255,255,0,0)
background_color = pygame.Color(0,0,0,0)

pygame.init()
Screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("SINE WAVE")

Screen.fill(background_color)

surface = pygame.Surface((Width, Height))
surface.fill(background_color)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      sys.exit()
    
  surface.fill(background_color)
  speed = 10
  freq = 3
  A = 40

  for x in range(Width):
    y = int(((Height / 2) + A * math.sin(freq * ((float(x) / Width)) * (2 * math.pi) + (speed * time.time()))))
    surface.set_at((x,y), color)
  for x in range(Width):
    y = int(((Height / 2) + (A+40) * math.cos((freq+5) * ((float(x) / Width)) * (2 * math.pi) + (speed*2 * time.time()))))
    surface.set_at((x,y), color)


  Screen.blit(surface, (0,0))
  pygame.display.flip()

