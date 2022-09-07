################      小球们任意走动
import pygame
import random

pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((size))
done = False

clock = pygame.time.Clock()

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Ball:
    BALL_SIZE = 25

    def get_random_change(self):
        change = random.randint(-2, 3)
        while change == 0:
            change = random.randint(-2, 3)
        return change

    def __init__(self, *args, **kwargs):
        self.radius = 20
        self.x = random.randint(self.BALL_SIZE, WIDTH - self.BALL_SIZE)
        self.y = random.randint(self.BALL_SIZE, HEIGHT - self.BALL_SIZE)
        self.dx = self.get_random_change()
        self.dy = self.get_random_change()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  
    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > 600 or self.x < 0:
            self.dx *= -1
        if self.y > 600 or self.y < 0:
            self.dy *= -1


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


ball_list = [
  Ball()
]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_list.append(Ball())

    for ball in ball_list:
        ball.move()

    screen.fill(WHITE)
  
    for ball in ball_list:
        ball.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()