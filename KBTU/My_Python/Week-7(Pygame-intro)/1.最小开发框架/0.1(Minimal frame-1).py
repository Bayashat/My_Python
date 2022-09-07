#################    0.1 Minimal Frame version-1

# 1. 引入 pygame 和 sys

import pygame,sys   

# 2.初始化 init 设置
pygame.init()       

screen = pygame.display.set_mode((600,400)) 
pygame.display.set_caption("Firse pygame")

# 3.获取事件并逐类响应
while True: # 无限循环,直到 Python 运行时退出结束
    for event in pygame.event.get():        # 从 pygame 的事件队列中取出事件, 并从队列中删除该事件.例如: 键盘按下是一个事件.
        if event.type == pygame.QUIT:
            sys.exit()
    
    # 4.刷新屏幕: 
    pygame.display.update()     # 对显示窗口进行更新, 默认窗口全部重绘.
