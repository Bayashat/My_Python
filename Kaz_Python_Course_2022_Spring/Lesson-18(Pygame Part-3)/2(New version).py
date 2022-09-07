from tkinter.tix import Balloon
import pygame, random

pygame.init()

size = WIDTH, HEIGHT = 600,600
screen = pygame.display.set_mode((size))

clock = pygame.time.Clock()

class Ball:
    Ball_size = 25

    def __init__(self, *args, **kwargs):
        self.radius = 20

        self.x = random.randint(self.Ball_size, WIDTH - self.Ball_size)
        self.y = random.randint(self.Ball_size, HEIGHT - self.Ball_size)

        self.dx = random.randint(-2, 3)  # -2 -1 0 1 2
        self.dy = random.randint(-2,3)

        if self.dx == 0: self.dx = random.randint(-2, 3) 
        if self.dy == 0: self.dy = random.randint(-2, 3)

        self.color =(random.randint(0,256),random.randint(0,256), random.randint(0,256) )
    

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > 600 or self.x < 0:
            self.dx *= -1
        if self.y > 600 or self.y < 0:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

dop = Ball()
while True:
    for event in pygame.event.get():  # Әрекет
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()

        
    screen.fill((0,0,0))

    dop.draw()
    dop.move()
    
    clock.tick(60)
    pygame.display.update()