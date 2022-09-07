import pygame, sys



pygame.init()   # initilization  pygame modeule


# will create surface object (create window): 
screen = pygame.display.set_mode((600,400)) # Экран  px 
pygame.display.set_caption("First my pygame")

running = True    # Жүріп жатыр

# Main program loop: 
while running:
    # Event :
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

    # Game logic:

    # Drawing objects

    # Apply changes of the window
    pygame.display.flip()   # update()

pygame.quit()

