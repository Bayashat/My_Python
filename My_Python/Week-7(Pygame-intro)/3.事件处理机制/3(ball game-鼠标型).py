#############  3.壁球游戏-鼠标型
'''需求:

 通过鼠标左键摆放壁球,按键按下时壁球停止移动.
鼠标按下且移动时,壁球跟随鼠标移动.
当释放按键时,壁球继续移动.

实现的关键因素:
对于鼠标键按下和释放的合理处置
'''
import pygame,sys

pygame.init()

size = WIDTH, HEIGHT = 600,400
dx, dy = 1, 1

BLACK = (0,0,0)

fps = 200
fclock = pygame.time.Clock()
still = False   # 设置1个变量,控制小球是静止还是移动.

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame 壁球")

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
                
        elif event.type == pygame.VIDEORESIZE:
            size = WIDTH, HEIGHT = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        # 增加对鼠标左键按下的响应
        elif event.type == pygame.MOUSEBUTTONDOWN:   # 鼠标键按下事件
            if event.button == 1:   # 当鼠标左键按下时,我们对控制小球移动的变量设为True.来让小球停止移动
                still = True
        # 接下来增加对鼠标释放的响应支持:
        elif event.type == pygame.MOUSEBUTTONUP:    # 鼠标键释放事件
            still = False
            if event.button  == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1] - ballrect.top)

        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1]-ballrect.top)


    if pygame.display.get_active() and not still:    
        ballrect = ballrect.move(dx,dy)

    if ballrect.left < 0 or ballrect.right > WIDTH:
        dx = -dx
        if ballrect.right > WIDTH and ballrect.right + dx > ballrect.right:
            dx = -dx
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        dy = -dy
        if ballrect.bottom > HEIGHT and ballrect.bottom + dy > ballrect.bottom:
            dy = -dy

    screen.fill(BLACK)
    screen.blit(ball, ballrect) 

    fclock.tick(fps)   
    pygame.display.update()