import pygame, sys

''' 
        pygame.draw.circle(Surface, color, center_pos, radius, width)

    center_pos : (x,y)
    radius : 25.0
    

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

    pygame.draw.circle(screen, (0,0,255), (250,250),100)
    pygame.display.update()

pygame.quit()
