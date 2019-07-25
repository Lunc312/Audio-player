"""Модуль содержит функции для работы с музыкальными файлами
и директориями в которых они находятся.

"""

import os
import winsound
from os.path import isfile, join, normpath


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


def play_song(path):
    """Воспроизводит песню."""
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_ALIAS)


def stop_song(path):
    """Останавливает песню."""
    return 0
