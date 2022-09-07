import pygame, sys, math

PI = math.pi
''' 
        pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle)


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
    pygame.draw.rect(screen, (255,0,0), (100,50,250,200), 1)

    pygame.draw.arc(screen, (0,255,0), (100,50,250,200), PI/2, PI)
    pygame.draw.arc(screen, (255,0,0), (100,50,250,200), PI, 3*PI/2)
    pygame.draw.arc(screen, (0,0,255), (100,50,250,200), 3*PI/2, 0)
    pygame.draw.arc(screen, (0,0,0), (100,50,250,200), 0, PI/2)

    pygame.display.update()

pygame.quit()
