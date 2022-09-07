import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
backImage = pygame.image.load("Images/bg.png")
pygame.display.set_caption("Galaxy game")
fonts = pygame.font.SysFont('Times new roman', 40)

isDone = False
isBul = False

bulletImage = pygame.image.load("Images/bullet.png")
enemyImage = pygame.image.load("Images/g-enemy.png")
playerImage = pygame.image.load("Images/g-player.png")

score = 0

bul_x = 220
bul_y = 460
bul_dx = 0
bul_dx = 0

player_x = 200
player_y = 500
last_x = 0

enemy_x = random.randint(100, 700)
enemy_y = random.randint(20, 50)
enemy_dx = 5
enemy_dy = 60

def show_player(x, y):
    screen.blit(playerImage, (x, y))

def show_enemy(x, y):
    screen.blit(enemyImage, (x, y))

def show_bullet(x, y):
    screen.blit(bulletImage, (x, y))

def isCollision(enemy_x, enemy_y, bul_x, bul_y):
    if bul_x in range(enemy_x, enemy_x + 70) and bul_y in range(enemy_y, enemy_y + 70):
        return True
    return False

def show_score(x, y):
    sc = fonts.render("Score: " + str(score), True, (255, 255, 0))
    screen.blit(sc, (x, y))
    
while not isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player_x -= 5
        bul_x -= 5
    if pressed[pygame.K_RIGHT]:
        player_x += 5
        bul_x += 5

    if (player_x < 0 or player_x > 735) and (bul_x < 0 or bul_x > 735):
        player_x = player_x % 735
        bul_x = bul_x % 735

    enemy_x += enemy_dx
    
    if enemy_x < 0 or enemy_x > 735:
        enemy_dx = -enemy_dx
        enemy_y += enemy_y
    screen.blit(backImage, (0, 0))

    if bul_x == player_x + 20 and bul_y == 460:
        last_x = player_x 

    if pressed[pygame.K_SPACE]:
        isBul = True
    if isBul:
        bul_y -= 5
        bul_x = last_x + 20

    if bul_y == 0:
        isBul = False
        bul_x = player_x + 20
        bul_y = 460    
    
    isCol = isCollision(enemy_x, enemy_y, bul_x, bul_y)
    if isCol and bul_y < 460:
        enemy_x = random.randint(100, 700)
        enemy_y = random.randint(20, 50)
        bul_x = player_x + 20
        bul_y = 460
        score += 1
        isBul = False

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_bullet(bul_x, bul_y)
    show_score(600, 60)
    pygame.display.update()