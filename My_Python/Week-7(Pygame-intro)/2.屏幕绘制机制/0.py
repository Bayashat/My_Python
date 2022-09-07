#############    0. pygame 屏幕绘制机制

'''
1.pygame 屏幕绘制机制简介
2.pygame 屏幕尺寸和模式设置
3.pyagme 窗口标题和图标设置
4.pygame 窗口感知和刷新运用
'''

## 1.屏幕绘制的重要函数:
'''
        1.屏幕尺寸和模式:
pygame.display.set_mode（）   设置相关屏幕模式
pygame.display.Info()         生成屏幕相关信息

        2.窗口标题和图标
pygame.display.set_caption()    设置标题信息
pygame.display.set_icon()       设置图标信息
pygame.display.get_caption()    获得图标

        3.窗口感知和刷新
pygame.display.get_active()
pygame.display.flip()
pygame.display.update()
'''

                    ## 1.1) 屏幕模式函数:
pygame.display.set_mode(r=(0,0), flags = 0)

# r 是游戏屏幕的分辨率,采用(width,height)方式输入
# flags 用来控制显示类型,可用 | 组合使用, 常用的如下:
pygame.RESIZABLE  # 窗口大小可调
pygame.NOFRAME    # 窗口没有边界显示 (无边框)
pygame.FULLSCREEN # 窗口全屏显示


                    ## 1.2) 屏幕信息函数-：
pygame.display.Info()
'''
产生一个显示对象VideoInfo , 表达当前屏幕的参数信息
在 .set_mode()之前调用,则显示当前系统显示参数信息.
这2个参数很重要:                            '''
current_w       # 当前显示模式或窗口的像素宽度
current_h       # 当前显示模式或窗口的像素高度


pygame.VIDEORESIZE
'''
这是一种窗口大小更改的事件
事件发生后,返回event.size元组,包含新窗口的宽度和高度

.size[0] 宽度, or event.w
.size[1] 高度, or event.h

返回参数仅在事件发生时有用          '''


                    ## 2) 窗口标题和图标设置
                        # 标题和图标函数
pygame.display.set_caption(title, icontitle=None)       
'''
title       设置窗口的标题内容
icontitle   设置图标化后的小标题
小标题可选,部分系统没有
'''


pygame.display.get_caption()
'''
返回当前设置窗口的标题及小标题内容
返回结构为(title, iocntitle)
该函数与游戏交互逻辑配合,可以根据游戏情节修改标题内容
'''

pygame.display.set_icon(surface)
'''
设置窗口的图标效果
图标是一个surface对象
'''
                        ## 3） 窗口感知和刷新设置:
                           # 屏幕控制函数
pygame.display.get_active() 
'''
当窗口在系统中显示(屏幕绘制/非图标化)时返回 True , 否则返回 False
该函数可以用来判断是否游戏窗口被最小化
进一步,判断后可以暂停游戏,改变响应模式等.               '''

pygame.dispaly.flip()   
'''
将重新绘制整个屏幕对应的窗口.
'''

pygame.display.update()
'''
仅重新绘制窗口中有变化的区域.执行速度更快.
'''