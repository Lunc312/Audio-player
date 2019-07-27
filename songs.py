"""Модуль содержит функции для работы с музыкальными файлами
и директориями в которых они находятся.

"""

import os
import glob
import pygame
from pygame import mixer


def get_songs_list(folder, key='*.mp3') -> list:
    """Возвращает список песен.
    Список состоит из полных путей к каждой песне,
    находящейся в директории folder.

    """
    # Если folder не указывает на папку,
    # тогда возвращаем пустой лист!
    if not os.path.isdir(folder):
        return []

    songs_list = []

    try:
        for songname in glob.glob(os.path.join(folder, key)):
            songs_list.append(songname)
    except:
        print("Что-то пошло не так!")
        return []

    return songs_list


def play_song(path):
    """Воспроизводит песню."""
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()


def stop_song():
    """Останавливает песню."""
    mixer.music.stop()
