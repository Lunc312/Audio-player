"""Модуль содержит функции для работы с музыкальными файлами
и директориями в которых они находятся.

"""

# import os
import glob
import pygame
from pygame import mixer

pygame.init()
mixer.init()
current_track = 0
>>>>>>> develop


def get_songs_list(folder, key='*.mp3') -> list:
    """Возвращает список песен.
    Список состоит из полных путей к каждой песне,
    находящейся в директории folder.

    """
    # Если folder не указывает на папку,
    # тогда возвращаем пустой лист!
    if isfile(folder):
        return []

    songs_list = []

    try:
        songs_list = [join(normpath(folder), f) for f in os.listdir(folder) if '.mp3' in f]
    except:
        print("Что-то пошло не так!")
        return []

    return songs_list


def play_song(songs_list):
    """Воспроизводит песню."""
    global current_track
    tracks_number = len(songs_list)
    NEXT = pygame.USEREVENT + 1
    mixer.music.set_endevent(NEXT) 
    mixer.music.load(songs_list[current_track])
    mixer.music.play()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == NEXT:
                current_track = (current_track + 1) % tracks_number
                mixer.music.load ( songs_list[current_track] )
                mixer.music.play()




class Pause:
    paused = pygame.mixer.music.get_busy()

    def toggle():
        if Pause.paused:
            pygame.mixer.music.unpause()
        if not Pause.paused:
            pygame.mixer.music.pause()
        Pause.paused = not Pause.paused


def song_next(songs_list):
    global current_track 
    tracks_number = len(songs_list)
    current_track = (current_track + 1) % tracks_number
    play_song(songs_list)
>>>>>>> develop


def song_previous(songs_list):
    global current_track
    tracks_number = len(songs_list)
    current_track = (current_track - 1) % tracks_number
    play_song(songs_list)
