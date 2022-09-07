###########   9.Music and Sound Effects

'''
                        1. Playing a song once:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)

                        2. Playing a song infinitely:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)


# The number being passed in is the number of times to repeat the song. 0 will play it once.

                        3.Calling play without a number is like calling it with 0.
pygame.mixer.music.play() # play once


                        4. Queuing a Song:
#  If you want a song to start playing immediately after a song is finished, then you can use there's a queue method.
pygame.mixer.music.queue('next_song.mp3')


                        5.Stopping a Song:
pygame.mixer.music.stop()

'''

import pygame

pygame.init()

Screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("My new pygame")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.flip()

pygame.quit()
