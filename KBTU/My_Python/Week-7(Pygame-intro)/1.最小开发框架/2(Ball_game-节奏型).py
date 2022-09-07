#################    2. 壁球小游戏(节奏型)与屏幕的帧率设置

'''
壁球小游戏(节奏型)关键要素:

需求: 壁球可以按照一定速度运动
关键要素: 如何控制壁球的速度?

'''
import pygame,sys   

pygame.init()

size = WIDTH, HEIGHT = 600,480
dx,dy = 1,1
BLACK = (0,0,0)

fps = 300
fclock = pygame.time.Clock()    # 创建一个 Clock 对象,用于操作时间.

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame 壁球之旅")

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")      
ballrect = ball.get_rect()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      
  ballrect = ballrect.move(dx, dy)  

  if ballrect.left < 0 or ballrect.right > WIDTH:
    dx = - dx
  if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    dy = -dy

  screen.fill(BLACK)
  screen.blit(ball, ballrect)

  fclock.tick(fps)    # 控制帧速度, 即窗口刷新速度.
  pygame.display.update()