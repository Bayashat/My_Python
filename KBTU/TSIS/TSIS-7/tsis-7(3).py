##########   自带动画
import pygame, os ,math

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SIZE  =WIDTH, HEIGHT = (630, 460)
screen = pygame.display.set_mode(SIZE)

x = 0
y = x
run = True
fps = 60
i = 1
clock = pygame.time.Clock()
font = pygame.font.SysFont('serif', 20, False, True)
font2 = pygame.font.SysFont('serif', 18, False, True)
font3 = pygame.font.SysFont('serif', 25, True, False)

l1 = (1.00, 0.75, 0.50, 0.25, 0, -0.25, -0.50, -0.75, -1.00)
l2 = ("-3П", "-2.5П", "-2П", "-1.5П", "-0.5П", "0", "0.5П", "П", "1.5П", "2П", "2.5П", "3П")
text1 = font2.render("-3П  -2.5П  -2П -1.5П  -П  -0.5П   0   0.5П    П   1.5П   2П   2.5П  3П", True, BLACK)
text2 = font3.render("X", True, BLACK)

surf = pygame.Surface((500,310))
surf.fill(WHITE)

win_ceny = surf.get_height() // 2
xpos, ypos = 0, 0
step = -3*math.pi

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run  =False
            if event.key == pygame.K_DOWN:
                WHITE = BLUE
                BLACK = RED
    screen.fill(WHITE)
    
    for i in l1:
        text = font.render(str(i), True, BLACK)
        screen.blit(text, (x, -i*154+170))
    # x-axis:
    screen.blit(text1, (50,375))
    # x
    screen.blit(text2, (310, 400))
    
    # NET:
    screen.blit(surf, (70,30))
    pygame.draw.rect(screen, BLACK, (45,10,550,350), 3)     # 外部框架
    pygame.draw.rect(screen, BLACK, (45,10,275,350), 3)     # x分割线
    pygame.draw.rect(screen, BLACK, (45,10,550,175), 3)     # y 分割线

    # SIN , COS:
    ypos = -1*math.sin(step) * 100
    pygame.draw.circle(surf, RED, (int(xpos), int(ypos) + win_ceny), 10)
    xpos += 0.5
    step += 0.008
    step %= 2*math.pi

    for i in range(9):
        pygame.draw.line(screen, BLACK, (45, i*38.5 + 30), (595, i*38.5+30), 1)
    
    for i in range(8):
        # big:
        pygame.draw.line(screen, BLACK, (45, i*38.5 + 50), (60, i*38.5+50), 1)

        pygame.draw.line(screen, BLACK, (580, i*38.5 + 50), (595, i*38.5+50), 1)

        # Small:
        pygame.draw.line(screen, BLACK, (45, i*38.5 + 40), (50, i*38.5+40), 1)
        pygame.draw.line(screen, BLACK, (45, i*38.5 + 60), (50, i*38.5+60), 1)

        pygame.draw.line(screen, BLACK, (590, i*38.5 + 40), (595, i*38.5+40), 1)
        pygame.draw.line(screen, BLACK, (590, i*38.5 + 60), (595, i*38.5+60), 1)

    for i in range(7):
        # big:
        pygame.draw.line(screen, BLACK, (i*83+70,10), (i*83+70,360), 1)

    for i in range(6):
        # big:
        pygame.draw.line(screen, BLACK, (i*83+110,345), (i*83+110,360), 1)

        pygame.draw.line(screen, BLACK, (i*83+110,10), (i*83+110, 25), 1)

        # Medium:
        pygame.draw.line(screen, BLACK, (i*83+90,350), (i*83+90,360), 1)
        pygame.draw.line(screen, BLACK, (i*83+130,350), (i*83+130,360), 1)

        pygame.draw.line(screen, BLACK, (i*83+90,10), (i*83+90,20), 1)
        pygame.draw.line(screen, BLACK, (i*83+130,10), (i*83+130,20), 1)

        # lil:
        pygame.draw.line(screen, BLACK, (i*83+80,355), (i*83+80,360), 1)
        pygame.draw.line(screen, BLACK, (i*83+100,355), (i*83+100,360), 1)
        pygame.draw.line(screen, BLACK, (i*83+120,355), (i*83+120,360), 1)
        pygame.draw.line(screen, BLACK, (i*83+140,355), (i*83+140,360), 1)

        pygame.draw.line(screen, BLACK, (i*83+80,10), (i*83+80,15), 1)
        pygame.draw.line(screen, BLACK, (i*83+100,10), (i*83+100,15), 1)
        pygame.draw.line(screen, BLACK, (i*83+120,10), (i*83+120,15), 1)
        pygame.draw.line(screen, BLACK, (i*83+140,10), (i*83+140,15), 1)
        
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()