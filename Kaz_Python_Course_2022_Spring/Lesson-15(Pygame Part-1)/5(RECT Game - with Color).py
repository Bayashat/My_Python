from turtle import color
import pygame, sys,pygame.time


pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (600,480)

screen = pygame.display.set_mode(SIZE) # Экран  px 
pygame.display.set_caption("First my pygame")

# RGB : (0,0,0)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



WHITE = (255,255,255)

dx = 1
dy = 0

tusy = RED

color = RED

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
    
        elif event.type == pygame.KEYDOWN:  # Клавитура
            if event.key == pygame.K_SPACE:
                if tusy == RED: tusy = BLUE
                elif tusy == BLUE: tusy = RED

    screen.fill(WHITE)

    pygame.draw.rect(screen, tusy, (100,100,200,200))

    pygame.display.update()