#############  2   Ball_game: 伸缩版
import pygame,sys

pygame.init()

size = WIDTH, HEIGHT = 600,400
dx, dy = 5, 5


BLACK = (0,0,0)

fps = 300
fclock = pygame.time.Clock()

screen = pygame.display.set_mode(size, pygame.RESIZABLE)    # 将屏幕设为窗口大小可调
pygame.display.set_caption("Pygame 壁球之旅")

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")
ballrect = ball.get_rect() 

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        dx = dx if dx ==0 else (abs(dx) - 1) * int(dx / abs(dx))

      elif event.key == pygame.K_RIGHT:
        dx = dx + 1 if dx > 0 else dx - 1

      elif event.key == pygame.K_UP:
        dy = dy + 1 if dy > 0 else dy - 1

      elif event.key == pygame.K_DOWN:
       dy = dy if dy ==0 else (abs(dy) - 1) * int(dy / abs(dy))

      elif event.key == pygame.K_ESCAPE: 
        sys.exit()


    elif event.type == pygame.VIDEORESIZE:  # 感知窗口大小更改的事件
      size = WIDTH, HEIGHT = event.size[0], event.size[1]   # 将新窗口的尺寸赋给当前窗口
      screen = pygame.display.set_mode(size, pygame.RESIZABLE)  

  ballrect = ballrect.move(dx,dy)

  if ballrect.left < 0 or ballrect.right > WIDTH:
    dx = -dx
  if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    dy = -dy

  screen.fill(BLACK)
  screen.blit(ball, ballrect) 

  fclock.tick(fps)  
  pygame.display.update()