##########   4.pygame event post  产生事件
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Pygame 事件处理")
fps = 1
fclock = pygame.time.Clock()
num = 1

while True:
    # 创建了一个我们自己的 KEYDOWN 事件:模拟了键盘中同时按下 SPACE 和 ALt
    my_event = pygame.event.Event(pygame.KEYDOWN, {"unicode":123, "key":pygame.K_SPACE, "mod":pygame.KMOD_ALT})
    pygame.event.post(my_event)
    num = num + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN {}]".format(num), "#", event.key, event.mod)
            else:
                print("[KEYDOWN {}]".format(num), event.unicode, event.key, event.mod)
    
    pygame.display.update()
    fclock.tick(fps)
