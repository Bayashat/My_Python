############    p2. 鼠标事件
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("pygame 事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.unicode == "" :
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)

        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
            print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)

        elif event.type == pygame.MOUSEBUTTONUP:    # 鼠标键释放事件
            print("[MOUSEBUTTONUP]:", event.pos, event.button)

        elif event.type == pygame.MOUSEBUTTONDOWN:   # 鼠标键按下事件
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
            
    pygame.display.update()
