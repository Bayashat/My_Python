import pygame, sys

''' 
        pygame.draw.ellipse(Surface, color, Rect, width = 0)

    Rect(x,y,width, height)


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

    pygame.draw.ellipse(screen, (255,0,0), (200,200,200,100))
    pygame.display.update()

pygame.quit()
