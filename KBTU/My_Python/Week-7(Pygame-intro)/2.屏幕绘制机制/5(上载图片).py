###################    5. 上载图片
import pygame,sys, os
## 第一种方式:
ball = pygame.image.load("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif")

## 第二种:

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

  

## 然后在 while loop 可以用 blit方法映射到指定的 区域:
pygame.blit(get_image("E:\KBTU\PP\Phyton\Week-7(Pygame-intro)\Images/ball.gif"), (300,300))