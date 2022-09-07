############    2.鼠标事件及类型的使用

## pygame支持3种鼠标事件:
pygame.event.MOUSEMOTION        # 鼠标移动事件
pygame.event.MOUSEBUTTONUP      # 鼠标键释放事件
pygame.event.MOUSEBUTTONDOWN    # 鼠标键按下事件

                            ## 1).pygame.event.MOUSEMOTION        # 鼠标移动事件
'''
只有鼠标在移动,就会产生这个事件
返回三个属性值：

1.event.pos     鼠标当前坐标值(x,y), 相对于窗口左上角
2.event.rel     鼠标相对运动距离(X,Y), 相对于上次事件
3.event.buttons 鼠标按钮状态(a,b,c), 对应于鼠标的三个键
                鼠标移动时,这三个键处于按下状态,对应的位置值为1，
                反之则为0.
'''

                            ## 2).pygame.event.MOUSEBUTTONUP      # 鼠标键释放事件
'''
有2个属性:
1.event.pos  鼠标当前坐标值(x,y), 相对于窗口左上角
2.event.button  鼠标按下键编号n
                取值0/1/2, 分别对应三个键
'''


                            ## 3). pygame.event.MOUSEBUTTONDOWN   
# 鼠标键按下事件
'''
有2个属性:
1.event.pos  鼠标当前坐标值(x,y), 相对于窗口左上角
2.event.button  鼠标按下键编号n
                取值为整数, 左键为1, 右键为3, 设备相关
if event.type == pygame.MOUSEBUTTONDOWN:
if event.button == 1: # left click grows radius
    radius = min(200, radius + 1)
elif event.button == 3: # right click shrinks radius
    radius = max(1, radius - 1)
'''

                            ##  4).pygame.mouse.get_pressed（） 
# -像pygame.key.get_pressed（）一样，返回每个鼠标按钮的状态。返回的值是一个大小为3的元组，对应于左，中和右按钮。
left, middle, right = pygame.mouse.get_pressed()

if left:
    print("Left Mouse Key is being pressed")

# 也可以这样: 
mouse_presses = pygame.mouse.get_pressed()
 
if mouse_presses[0]:
    print("Left Mouse Key is being pressed")

# 以上这些,只要还在按住鼠标, print 函数就会一直输出

                            ##  5).Mouse Position
                        1.pygame.mouse.get_pos( )
#  返回鼠标光标的坐标。如果鼠标尚未在屏幕上移动，将返回（0，0）
print(pygame.mouse.get_pos())


                        2.get_rel()
# 返回以x和y为单位的移动量。换句话说，它给出了相对运动。
print(pygame.mouse.get_rel())

                        3.set_visible()
#  用于更改鼠标的可见性。简单来说，您可以通过将False传递给它来隐藏鼠标。
flag = 1
 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if flag == 1:
                    pygame.mouse.set_visible(False)
                    flag = 0
                elif flag == 0:
                    pygame.mouse.set_visible(True)
                    flag = 1

                        4.Other:
# 将鼠标的光标换成手:
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if event.key == pygame.K_2:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


                            ## 6.Collision with other Sprites/Rects
# 这是检测鼠标是否触摸精灵的一种非常方便的方法:
class Player:
    def __init__(self):
        self.rect = pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))
 
player = Player()
 
while 1:
    for event in pygame.event.get():
        ...
        ...
        if event.type == pygame.MOUSEBUTTONDOWN:           
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")
  
        if event.type == pygame.MOUSEBUTTONUP:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")