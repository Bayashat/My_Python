import pygame, sys

pygame.init()

ball = pygame.image.load("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-17(Pygame Part-2)\images.jfif")

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")
pygame.display.set_icon(ball)

running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

    pygame.display.update()

pygame.quit()

