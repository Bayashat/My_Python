import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

radius = 10
body = [[100, 100], [0, 0], [0, 0]] # 初始长度
# 1) [100, 100], [0, 0], [0, 0]
# 2) [115，100], [100, 100], [0，0] # 开始了
# 3）[130.100], [115,100], [100,100]
# 4) [130,115], [130,100], [115,100]    # 向下移动的时候
block = 15
dx, dy = 15, 0  # 初始每移动的距离



# 223
# round(223 / 10) = round(22.3) = 220
def own_round(value, base=10):  # 由于我们的蛇体是radius=10, 所以food需要在10的倍数的位置出现
  return base * round(value / 10)

def set_random_position():
  return own_round(random.randint(10, WINDOW_WIDTH-10)), own_round(random.randint(10, WINDOW_HEIGHT-10))

food_x, food_y = set_random_position()

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx = block
        dy = 0
      if event.key == pygame.K_LEFT:
        dx = -block
        dy = 0
      if event.key == pygame.K_UP:
        dx = 0
        dy = -block
      if event.key == pygame.K_DOWN:
        dx = 0
        dy = block
      if event.key == pygame.K_SPACE:
        body.append([0, 0])
        food_x, food_y = set_random_position()

  for i in range(len(body) - 1, 0, -1): # 从后面开始, 每移动时后面的位置成为前一位的.
    body[i][0] = body[i - 1][0]
    body[i][1] = body[i - 1][1]
  
  body[0][0] += dx  # 而头直接按d 变
  body[0][1] += dy

  # Check for Food eating, if so, add one item to Snake body
  screen.fill(BLACK)

  # Draw food
  pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)

  # Draw snake
  for i, (x, y) in enumerate(body):
    color = RED if i == 0 else GREEN    # 给蛇头画红色,身体绿色
    pygame.draw.circle(screen, color, (x, y), radius)

  pygame.display.flip()

  clock.tick(30)

pygame.quit()