###########   5.Practice-with rect
import pygame

#Initializing pygame module
pygame.init()

SCREEN_WIDHT, SCREEN_HEIGHT = 500, 500

# Will be retered Surface object (Creating window)
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('My First Game')

# Red Green Blue   ---> [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()
# Frames Per Second
FPS = 60

PI = 3.14

running = True

flag = True
color = RED
x, y = 100, 50
dx, dy = 10, 3


# Main program loop
while running:
    # Even loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_SPACE:
                flag = not flag
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
    pos = pygame.mouse.get_pos()
    print(pos)
        
    color = RED if flag else BLUE
    x += dx
    y += dy

    if x + 100 > SCREEN_WIDHT or x < 0:
        dx *= -1
        flag = not flag

    if y + 100 > SCREEN_HEIGHT or y < 0:
        dy *= -1
        flag = not flag

    screen.fill(WHITE)
    pygame.draw.rect(screen, color, (x, y, 100, 100))

    # Apply changes on the window
    pygame.display.flip()

    clock.tick(FPS)


# Exiting from pygame program
pygame.quit()