import pygame
import random

pygame.init()

pygame.font.init()

screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Змейка')

FPS = 90
d = 3       # change

running = True

color_change1 = random.randint(0, 255)
color_change2 = random.randint(0, 255)
color_change3 = random.randint(0, 255)

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = d
        self.dy = 0
        self.grow = False       # 检测它是否处于要增长
        self.dir = 'right'      # Direction
        self.need_to_grow = 5   # 首设置长度为5

    def draw(self):
        
        for element in self.elements[1 : ]:
            color_change1 = random.randint(0, 255)
            color_change2 = random.randint(0, 255)
            color_change3 = random.randint(0, 255)
            pygame.draw.circle(screen, (color_change1, color_change2, color_change3), element, self.radius)     # 绘制除头部以外的部位
        
        pygame.draw.circle(screen, (255, 255, 255), (self.elements[0][0], self.elements[0][1]), self.radius)    # 绘制头部
    

    def move(self):
        global running
        if self.need_to_grow > 0:
            self.need_to_grow -= 1
            self.grow = True

        self.elements.insert(0, [self.elements[0][0] + self.dx, self.elements[0][1] + self.dy])    # 让它一直处于移动状态
        
        if not self.grow:
            self.elements.pop() 
        else:
            self.grow = False
            self.size += 1  # 手动增长
        
        if self.elements[0] in self.elements[1 : ]: # 检测是否咬到自己
            running = False

class Food:
    def __init__(self):
        self.radius = 10
        self.x = 1
        self.y = 1
        self.generate()

    def generate(self): # food 的位置随机
        self.x = random.randint(10, screen_size[0] - 10)
        self.y = random.randint(10, screen_size[1] - 10)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

snake = Snake()
food = Food()
clock = pygame.time.Clock()

while running:
    Ticks = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_LEFT and snake.dir != 'right':
                snake.dx = -d
                snake.dy = 0
                snake.dir = 'left'
            if event.key == pygame.K_RIGHT and snake.dir != 'left':
                snake.dx = d
                snake.dy = 0
                snake.dir = 'right'
            if event.key == pygame.K_UP and snake.dir != 'down':
                snake.dx = 0
                snake.dy = -d
                snake.dir = 'up'
            if event.key == pygame.K_DOWN and snake != 'up':
                snake.dx = 0
                snake.dy = d
                snake.dir = 'down'

            if event.key == pygame.K_1:
                snake.need_to_grow = 5

    # 可越出边界
    if snake.elements[0][0] < 0:
        snake.elements[0][0] = screen_size[0]
    if snake.elements[0][0] > screen_size[0]:
        snake.elements[0][0] = 0
    if snake.elements[0][1] < 0:
        snake.elements[0][1] = screen_size[1]
    if snake.elements[0][1] > screen_size[1]:
        snake.elements[0][1] = 0

    # 若 蛇头与food的间隔<=它们的长度, 则吃了
    if(abs(snake.elements[0][0] - food.x) <= (food.radius + snake.radius) and abs(snake.elements[0][1] - food.y) <= (food.radius + snake.radius)):  
        snake.need_to_grow = 5
        food.generate()

    snake.move()
    screen.fill((0, 0, 0))
    snake.draw()
    food.draw()
    pygame.display.flip()
            