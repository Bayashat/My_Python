from turtle import Screen
import pygame, sys

pygame.init()

Screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My music palyer")

songs = ['Song1.mp3','Song2.mp3','Song3.mp3','Song4.mp3','Song5.mp3']
index = 0

pygame.mixer.music.load(songs[index])
pygame.mixer.music.play()

def change_index(index):
    if index == -1:
        index = 4
    elif index == 5:
        index = 0
    return index 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index -= 1
                index = change_index(index)

                pygame.mixer.music.load(songs[index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                index += 1
                index = change_index(index)
                
                pygame.mixer.music.load(songs[index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()

            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()

    pygame.display.update()