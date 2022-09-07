import pygame, sys, math

PI = math.pi
''' 
        pygame.draw.aalines(Surface, color, closed, pointList)
    


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

    screen.fill((255,255,255))
    pygame.draw.aalines(screen, (255,0,0), False, [(100,100),(100,300), (500,300), (100,100)])

    pygame.display.update()

pygame.quit()