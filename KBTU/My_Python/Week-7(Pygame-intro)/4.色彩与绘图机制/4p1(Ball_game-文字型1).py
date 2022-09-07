##################  4p. Ball_game-文字型
## 使用 .render_t 实现
'''
需求: 把壁球改为一段文字,可以进行移动
关键要素: 文字的移动绘制及刷新
'''
import pygame,sys
import pygame.freetype

pygame.init()

size = WIDTH, HEIGHT = 600, 480
speed = [1,1]
BLACK = (0,0,0)
Gold = 255,251,0
pos = [230,160]

fps = 300
fclock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame 文字绘制")

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=Gold, size=50)

ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    ballrect = ballrect.move(speed[0], speed[1])

    if pos[0] < 0 or pos[0] + f1rect.width > WIDTH:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1rect.height > HEIGHT:
        speed[1] = -speed[1]

    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    screen.fill(BLACK)
    
    f1rect = f1.render_to(screen, (pos[0], pos[1]), "世界和平", fgcolor=Gold, size=50)

    fclock.tick(fps)   
    pygame.display.update()