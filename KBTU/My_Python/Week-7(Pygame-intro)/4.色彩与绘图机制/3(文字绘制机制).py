###################         3. 文字绘制机制


# 枚举机器上所有可用的字体
#  all_fonts = pygame.font.get_fonts()

                        pygame.font.Font() and pygame.font.SysFont()
'''
The difference between the two of them is that pygame.font.Font() requires the file path for a font to be passed into it’s parameters 
whereas pygame.font.SysFont() just requires the name of the font. You’ll understand where to use which in the examples shown below.
'''
pygame.font.Font("arial.ttf", 20)

font = pygame.font.Font(None, size) # 使用默认的字体

# The first parameter is the file path, and the second is the font size.

# 1.create a font type
dialogue_font = pygame.font.SysFont('arial',15,) # 在 SysFont , 我们只需要填字体的名称就可. 
# 2.render your font and create a surface object
dialogue = dialogue_font.render("Hey there, Beautiful weather today!",True, (0,0,0))    # (Text, 需要抗锯齿, 颜色)
# 3.display the object onscreen.
screen.blit(dialogue, (40,40))

                                
                                
                                
                                pygame.freetype
'''
向屏幕上绘制特点字体的文字
文字不能直接 print(), 而是用像素根据字体点阵图绘制

pygame.freetype 需要额外import 引用:  import pygame.freetype
'''

pygame.freetype.Font # 用此方法根据字体和字号生成一个Font对象

Font.render_to()
# or
Font.render()       # 用Font对象的render*方法绘制具体文字



                            ### 1.pygame.freetype.Font(file, size=0)
'''
此方法根据字体和字号生成一个Font对象
'''
file    字体类型名称或路径
size    字体的大小


                            ## 2.1 Font 类的绘制方法-1:
                        Font.render_to(surf, dest, text, fgcolor=None, bgcolor=None, rotation=0, size=0)
'''
返回 Rect 对象
'''
surf        绘制字体的平面, Surface 对象
dest        在平面中的位置, (x,y)
text        绘制的文字内容
fgcolor     文字颜色
bgcolor     背景颜色
rotation    逆时针的旋转角度,取值 0-359, 部分字体可旋转
size        文字大小,赋值该参数将覆盖Font中的设定值



                            ## 2.2 Font 类的绘制方法-2:
                        Font.render(text, fgcolor=None, bgcolor=None, rotation=0, size=0)
'''
返回 一个元组,包含Surface对象 和 Rect 对象
'''
text        绘制的文字内容
fgcolor     文字颜色
bgcolor     背景颜色
rotation    逆时针的旋转角度,取值 0-359, 部分字体可旋转
size        文字大小,赋值该参数将覆盖Font中的设定值



                            #  3.字形 text:
    font = pygame.font.Font(None, 25)   # (type, size)
    text = font.render("KBTU FIT", True, RED)
    screen.blit(text, (300, 300))   # (source, (x,y))

                            # 4. text rotating
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text2 = font.render("Programming Technologies", True, BLACK)
    text2 = pygame.transform.rotate(text2, 90)  # souce, angle
    screen.blit(text2, (0, 0))

    screen.blit(text2, (300, 300))   # (source, (x,y))

                            # 4.1 loop text rotating
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Programming Technologies", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    screen.blit(text, (100, 100))
    text_rotate_degrees += 1
    clock.tick(60)
    pygame.display.flip()


# https://blog.csdn.net/qq_41556318/article/details/86303502
                        ## 5.函数
pygame.font.init()  ——  初始化字体模块
pygame.font.quit()  ——  还原字体模块
pygame.font.get_init()  ——  检查字体模块是否被初始化
pygame.font.get_default_font()  ——  获得默认字体的文件名
pygame.font.get_fonts()  ——  获取所有可使用的字体
pygame.font.match_font()  ——  在系统中搜索一种特殊的字体
pygame.font.SysFont()  ——  从系统字体库创建一个 Font 对象
# SysFont(name, size, bold=False, italic=False) -> Font
                        
                        ## 6.类
pygame.font.Font   ——  从一个字体文件创建一个 Font 对象
# Font(filename, size) -> Font
# Font(object, size) -> Font

                        ## 7.方法
pygame.font.Font.render()  ——  在一个新 Surface 对象上绘制文本
pygame.font.Font.size()  ——  确定多大的空间用于表示文本
pygame.font.Font.set_underline()  ——  控制文本是否用下划线渲染
pygame.font.Font.get_underline()  ——  检查文本是否绘制下划线
pygame.font.Font.set_bold()  ——  启动粗体字渲染
pygame.font.Font.get_bold()  ——  检查文本是否使用粗体渲染
pygame.font.Font.set_italic()  ——  启动斜体字渲染
pygame.font.Font.metrics()  ——  获取字符串参数每个字符的参数
pygame.font.Font.get_italic()  ——  检查文本是否使用斜体渲染
pygame.font.Font.get_linesize()  ——  获取字体文本的行高
pygame.font.Font.get_height()  ——  获取字体的高度
pygame.font.Font.get_ascent()  ——  获取字体顶端到基准线的距离
pygame.font.Font.get_descent()  ——  获取字体底端到基准线的距离
