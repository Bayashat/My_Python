import pygame, sys

''' 
        pygame.draw.rect(Surface, color, Rect, width = 0)
    Rect(x,y,width,height)   
    width = 0  қалыңдығы




'''
pygame.init()

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")

running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

    pygame.draw.rect(screen, (0,255,0), (150,150,200,50), 20)
    pygame.display.update()

pygame.quit()
