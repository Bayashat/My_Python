import pygame, sys

''' 
        pygame.draw.polygon(Surface, color, pointList, width)
        pointList: нүктелердің тізімі

'''
pygame.init()

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")

l= [(100,100), (300,100), (200,200), (300,300), (100,300)]
running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

    pygame.draw.polygon(screen, (255,0,0), l)
    pygame.display.update()

pygame.quit()
