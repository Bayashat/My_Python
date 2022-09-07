import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    new_surf = pygame.Surface((640,480))
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))

    bastapky_x = -1   # 100
    bastapky_y = -1   # 100

    kazir_x = -1  # 300
    kazir_y = -1  # 300

    points = []

    mouse_down = False
    while True:
        
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                kazir_x = event.pos[0]
                kazir_y = event.pos[1]
                bastapky_x = kazir_x
                bastapky_y = kazir_y
                
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    kazir_x = event.pos[0]
                    kazir_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                new_surf.blit(screen, (0,0))

        if mouse_down and bastapky_x != -1 and bastapky_y != -1 and kazir_x != -1 and kazir_y != -1:
            screen.blit(new_surf, (0,0))
            
            point3 = [bastapky_x - (kazir_x-bastapky_x),kazir_y ]
            point4 = [bastapky_x, kazir_y + (kazir_y - bastapky_y)]

            pygame.draw.polygon(screen, (255,255,255), ([bastapky_x, bastapky_y],[kazir_x, kazir_y], point4, point3), 1)

        
        pygame.display.flip()
        
        clock.tick(60)


main()