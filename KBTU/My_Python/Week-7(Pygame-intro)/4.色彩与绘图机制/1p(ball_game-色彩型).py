################   1p. 壁球小游戏(色彩型) Wall Ball game

# 需求: 根据壁球移动修改游戏的背景色
'''
RGB 颜色分别定义为如下:
R: 壁球水平距离: int(水平距离/窗体宽度)  取值 0-255

G: 壁球垂直距离: int(垂直距离/窗体高度） 取值 0-255

B: 壁球水平和垂直速度差别: 最小速度/最大啊速度  取值 0-255
'''

import pygame,sys

pygame.init()

size = WIDTH, HEIGHT = 600,400
dx, dy = 1, 1

BLACK = (0,0,0)

fps = 200
fclock = pygame.time.Clock()    
still = False

bgcolor = pygame.Color("black")     # 背景色为黑色

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame 壁球之旅")

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")
ballrect = ball.get_rect()


def RGBChannel(a):      # 此函数用于把输入的参数映射成 0-255 的整数
    return 0 if a<0 else (255 if a>255 else int(a))
    
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
                
        elif event.type == pygame.VIDEORESIZE:
            size = WIDTH, HEIGHT = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:  
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:    
            still = False
            if event.button  == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1] - ballrect.top)

        elif event.type == pygame.MOUSEMOTION:  
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1]-ballrect.top)


    if pygame.display.get_active() and not still:    
        ballrect = ballrect.move(dx,dy)

    if ballrect.left < 0 or ballrect.right > WIDTH:
        dx = -dx
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        dy = -dy

    bgcolor.r = RGBChannel(ballrect.left*255/WIDTH)     # 小球背景的红色通道值
    bgcolor.g = RGBChannel(ballrect.top*255/HEIGHT)     # 小球背景的绿色通道值
    bgcolor.b = RGBChannel(min(x,y)*255/max(x,y,1))     # 小球背景的蓝色通道值, 最大速度不能为0,最小是1.

    screen.fill(bgcolor)    # 背景调成我们的
    screen.blit(ball, ballrect) 

    fclock.tick(fps)   
    pygame.display.update()