#########    6. uploads photos
import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((800,800))
running = True

image = pygame.image.load('Images/ball.png')
image2 = pygame.image.load('Images/Enemy.png')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    screen.blit(image,(20,20))
    screen.blit(image2,(50,50))

    pygame.display.flip()
