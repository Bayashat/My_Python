#############   2p1.Draw Rectangular
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Pygame 图形绘制")

Gold = (255,251,0)
Red = pygame.Color("red")

# 开始绘制:
r1rect = pygame.draw.rect(screen, Gold, (100,100,200,100), 5)  # pygame.draw.rect(screen, Gold, pygame.rect(100,100,200,100), 5)
r2rect = pygame.draw.rect(screen, Red, (210,210,200,100), 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
