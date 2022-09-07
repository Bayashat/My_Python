from turtle import color
import pygame, sys,pygame.time


pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (800,600)

x = WIDTH / 2
y = HEIGHT / 2

screen = pygame.display.set_mode(SIZE) # Экран  px 
pygame.display.set_caption("My red ball game")

# RGB : (0,0,0)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

dx = 1
dy = 0
speed = 20

clock = pygame.time.Clock()

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
    
        elif event.type == pygame.KEYDOWN:  # Клавитур
            if event.key == pygame.K_RIGHT:
                x += speed

            elif event.key == pygame.K_LEFT:
                x -= speed

            elif event.key == pygame.K_UP:
                y -= speed

            elif event.key == pygame.K_DOWN:
                y += speed

    if x > 775:
        x = 775
    elif x < 25:
        x = 25
    if y > 575:
        y = 575
    elif y < 25:
        y = 25
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x,y), 25)

    pygame.display.update()