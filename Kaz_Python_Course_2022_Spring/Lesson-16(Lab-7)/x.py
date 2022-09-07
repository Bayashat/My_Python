import pygame  
from datetime import datetime  
pygame.init()  
  
#global Variables  
WIDTH=1000 
HEIGHT=800  
FPS=20  
  
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
BLUE = (0, 0, 255)  
  
def blitRotateCenter(surf, image, topleft, angle):  
      
    rotated_image = pygame.transform.rotate(image, angle)  
      
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)  
  
    surf.blit(rotated_image, new_rect)  
  
#Initializing  
screen=pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption('MICKEY CLOCK')  
  
  
#Variables  
x,y = WIDTH // 2, HEIGHT // 2  
color = BLACK  
RAD = 10  
  
#Images  
mickey=pygame.image.load('background.jpg')  
mickey=pygame.transform.scale(mickey, (WIDTH, HEIGHT))  
right=pygame.image.load('min.jpg').convert()  
left=pygame.image.load('sec.jpg').convert()  
  
# #Music  
# pygame.mixer.music.load("./music/ticktack.mp3")  
# pygame.mixer.music.play(-1)  
  
clock=pygame.time.Clock()  
  
finished=False  
  
def time(time):  
    return 360-time*6  
  
while not finished:  
    clock.tick(FPS)  
  
    for event in pygame.event.get():  
        if event.type==pygame.QUIT:  
            finished=True  
  
    screen.blit(mickey, (0, 0))  
  
    t = datetime.now()  
  
    angle_sec = time(t.second+1)  
    angle_min = time(t.minute)  
  
    blitRotateCenter(screen, left, (WIDTH // 4 - 52, HEIGHT // 4 - 95), angle_sec)  
    blitRotateCenter(screen, right, (WIDTH // 4 - 52, HEIGHT // 4 - 90), angle_min)  
      
    pygame.draw.circle(screen, color, (x, y), RAD)  
      
    pygame.display.flip()  
pygame.quit()