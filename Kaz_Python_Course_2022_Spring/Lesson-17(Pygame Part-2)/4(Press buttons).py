from tkinter import LEFT
import pygame, sys



pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")

coordinata = x,y = 100,100

running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        x += 50
    elif pressed[pygame.K_LEFT]:
        x -= 50
    elif pressed[pygame.K_DOWN]:
        y += 50
    elif pressed[pygame.K_UP]:
        y -= 50
    


    screen.fill(BLACK)
    pygame.draw.rect(screen, (255,0,0), (x,y,50,50))
    pygame.display.flip()   # update()

    clock.tick(30)

pygame.quit()

