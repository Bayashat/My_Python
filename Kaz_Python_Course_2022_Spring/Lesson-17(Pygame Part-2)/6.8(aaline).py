import pygame, sys, math

PI = math.pi
''' 
        pygame.draw.aaline(Surface, color, start_pos, end_pos, blend = 1)
    


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
    pygame.draw.aaline(screen, (255,0,0), (100,100),(500,100))
    pygame.draw.line(screen, (255,0,0), (100,200),(500,100), 10)

    pygame.display.update()

pygame.quit()
