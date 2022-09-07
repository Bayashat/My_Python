import pygame, sys

pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (600,480)

screen = pygame.display.set_mode(SIZE) # Экран  px 
pygame.display.set_caption("First my pygame")

car = pygame.image.load('D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-18(Pygame Part-3)\car1.jpg')

# RGB : (0,0,0)
BLACK = (0,0,0)

WHITE = (255,255,255)

def middle():
    pointList = []  # [300,40][300,60]
    x = 300
    for y in range(0,480,20):
        pointList.append([x,y])
        if len(pointList) == 4:
            pygame.draw.lines(screen, BLACK, False, pointList, 5)
            pointList = []

x = 350
y = 350

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20
            elif event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20                

    screen.fill((255,255,255))

    pygame.draw.line(screen, BLACK, (100, 480), (200,0), 5)
    pygame.draw.line(screen, BLACK, (500, 480), (400,0), 5)

    middle()

    screen.blit(car, (x,y))
        
    pygame.display.update()
    

