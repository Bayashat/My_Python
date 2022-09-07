###########     1.键盘事件及类型的使用

## pygame支持两种键盘事件:
pygame.event.KEYDOWN    # 键盘按下事件
pygame.event.KEYUP      # 键盘释放事件

## 1.pygame.event.KEYDOWN    # 键盘按下事件
'''
当键盘的按下事件发生时,会返回3个信息:
1.event.unicode   按键的uincode码 (unicode 码与平台有关,不推荐使用)
2.event.key       按键的常量名称
3.event.mod       按键修饰符的组合值
event.mod = KMOD_ALT | KMOD_SHIFT
'''

    '''
    若用以下这种方式， 当你在按住 上下左右键它会一直move.
    
pressed = pygame.key.get_pressed()

if pressed[pygame.K_UP]: y -= step
elif pressed[pygame.K_DOWN]: y += step
elif pressed[pygame.K_LEFT]: x -= step
elif pressed[pygame.K_RIGHT]: x += step
'''


## 2.pygame.event.KEYUP      # 键盘释放事件
'''
键盘释放事件包含2个属性:
event.key       按键的常量名称
event.mod       按键修饰符的组合值
event.mod = KMOD_ALT | KMOD_SHIFT
'''