import pygame,datetime
pygame.init()

screen=pygame.display.set_mode((800,600))
bg=pygame.transform.scale(pygame.image.load('mickeybg.jpeg'),(800,600))   # өлшемін өзгерту
sec=pygame.transform.smoothscale(pygame.image.load('mickeym.png'),(800,600))  # тегіс түрде масштабын өзгертеді
min=pygame.transform.smoothscale(pygame.image.load('mickeyh.png'),(800,600))
cl=pygame.time.Clock()

def r_center(s,image, angle, x, y): 
    r_image = pygame.transform.rotate(image, angle) 
    n_rect = r_image.get_rect(center=image.get_rect(center=(x, y)).center) 
    s.blit(r_image,n_rect)

run=True
while run:
    screen.blit(bg,(0,0))
    time=datetime.datetime.now()
    cl.tick(30)
    r_center(screen,sec,-time.second*6,400,300)   # Минус жаздық, чтобы оң бағытта айналу үшін, *6 өйткені 1с  = 6 градус
    r_center(screen,min,-time.minute*6-42,400,300)  # *6 өйткені 1минут  = 6 градус,  -42 өйткені суретіміз бастапқыда 42 ге градусқа солға қисайып тур
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update() 