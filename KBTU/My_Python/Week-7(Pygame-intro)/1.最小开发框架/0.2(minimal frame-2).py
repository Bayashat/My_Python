###############   0.2 Minial Frame version-2
import pygame

#Initializing pygame module
pygame.init()

Size = SCREEN_WIDHT, SCREEN_HEIGHT = 500, 500

# Will be retered Surface object (Creating window)
screen = pygame.display.set_mode((Size))
pygame.display.set_caption('My First Game')

running = True

# Main program loop
while running:
  # Even loop
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False
  
  # Game Logic

  # Drawing objects

  # Apply changes on the window (change the frame)
  pygame.display.flip()

# Exiting from pygame program
pygame.quit()