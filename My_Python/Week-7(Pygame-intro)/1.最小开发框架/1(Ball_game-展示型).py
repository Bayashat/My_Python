#################    1. 壁球小游戏(展示型)与图像的基本使用

'''
从需求到实现的三个关键元素:

1) 壁球: 游戏需要一个壁球,通过图片引入
2) 壁球运动: 壁球要能够上下左右运动
3) 壁球反弹: 壁球要能够在上下左右边缘反弹
'''
import pygame,sys   

pygame.init()

size = WIDTH, HEIGHT = 600,480
dx,dy = 1,1
BLACK = (0,0,0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame 壁球之旅")

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")      # 将图片载入游戏, 支持 JPG, PNG, GIF(非动画)等13种常用图片格式. 会表示成为 Surface 对象
ballrect = ball.get_rect()  # Surafce 对象的 .get_rect 方法返回一个覆盖图像的矩形 Rect 对象.

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      
  ballrect = ballrect.move(dx, dy)  # move 方法移动一个偏移量(x,y). x,y 是整数.

  # Rect 对象有这些属性: Left, Right, Top, Bottom 表示上下左右. width, hight 表示宽度,高度.
  # 壁球的反弹运动: 遇到 左右上下四侧, 速度取反:
  if ballrect.left < 0 or ballrect.right > WIDTH:
    dx = - dx
  if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    dy = -dy

  screen.fill(BLACK)        # 显示窗口背景填充为这个颜色, 采用RGB色彩体系. 由于壁球不断运动,运动后原有位置填充白色, 因此需要不断刷新背景色.
  screen.blit(ball, ballrect) # 让 ball 跟着 ballrect 移动   # .blit()函数将一个图形绘制在另一个图形上. 通过Rect对象引导对壁球的绘制.

  pygame.display.update()