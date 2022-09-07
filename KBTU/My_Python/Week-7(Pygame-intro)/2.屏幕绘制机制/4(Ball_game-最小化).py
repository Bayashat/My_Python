#############  4.Ball_game : 感知最小化
import pygame,sys

pygame.init()

size = WIDTH, HEIGHT = 600,400
dx,dy = 1,1


BLACK = (0,0,0)

fps = 300
fclock = pygame.time.Clock()

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
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
            elif event.type == pygame.VIDEORESIZE:
                size = WIDTH, HEIGHT = event.size[0], event.size[1]
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    if pygame.display.get_active():     # 感知窗口.当最小化时,游戏不会运行
        ballrect = ballrect.move(dx,dy)

    if ballrect.left < 0 or ballrect.right > WIDTH:
        dx = -dx
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        dy = -dy

    screen.fill(BLACK)
    screen.blit(ball, ballrect) 

    fclock.tick(fps)   
    pygame.display.update()