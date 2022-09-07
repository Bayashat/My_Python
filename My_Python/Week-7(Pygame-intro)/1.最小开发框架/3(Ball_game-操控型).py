#################    3.壁球小游戏(操控型)与键盘的基本使用

'''
壁球小游戏(操控型)关键要素:

键盘使用: 如何获取键盘的操作事件
速度调节: 根据对应按键调节壁球运动速度.

'''
import pygame,sys

pygame.init()

size = WIDTH, HEIGHT = 600, 480
dx, dy = 1,1
BLACK = (0,0,0)

fps = 300
fclock = pygame.time.Clock()    # 创建一个 Clock 对象, 用于操作时间

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame 壁球之旅")

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")
ballrect = ball.get_rect() 

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:  # Pygame 对键盘敲击的事件定义, 键盘每个键对应一个具体定义.

      if event.key == pygame.K_LEFT:
        if dx == 0:
          dx = dx
        else:
          (abs(dx) - 1) * int(dx / abs(dx))

      elif event.key == pygame.K_RIGHT:
        dx = dx + 1 if dx > 0 else dx - 1

      elif event.key == pygame.K_UP:
        dy = dy + 1 if dy > 0 else dy - 1

      elif event.key == pygame.K_DOWN:
       dy = dy if dy ==0 else (abs(dy) - 1) * int(dy / abs(dy))

  ballrect = ballrect.move(dx,dy)

  if ballrect.left < 0 or ballrect.right > WIDTH:
    dx = -dx
  if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    dy = -dy

  screen.fill(BLACK)
  screen.blit(ball, ballrect)

  fclock.tick(fps)    # 控制帧速度, 即窗口刷新速度,.
  pygame.display.update()