import pygame, sys, math

PI = math.pi
''' 
        pygame.draw.line(Surface, color, start_pos, end_pos, width = 1)
    


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
    pygame.draw.line(screen, (255,0,0), (100,100),(500,100),1)
    pygame.draw.line(screen, (255,0,0), (500,100),(500,300),1)
    pygame.draw.line(screen, (255,0,0), (500,300),(100,300),1)
    pygame.draw.line(screen, (255,0,0), (100,300),(100,100),1)

    pygame.display.update()

pygame.quit()
