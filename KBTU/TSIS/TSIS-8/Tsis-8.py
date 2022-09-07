import pygame, time, random 

pygame.init()

#Setting up FPS 
FPS = 30

flock = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (400,600)
SPEED = 5
SPEED2 = random.randint(5,10)       # 为Enemy 和 Coins 设计的random速度
SCORE = 0
cnt = 0     # 计数我们收集的星星


#Create a white screen 
DISPLAYSURF = pygame.display.set_mode(SIZE)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game")
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("Images/AnimatedStreet.png")
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Images/Player.png")
        self.surf = pygame.Surface((40, 75))    # 它的我们看不见的 Surface
        self.rect = self.surf.get_rect(center = (160, 520)) # 在这个位置居中创建rect

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top >0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
                
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,5)
         
        if self.rect.left > 0:       # 上限: 让它在不超过左边界的情况下才能往左移动
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:      # 上限: 让它在不超过右边界的情况下才能往右移动   
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Images/Enemy.png")
        self.surf = pygame.Surface((42, 70))    # 它的Surface 大小. 我们看不见
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))    # Enemy 需要在道路上随机出现
 
      def move(self):
        global SCORE    # 设分数为全局
        self.rect.move_ip(0,SPEED2)  # Enemy 在 y-轴向我们走动
        if (self.rect.top > 600):   # 每当一个 Enemy 过后, Score +1
            SCORE += 1
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 40))   # 将照片转换成这个 Size
        self.surf = pygame.Surface((42,72)) # 它的 Surface 大小
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH - 40), 0)) # Coins 需要在道路随机出现
 
    def move(self):
        global cnt 
        self.rect.move_ip(0,SPEED2)
        if (self.rect.top > 600):
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -10)


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coins()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event        用户事件. 目的是每过一秒,让速度提高0.5
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)   # 每1000毫秒（即1秒）调用INC_SPEED事件对象
 
run = True
i = 0
#Game Loop
pygame.mixer.music.load('videoplayback.wav')
pygame.mixer.music.play(-1)
while run:

    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == pygame.QUIT:
            run = False
 
    DISPLAYSURF.blit(background, (0,0))     # 将马路渲染
    scores = font_small.render("Passed: "+str(SCORE), True, BLACK)
    points = font_small.render("Points: " + str(cnt), True, BLACK)

    DISPLAYSURF.blit(scores, (10,10))       # 将分数渲染在左上角
    DISPLAYSURF.blit(points, (10,30))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) # 在窗口绘制所有的精灵(Enemy, Player, Coin)
        entity.move()       # 让他们走动

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies): # 检测与另一个Group的任何 Enemy 是否有碰撞:
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        run = False
        
    if pygame.sprite.spritecollideany(P1, coins): # 检测与另一个Group的任何 Coins 是否有碰撞:
        cnt += 1
        # 在车吃了Coin后, 让下次的Coin 晚点出现, 所以把他的下次y位置设为了 -150: 
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -150)

         
    pygame.display.update()
    flock.tick(FPS)
pygame.quit()
sys.exit()