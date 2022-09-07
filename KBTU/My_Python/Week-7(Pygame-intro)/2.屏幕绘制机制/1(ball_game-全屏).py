#############  1. Ball_game : 全屏型
import pygame,sys

pygame.init()

vInfo = pygame.display.Info()   # 感知当前操作系统的屏幕尺寸
size = WIDTH, HEIGHT = vInfo.current_w , vInfo.current_h  # 将我们游戏的窗口尺寸设为与我们屏幕一样大
dx,dy = 5,5


BLACK = (0,0,0)

fps = 300
fclock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
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

      elif event.key == pygame.K_ESCAPE:  # ESC 键退出
        sys.exit()

  ballrect = ballrect.move(dx,dy)  

  if ballrect.left < 0 or ballrect.right > WIDTH:
    dx = -dx
  if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    dy = -dy

  screen.fill(BLACK)
  screen.blit(ball, ballrect) 

  fclock.tick(fps)   
  pygame.display.update()