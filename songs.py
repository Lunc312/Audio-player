"""Модуль содержит функции для работы с музыкальными файлами
и директориями в которых они находятся.

"""
import os
from os.path import isfile, join, normpath
import pygame
from pygame import mixer

pygame.init()
mixer.init()
current_track = 0
running = True

def get_songs_list(folder, key='*.mp3') -> list:
    """Возвращает список песен.
    Список состоит из двух списков: список полных путей
    и список имен песен, находящихся в директории folder.

    """
    # Если folder не указывает на папку,
    # тогда возвращаем пустой лист!
    if isfile(folder):
        return [[],[]]

    songs_paths = []
    songs_names = []

    try:
        for f in os.listdir(folder):
            if '.mp3' in f:
                # Записываем путь
                songs_paths.append(join(normpath(folder), f))
                # Записываем имя
                songs_names.append(f)
    except Exception as e:
        print("Что-то пошло не так!")
        print(type(e))
        return [[],[]]

    return [songs_paths, songs_names]


def play_song(songs_list):
    """Воспроизводит песню."""
    global current_track
    tracks_number = len(songs_list)
    NEXT = pygame.USEREVENT + 1
    mixer.music.set_endevent(NEXT)
    mixer.music.load(songs_list[current_track])
    mixer.music.play()

    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == NEXT:
                current_track = (current_track + 1) % tracks_number
                mixer.music.load(songs_list[current_track])
                mixer.music.play()
            if event.type == pygame.QUIT:
                running = False


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


def song_previous(songs_list):
    global current_track
    tracks_number = len(songs_list)
    current_track = (current_track - 1) % tracks_number
    play_song(songs_list)

def stop_playback():
    """Stop playback of all sound channels.
    This will stop all playback of all active mixer channels."""

    running = False
    mixer.music.set_endevent(pygame.QUIT)
    pygame.mixer.music.stop()