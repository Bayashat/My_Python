#################   2.图形绘制机制

                    pygame.draw 
'''
.rect()     矩形            .line()     直线
.polygon()  多边形          .lines()    连续多线
.circle()   圆形            .aaline()   无锯齿线
.ellipse()  椭圆形          .aalies()   连续无锯齿线
.arc()      椭圆弧型
'''

'''
图形绘制后,返回一个矩形Rect类表示该形状
'''
                    pygame.Rect 
'''
表达一个矩形区域的类,用于存储坐标和长度信息. 
pygame 利用Rect类 =来操作图形/图像等元素.
有四个参数: 
(left, top)     # 左上角坐标
width           
height  
'''

                            ## 1.pygame.draw.rect(Surface, color, Rect, width=0)
Surface         # 矩形的绘制屏幕
color           # 矩形的绘制颜色
Rect(x, y, width , height)    # 矩形的绘制区域 
width=0         # 绘制边缘的宽度,默认为0,即填充图形


                            ## 2.pygame.draw.polygon(Surface, color, pointlist, width=0)
Surface         # 多边形的绘制屏幕
color           # 多边形的绘制颜色
pointlist       # 多边形顶点坐标列表
width=0         # 绘制边缘的宽度,默认为0,即填充图形


                            ## 3.pygame.draw.circle(Surface, color, center——pos, radius, width=0)
Surface         # 圆形的绘制屏幕
color           # 圆形的绘制颜色
pos             # 圆形的圆心坐标
radius          # 圆形的半径
width=0         # 绘制边缘的宽度,默认为0,即填充图形

                            ## 4.pygame.draw.ellipse(Surface, color, Rect, width=0)
Surface         # 椭圆形的绘制屏幕
color           # 椭圆形的绘制颜色
Rect(x, y, width , height)  # 椭圆形的绘制区域
width=0         # 绘制边缘的宽度,默认为0,即填充图形



                            ## 5.pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=0)
Surface         # 椭圆弧形的绘制屏幕
color           # 椭圆弧形的绘制颜色
Rect(x, y, width , height)   # 椭圆弧形的绘制区域
start_angle, stop_angle  # 弧形绘制起始和结束弧度值, 横向右侧为0度
width=0         # 绘制边缘的宽度,默认为0,即填充图形


                            ## 6.pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
Surface         # 直线的绘制屏幕
color           # 直线的绘制颜色
start_pos, end_pos  # 直线的起始和结束坐标
width=1         # 直线的宽度,默认值为1

                            ## 7.pygame.draw.lines(Surface, color, closed, pointlist, width=1)
Surface         # 连续多线的绘制屏幕
color           # 连续多线的绘制颜色
closed          # 如果为 True, 起止节点间自动增加封闭直线
pointlist       # 连续多线的顶点坐标列表
width=1         # 连续多线的宽度,默认值为1



                            ## 8.pygame.draw.aaline(Surface, color, start_pos, end_pos, blend=1)
Surface         # 无锯齿线的绘制屏幕
color           # 无锯齿线的绘制颜色
start_pos, end_pos  # 无锯齿线线的起始和结束坐标
blend=1         # 不为0时, 与线条所在背景颜色进行混合.


                            ## 9.pygame.draw.aalines(Surface, color, closed, pointlist, blend=1)
Surface         # 连续无锯齿线的绘制屏幕
color           # 连续无锯齿线的绘制颜色
closed          # 如果为 True, 起止节点间自动增加封闭直线
pointlist       # 连续无锯齿线的顶点坐标列表
blend=1         # 不为0时, 与线条所在背景颜色进行混合.
