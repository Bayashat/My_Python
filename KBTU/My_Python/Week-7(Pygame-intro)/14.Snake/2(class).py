import pygame
import random

pygame.init()
SIZE = WIDTH, HEIGHT = (800,600)
screen = pygame.display.set_mode(SIZE)

class Food:
    def __init__(self):
        self.x = round(random.randint(10,WIDTH-10) / 10.0) * 10.0   # 让位置不靠边缘并在10的倍数位置出现
        self.y = round(random.randint(10, HEIGHT-10) / 10.0) * 10.0

    def generate(self):
        self.x = round(random.randint(10,WIDTH-10) / 10.0) * 10.0
        self.y = round(random.randint(10, HEIGHT-10) / 10.0) * 10.0

    def draw(self):
        pygame.draw.circle(screen, (0,255,0), (self.x, self.y), 10)

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 10 # right
        self.dy = 0

        self.is_add = False
        self.speed = 30     # FPS

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):   # # 从后面开始, 每移动时后面的位置成为前一位的.
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx   # 而头直接按d 变
        self.elements[0][1] += self.dy  
        
    def eat(self, foodx, foody):
        # 头部位置
        x = self.elements[0][0] 
        y = self.elements[0][1]
        
        # 第1种方法: 会吃到的准确率高点儿
        if abs(x-foodx) <= 2*self.radius and abs(y-foody) <= 20:
            return True
        # 第2种: 
        # if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
        return False
        
        

snake1 = Snake(100, 100)
food = Food()

running = True

d = 5

clock = pygame.time.Clock()

while running:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d: # 让它在往左走的时候不能往右走
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d

            # if event.key == pygame.K_1:   # 手动增长
            #     snake.is_add = True

    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        food.generate() # 重定义 food 位置

    snake1.move()
    screen.fill((0, 0, 0))
    snake1.draw()
    food.draw()
    pygame.display.flip()

pygame.quit()