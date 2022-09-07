#############   2p2.Draw Smiley face
import pygame,sys
from math import pi 

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Pygame 图形绘制")

Gold = (255,251,0)
Red = pygame.Color("red")
White = 255,255,255
Green = pygame.Color("green")

# 开始绘制:
e1rect = pygame.draw.ellipse(screen, Green, (50,50,500,300), 3) # 头
c1rect = pygame.draw.circle(screen, Gold, (200,180), 30, 5)     # 左眼
c2rect = pygame.draw.circle(screen, Gold, (400,180), 30)        # 右眼
r1rect = pygame.draw.rect(screen, Red, (170,130,60,10), 3)      # 左眉毛
r2rect = pygame.draw.rect(screen, Red, (370,130,60,10))         # 右眉毛

plist = [(295,170), (285,250), (260,280), (340,280), (315,250), (305,170)]      # 顶点坐标的列表

l1rect = pygame.draw.aalines(screen, Gold, True, plist, 2)    # 鼻子
a1rect = pygame.draw.arc(screen, Red, (200, 220, 200, 100), 1.4*pi, 1.9*pi, 3)  # 嘴巴

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
