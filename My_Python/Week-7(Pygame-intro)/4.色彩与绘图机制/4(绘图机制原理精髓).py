###############    4.pygame 绘图机制原理精髓

                        pygame.Surface
'''
绘图层,或绘图平面,或图层

用于表示图形,文字,或图像的绘制效果.
与当前屏幕主图层可以并列存在.
如果不绘制在主图层上,则不会被显示
'''
## Ex-1: Create 2 surface:
Surf1 = pygame.Surface((width, height))
Surf2 = pygame.Surface((width2, height2))

Surf1.fill((255,0,0))
Surf2.fill((0,255,0))

screen.blit(Surf1, (x,y))       # blit 方法将 Surf1 映射到 (x,y)点上

## Ex-2: 在多Surface情况时, 设置透明度:
Surf1 = pygame.Surface((width, height), pygame.SRCALPHA)
Surf2 = pygame.Surface((width2, height2))

Surf2.set_alpha(200)    # 设置透明度

'''
********************************************************************************************************************************************
'''
                        pygame.Rect
'''
矩形区域

对应于当前主图层的某个具体区域.
相当于某个矩形区域的指针或标识信息.
可以指定图层绘制在某个矩形区域中.
'''

    # 主图层
    # 由 pygame.display.set_mode()生成的 Surface 对象 : 
screen = pygame.display.set_mode((600,400))

    # 在主图层上绘制其他图层使用 .blit()方法：
screen.blit(ball, ballrect)
'''
我们将小球的图像表示为一个图层,叫 ball
然后,我们在主图层上选取一个区域,使用 ballrect 来表示它的位置.
我们使用 blit 方法就可以将这个图层(ball)绘制在主图层的 ballrect 区域上
'''

'''
*************************************************************************************************************************************************************
'''