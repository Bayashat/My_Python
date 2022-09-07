import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED_COIN = 3
SCORE = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("static/AnimatedStreet.png")
 
#Create a white screen 
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):  # бастапқы қалпын құру
        super().__init__() 
        self.image = pygame.image.load("static/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):  # машинаның қозғалуы
        self.rect.move_ip(0,SPEED)  # Y осі бойынша төмен қарай жылжып отырады
        if (self.rect.top > 600):  # экраннан шыққан кезде жоғарыдан қайта пайда болады
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("static/coins.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0) 

    def move(self):
        self.rect.move_ip(0, SPEED_COIN)
        if (self.rect.top > 600):  # экраннан шыққан кезде жоғарыдан қайта пайда болады
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def hit(self):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    


 
class Player(pygame.sprite.Sprite):
    def __init__(self):   # бастапқы қалпын құру
        super().__init__() 
        self.image = pygame.image.load("static/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # біздіңт машинаның бастапқы орны
        
    def move(self):   # машинаның қозғалуы

        if SCORE != 0 and SCORE % 20 == 0:  # 20 40 60 80 ...
            SPEED += 0.5

        pressed_keys = pygame.key.get_pressed()  # клавитураның басылғанын анықтау
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:  # солға жылжытады
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:  # оңға жылжытады
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coins()
C2 = Coins()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

players = pygame.sprite.Group()
players.add(P1)

coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждый 1 секунд өткенін анықтайды
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # каждый 1 секнд өткен сайын, жылдамдық += 0,5
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    screen.blit(background, (0,0))  # жолдың суретін экранға салу
    scores = font_small.render(str(SCORE), True, BLACK) # ұпайдың жазуы
    screen.blit(scores, (350,10))  # ұпайды экранның сол жақ жоғары жағына қойдық
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:  # цикл арқылы барлық персонажды қозғалтамыз        
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(C1, players):
        SCORE += 2
        C1.hit()
        
    if pygame.sprite.spritecollideany(C2, players):
        SCORE += 4
        C2.hit()
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):  # қандай да бір обьектінің басқа бір класспен соғылуын анықтайды
          pygame.mixer.Sound('static/crash.wav').play()
          time.sleep(0.5)
                    
          screen.fill(RED)
          screen.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)