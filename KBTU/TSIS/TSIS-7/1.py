##############    Draw just Sinx, Cosx
import pygame
import math
import sys

pygame.init()

Width = 840
Height = 840

Screen = pygame.display.set_mode((Width,Height))

pointes_sin = []
pointes_cos = []
Screen.fill((0,0,0))

n = 6
A = 200
for x in range(Width):
  y = int(math.sin(x / 840. * n * math.pi) * A+420)
  pointes_sin.append([x,y])

for x in range(Width):
  y = int(math.cos(x / 840. * n * math.pi) * A+420)
  pointes_cos.append([x,y])

pygame.draw.lines(Screen, (255,0,0), False, pointes_sin, 3)
pygame.draw.lines(Screen, (0,0,255), False, pointes_cos, 3)
pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      sys.exit()
    