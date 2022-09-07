############    p1. 将每次用户按下的键以及返回的信息输出到屏幕上. Pygame Event print
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("pygame 事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # # 键盘按下事件

            if event.unicode == "" :    # 由于有些平台不支持 unicode 码, 所以若为空,则用 # 填充.
                print("[KEYDOWN]:", "#", event.key, event.mod)      # 有些unicode为空,所有要判断一下
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)
    pygame.display.update()
