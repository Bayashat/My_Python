##############   0.pygame 事件处理机制
'''
1.pygame 事件处理机制简介
2.键盘事件及类型的使用
3.鼠标事件及类型的使用
4.壁球小游戏(鼠标型)
5.pygame 事件处理函数
'''

## 1.事件处理需求：
'''
1.响应用户键盘,鼠标等外设操作
2.响应屏幕的尺寸和模式变化
3.响应游戏情节的特定触发条件
4.产生一些触发条件
'''

## 2. pygame.event.EventType
'''
本质上是一种封装后的数据类型(对象)
是pygame的一个类,表示事件类型.
事件类型只有属性,没有方法
用户可自定义新的事件类型
'''


##   3. pygame 提供了6种类型的事件类型:
'''
1. 系统:
        事件类型                属性
    QUIT                       None             退出
    ACTIVEEVENT                gain,state

2.键盘
    KEYDOWN                    unicode, key, mode   按键
    KEYUP                      key, mode            释放

3.鼠标
    MOUSEMOTION                pos, rel, buttons    鼠标的移动
    MOUSEBUTTONUP              pos, button          鼠标按键的按下
    MOUSEBUTTONDOWN            pos, button          鼠标按键的释放

4.游戏杆
    JOYAXISMOTION              joy, axis, value
    JOYBALLMOTION              joy, ball , rel
    JOYHATMPTION               joy, hat, value
    JOYBUTTONUP                joy, button
    JOYBBUTTONDOWN             joy, button

5.窗口
    VIDEORESIZE                size, w, h
    VIDEOEXPOSE                none

6.用户定义  
    USEREVENT                  code
'''

## 3.1 键盘落下事件及属性:
pygame.event.KEYDOWN
'''
对应3个参数:
event.unicode   键盘按下的对应键的uincode编码
event.key       键的常量名称
event.mod       # 键盘按下时键盘提供的状态模式
'''

## 4. 事件处理的重要函数:

# 1).处理事件:
pygame.event.get()
pygame.event.poll()
pygame.event.clear()

# 2).操作事件队列:
pygame.event.set_blocked()
pygame.event.get_blocked()
pygame.event.set_allowed()

# 3).生成事件:
pygame.event.post()
pygame.event.Event(type, dict)  