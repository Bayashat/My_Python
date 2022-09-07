import pygame, sys, math

PI = math.pi
''' 
        pygame.draw.lines(Surface, color, closed, pointList, width = 1)
    
    closed : True : басталған нүкте мен аяқталған нүктенің арасын қосады

    pintList: Нүктелердің тізімі


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
    pygame.draw.lines(screen, (255,0,0), True, [(100,100), (200,300), (500,400)], 2)

    pygame.display.update()

pygame.quit()
