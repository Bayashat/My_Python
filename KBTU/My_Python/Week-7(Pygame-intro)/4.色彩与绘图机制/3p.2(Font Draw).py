#########   3p.Font Draw-2:  using .render
import pygame,sys
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Pygame 文字绘制")

Gold = 255,251,0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)   # 形成 Font 对象
f1surf, f1rect = f1.render("世界和平", fgcolor=Gold, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 使用 blit方法绘制到窗口
        screen.blit(f1surf, (200,160))
    pygame.display.update()
