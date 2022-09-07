import pygame, sys, pygame.freetype
'''

        1. pygame.font.Font()

        2. pygame.font.SysFont()
        
        all_fonts = pygame.font.get_fonts()  : get all the fonts



        3. pygame.freetype.Font()
        '''

pygame.init()

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")

f1 = pygame.freetype.Font("C:\Windows\Fonts\Verdana.ttf", 35)

f1.render_to(screen, (100,100),"Kazakhstan", fgcolor=(255,0,0),bgcolor= (0,255,0), size=50)
# 1-step
my_font = pygame.font.SysFont("stliti", 20)

font2 = pygame.font.Font(None, 20)

# 2-step: жазуды бояу
text =font2.render("Hello World",True, (255,0,0))

all_fonts = pygame.font.get_fonts()
print(all_fonts)
running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
    # 3-step:
    screen.blit(text, (300,200))
    pygame.display.update()

pygame.quit()

