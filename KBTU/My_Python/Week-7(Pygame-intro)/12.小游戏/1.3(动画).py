###########   1.3.动画
'''
     计算机动画实际上就是把图像从一个地方移动到另一个地方，同时几个连接动作交待显示就会产生逼真的效果。
     因此，在做动画中，最基本要考虑的因素主要是三个，一是时间，什么时间移动，多长时间变下一个动作，二是位置，从什么位置到什么位置，三是动作，前后两个动作的连续性。
     在这个例子中，因为车是俯视的，所以车轮转动实际是看不到的，所以不用考虑连续动作的变化，而是只考虑车的位置和多长时间移动即可。第一步pygame.time.delay()来实现时间延迟；
     第二步利用pygame.draw.rect()把原来位置的图像覆盖掉；第三步screen.blit()在新位置引入图像。下面的例子实现了汽车从驶入到驶出的过程。
'''

import pygame,sys
def lineleft():
    plotpoints=[]
    for x in range(0,640):
        y=-5*x+1000
        plotpoints.append([x,y])
    pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
    pygame.display.flip()
def lineright():
    plotpoints=[]
    for x in range(0,640):
        y=5*x-2000
        plotpoints.append([x,y])
    pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
    pygame.display.flip()    
def linemiddle():
    plotpoints=[]
    x=300
    for y in range(0,480,20):
        plotpoints.append([x,y])
        if len(plotpoints)==2:
            pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
            plotpoints=[]
    pygame.display.flip() 
def loadcar(yloc):
    my_car=pygame.image.load('car1.jpg')
    locationxy=[310,yloc]
    screen.blit(my_car,locationxy)
    pygame.display.flip()

    
pygame.init()
screen=pygame.display.set_caption('hello world!')
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
lineleft()
lineright()
linemiddle()
fps = 15
fclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    for looper in range(480,-140,-50):
        # pygame.time.delay(200)
        fclock.tick(fps)
        pygame.draw.rect(screen,[255,255,255],[310,(looper+132),83,132],0)
        loadcar(looper)