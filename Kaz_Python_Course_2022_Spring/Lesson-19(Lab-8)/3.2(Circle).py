import pygame, math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    new_surf = pygame.Surface((640,480))
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))

    bastaopky_x = -1   # 100
    bastapky_y = -1   # 100

    kazir_x = -1  # 300
    kazyr_y = -1  # 300


    mouse_down = False
    while True:
        
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                kazir_x = event.pos[0]
                kazyr_y = event.pos[1]
                bastaopky_x = kazir_x
                bastapky_y = kazyr_y
                
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    kazir_x = event.pos[0]
                    kazyr_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                new_surf.blit(screen, (0,0))

        if mouse_down and bastaopky_x != -1 and bastapky_y != -1 and kazir_x != -1 and kazyr_y != -1:
            screen.blit(new_surf, (0,0))
            r = get_radius(bastaopky_x,bastapky_y, kazir_x, kazyr_y)
            pygame.draw.circle(screen, (255,255,255),(bastaopky_x, bastapky_y), r, 1  )

                
        def get_radius(bastaopky_x,bastapky_y, kazir_x, kazyr_y):
            return math.sqrt(((kazir_x-bastaopky_x)**2) + ((kazyr_y-bastapky_y)**2))
        
        pygame.display.flip()
        
        clock.tick(60)

main()