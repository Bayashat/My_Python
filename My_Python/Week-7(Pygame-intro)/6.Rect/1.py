
                                        1）.Creating a Rect
                                1.Using the Rect Class
object = pygame.Rect((20, 50), (50, 100))   # top, left, width, height

# The above code creates a rect at coordinates (20, 50) and of width 50 and height 100.

                                2.Creating a Rect using an Image
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player_Sprite_R.png")
        self.rect = self.image.get_rect()   # 直接获取 Rect 对象

        self.rect = elf.image.get_rect(center = 10,10)  # 为在给定位置居中的Surface创建一个矩形

                                        2).Rect Functions
                                1.CollideRect
# 检测2个 Rect 对象是否接触.b 接触--True 
import pygame
 
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
object3 = pygame.Rect((0, 0), (50, 50))
 
print(object1.colliderect(object2)) # 1
print(object1.colliderect(object3)) # 0
print(object2.colliderect(object3)) # 1

                                 2. Move
# 按照一组 X，Y 坐标移动矩形, 并返回新的 Rect 对象:
object1 = pygame.Rect((20, 50), (50, 100))
 
object2 = object1.move(100, 100)
print(object1.topleft)  # (20,50)
print(object2.topleft)  # (120,150)

                                3.Move_ip
# 原地更改, 不返回新的
object1 = pygame.Rect((20, 50), (50, 100))
 
object1.move_ip(100, 100)
print(object1.topleft)  # (120,150)
                                
                                4.collidepoint
# 与CollidRecr 相似, 但是与一组 X,Y 坐标比较:
object1 = pygame.Rect((20, 50), (50, 100))
print(object1.collidepoint(50, 75))

                                5.collidelist
# 将 Rect 对象与列表里的 Rect 对象比较, 若与任意 Rect Object 碰撞, 返回其 Index
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
object3 = pygame.Rect((0, 0), (50, 50))
object4 = pygame.Rect((100, 100), (30, 50))
 
list = [object4, object3, object2]
print(object1.collidelist(list))        # 2

                                6. rect update
# 直接更改Rect 的坐标和大小:
import pygame
 
object1 = pygame.Rect((20, 50), (50, 100))
object1.update((30, 30), (50, 50))
print(object1.topleft)  # (30,30)
print(object1.size)     # (50,50)

                                7. Rect attributes:
>>> object1.y
50
>>> object1.x
20
>>> object1.topright
(70, 50)
>>> object1.center
(45, 100)
>>> object1.size
(50, 100)
>>> object1.height
100
>>> object1.right
70
>>> object1.midright
(70, 100)
>>> object1.w
50


