import pygame

pygame.init()
            #######  1.
s = pygame.mixer.Sound('CarCrash.mp3')
s.play()
'''
# Step-1: Жүктеу:
pygame.mixer.music.load('test1.mp3')

# Step-2: Music.play()
pygame.mixer.music.play()  # play once

pygame.mixer.music.play(4)  # play 4
pygame.mixer.music.play(-1)  # play infinitly
pygame.mixer.music.play()  # play once

##############          2. Queuing a song
pygame.mixer.music.queue('2.mp3')

############            3. Stopping a song:
pygame.mixer.music.stop()

############            4. pause and unpause
pygame.mixer.music.pause()
pygame.mixer.music.unpause()

############3           5. Music.set_endevent()
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.music.load('2.mp3')
pygame.mixer.music.play()
'''
screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) 
pygame.display.set_caption("First my pygame")

running = True    
while running:
    # Event :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()   # sys.exit()
        #elif event.type == SONG_END:
         #   print("The song ended!")

    pygame.display.flip()   # update()

pygame.quit()

