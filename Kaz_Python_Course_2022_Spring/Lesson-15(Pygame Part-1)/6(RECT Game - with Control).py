from turtle import color
import pygame, sys,pygame.time


pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (500,500)

x = WIDTH / 2
y = HEIGHT / 2

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
speed = 15
tusy = RED

clock = pygame.time.Clock()

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
    
        elif event.type == pygame.KEYDOWN:  # Клавитура
            if event.key == pygame.K_SPACE:
                if tusy == RED: tusy = BLUE
                elif tusy == BLUE: tusy = RED

            elif event.key == pygame.K_RIGHT:
                x += speed

            elif event.key == pygame.K_LEFT:
                x -= speed

            elif event.key == pygame.K_UP:
                y -= speed

            elif event.key == pygame.K_DOWN:
                y += speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, tusy, (x,y,100,100))

    pygame.display.update()