import pygame, sys

pygame.init()   # initilization  

SIZE = WIDTH, HEIGHT =  (600,480)

screen = pygame.display.set_mode(SIZE) # Экран  px 
pygame.display.set_caption("First my pygame")

icon = pygame.image.load('D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-18(Pygame Part-3)\icon.jpg')
pygame.display.set_icon(icon)

# RGB : (0,0,0)
BLACK = (0,0,0)

WHITE = (255,255,255)

x = 100
y = 100

running = True    # Жүріп жатыр
while running:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 10
        
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255,0,0), (x,y), 25)

    pygame.display.update()
    

