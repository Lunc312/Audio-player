import os
from os.path import split, join, isdir, isfile
from bin.pickleClass import Pickler

class PlayList(Pickler):
    def __init__(self, songsPaths=[]):
        self.songsPaths = songsPaths.copy()
        self.currentTrack = 0
        self.name = "MyPlayList"

    # Adding, removing, song, updating playlist
    def append(self, newSong):
        if isfile(newSong):
            self.songsPaths.append(newSong)
        else:
            print("Неверно указанный файл ", newSong)
    def extend(self, iterableObj):
        self.songsPaths.extend(iterableObj)
    def add(self, newSongs):
        if isdir(newSongs):
            self.addSongsFromPath(newSongs)
            return
        newSongs = list(newSongs)
        if len(newSongs) > 1:
            self.extend(newSongs)
        elif len(newSongs) == 1:
            self.append(list(newSongs)[0])
        else:
            print("Добавление пустого списка")
    def removeSong(self, index):
        self.songsPaths.pop(index)
    def addSongsFromPath(self, path):
        songsPaths = [join(path, sp) for sp in os.listdir(path=path) if ".mp3" in sp]
        self.songsPaths.extend(songsPaths)

    # Получение доп информации
    def getSongsNames(self):
        names = []
        for p in self.songsPaths:
            _, tail = split(p)
            if tail:
                names.append(tail)
        return names
    def isEmpty(self):
        if self.songsPaths == []:
            return True
        else: return False
    def len(self):
        return len(self.songsPaths)
    def getTrack(self, index=None):
        if index == None: index = self.currentTrack
        return self.songsPaths[index], self.getSongsNames()[index]

    def save(self, dataFile="playlist"):
        Pickler.save(self, dataFile)
    @staticmethod
    def load(dataFile="playlist"):
        return Pickler.load(dataFile)

    def __str__(self):
        return str(self.getSongsNames())
    def __getitem__(self, index):
        return self.songsPaths[index]
