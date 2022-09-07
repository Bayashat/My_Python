##########   3. Create a rect in our surface
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


# Frames Per Second
FPS = 60

PI = 3.14

running = True

flag = True
color = RED

# Main program loop
while running:
  # Even loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:  # 收取键盘上的信息
      if event.key == pygame.K_q:
        running = False
      elif event.key == pygame.K_SPACE:
        flag = not flag


  # if flag:
  #   color = RED
  # else:
  #   color = BLUE
  color = RED if flag else BLUE

  screen.fill(WHITE)

  pygame.draw.rect(screen, color, (50, 50, 100, 100))
  
  # Apply changes on the window
  pygame.display.flip()



# Exiting from pygame program
pygame.quit()