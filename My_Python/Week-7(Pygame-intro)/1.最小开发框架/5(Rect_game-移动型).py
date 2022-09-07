#########   4.Moves the rect
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


clock = pygame.time.Clock()   # 用于将速度控制在某数字(fps)内，可以明显看到速度有降低.
# Frames Per Second
FPS = 60

PI = 3.14

running = True

flag = True
color = RED
x, y = SCREEN_WIDHT / 2, SCREEN_HEIGHT / 2

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
      elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        x -= 5
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        x += 5
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        y -= 5
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        y += 5

      '''
      若用以下这种方式， 当你在按住 上下左右键它会一直move.
      
  pressed = pygame.key.get_pressed()

  if pressed[pygame.K_UP]: y -= step
  elif pressed[pygame.K_DOWN]: y += step
  elif pressed[pygame.K_LEFT]: x -= step
  elif pressed[pygame.K_RIGHT]: x += step
  '''


  color = RED if flag else BLUE

  screen.fill(WHITE)    # 若不加这个覆盖白色的会让你的rect变"贪吃蛇". 

  pygame.draw.rect(screen, color, (x, y, 100, 100))

  # Apply changes on the window
  pygame.display.flip()

  clock.tick(FPS)


# Exiting from pygame program
pygame.quit()