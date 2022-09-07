####################     0.music
import pygame

    # 1.加载. 必须在同一路径下
pygame.mixer.music.load('1.wav')    

    # Music.play()
pygame.mixer.music.play(0)  # play once
pygame.mixer.music.play(5)  # play 5 times
pygame.mixer.music.play(-1) # play infinitly
pygame.mixer.music.play() # play once

    # 3.Queuing a Song:     当前音乐播放结束后，将立即播放已排队的音频。
pygame.mixer.music.queue('next_song.mp3')

    # 4.Stopping a Song:    # 结束. isn't pause.
pygame.mixer.music.stop()

    # 5. Music.pause() and Music.unpause()  # 暂停和继续
pygame.mixer.music.pause()

pygame.mixer.music.unpause()

    # 5.Shuffle and Repeat: 随机播放:
_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.m']

    # 6. Music.set_endevent().  # 音乐停了的时候侦测
    '''
    此功能将数字作为参数，并在音乐停止播放后触发相应的事件'''
SONG_END = pygame.USEREVENT + 1     # 调用pygame.USEREVENT并添加1可以确保我们用户定义的事件的值是唯一的

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

...

while True:
    ...
    for event in pygame.event.get():
        ...
        if event.type == SONG_END:
            print("the song ended!")
    ...

    # 7. Other less common functions: 
pygame.mixer.music.rewind() – Rewinds the currently playing music to the start.
pygame.mixer.music.set_volume() – Takes values in between 0.0 and 1.0. When a new music piece is loaded, these settings reset.
pygame.mixer.music.get_busy() – Checks to see if music is currently playing or not. Returns False if not playing and True if it is.