import pygame , time, random

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,102)
GREEN = (0,255,0)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

snake_block_size = 10
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("papyrusttc", 50)
score_font = pygame.font.SysFont("ヒラキノ角コシックw0ttc", 35)

class Snake:
    def __init__(self,
                 keys = {'UP': pygame.K_w, 'RIGHT':pygame.K_d,
                         'DOWN': pygame.K_s, 'LEFT': pygame.K_a}):
        self.block_size = 10
        self.speed = 10
        self.color = BLACK
        self.keys = keys
        self.elements = [WIDTH // 2, HEIGHT // 2]
        self.dx = 0
        self.dy = 0
        self.ate_food = False
    
    def move(self, pressed_keys):
        if pressed_keys[self.keys['UP']]:
            self.dx = 0
            self.dy = -1
        elif pressed_keys[self.keys['DOWN']]:
            self.dx = 0
            self.dy = 1
        elif pressed_keys[self.keys['RIGHT']]:
            self.dx = 1
            self.dy = 0
        elif pressed_keys[self.keys['LEFT']]:
            self.dx = -1
            self.dy = 0
        
        old_head = self.elements[0]
        head = [old_head[0] + self.dx * self.speed, old_head[1] + self.dy * self.speed]

        if self.ate_food:
            self.elements = [head] + self.elements
        else:
            self.elements = [head] + self.elements[:-1]
        self.ate_food = False
    
    def draw(self, screen):
        for item in self.elements:
            pygame.draw.rect(screen, self.color, [*item, self.block_size, self.block_size])

    def get_head_coordinates(self):
        return self.elements[0]
    
    def get_length(self):
        return len(self.elements)

    def add_block(self):
        self.ate_food = True
    

def message(font, msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, (x, y))

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = WIDTH // 2

    snake = Snake(snake_block_size, BLACK, [WIDTH // 2, HEIGHT // 2])
    '''
    keys = {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN,
        'RIGHT': pygame.K_RIGHT,
        'LEFT': pygame.K_LEFT
    }
    '''
    foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
    
    while not game_close:
        clock.tick(snake_speed)

        while game_over:
            screen.fill(BLUE)
            message(font_style, "Game over!", RED, WIDTH // 2, HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

        x1, y1 = snake.get_head_coordinates()
    
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over == True
        
        

        snake.move(pygame.key.get_pressed())

        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block_size, snake_block_size]) 
        snake.draw(screen)

        message(score_font, "Your score: " + str(snake.get_length() - 1), YELLOW, 0, 0)
   
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
            snake.add_block()
            
    pygame.quit()
    quit() 
game_loop()