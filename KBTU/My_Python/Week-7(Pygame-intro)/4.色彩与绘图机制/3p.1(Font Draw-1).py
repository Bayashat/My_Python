#########   3p.Font Draw-1:  using .render_to
import pygame,sys
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Pygame 文字绘制")

Gold = 255,251,0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)   # 形成一个 Font 类型
f1rect = f1.render_to(screen, (200,160), "世界和平", fgcolor=Gold, size = 50)   # 绘制字符串

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
