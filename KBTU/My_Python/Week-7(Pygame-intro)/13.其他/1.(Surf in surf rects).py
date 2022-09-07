from random import randint
import pygame

screen = pygame.display.set_mode((400, 400))

background = pygame.Surface((400, 200))     # Create a surface named "background"
background.fill((0, 255, 0)) 
xb = 0
yb = 100

surf = pygame.Surface((100, 100))   # create a surface named "surf"
surf.fill((255, 0, 0))

x = 0
y = 50

background.blit(surf, (x, y))   # 将 surf 映射到 background
screen.blit(background, (xb, yb))   # 再将 background 映射到 screen

pygame.display.update()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            yb = randint(0, 200)

    if x < 400:
        x += 2
    else:
        x = 0

    screen.fill((0, 0, 0))
    background.fill((0, 255, 0))
    background.blit(surf, (x, y))
    screen.blit(background, (xb, yb))
    
    pygame.display.update()

    pygame.time.delay(30)

pygame.quit()