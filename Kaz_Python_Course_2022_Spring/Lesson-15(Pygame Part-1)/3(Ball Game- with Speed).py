import pygame, sys,pygame.time

pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (600,480)

screen = pygame.display.set_mode(SIZE) # Экран  px 
pygame.display.set_caption("First my pygame")

# RGB : (0,0,0)
BLACK = (0,0,0)

WHITE = (255,255,255)
ball = pygame.image.load("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-15(Pygame)/ball.png")

fps = 300  # framerate  : экранды 1 секундта неше рет жаңарту
dx = 1
dy = 0
ballrect = ball.get_rect()  # (1,1)

fclock = pygame.time.Clock()  # Clock обектісі чтобы уақытын настройт ету үшін

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

    ballrect = ballrect.move(dx, dy)  # (0,1)

    if ballrect.right > WIDTH or ballrect.left < 0:
        dx = -dx

    if ballrect.bottom > HEIGHT or ballrect.top < 0:
        dy = -dy

    screen.fill(WHITE)
    
    screen.blit(ball, ballrect)   # доп всегда ballrect пен бірге жүру қолданамыз

    fclock.tick(fps)

    pygame.display.update()

    

