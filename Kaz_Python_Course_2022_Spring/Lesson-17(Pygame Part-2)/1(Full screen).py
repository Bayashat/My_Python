import pygame, sys


pygame.init()  

screen_info = pygame.display.Info()  # ноутбугымыздың экрани үлкендігін анықап береді

size = WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode(size) #
pygame.display.set_caption("First my pygame")

running = True   

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()  

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                sys.exit

    pygame.display.flip()   

pygame.quit()

