from os.path import split
from bin.pickleClass import Pickler

class ListOfSongs(Pickler):
    def __init__(self, songsPaths=[]):
        self.songsPaths = songsPaths.copy()
        self.currentTrack = 0
    def append(self, newSong):
        self.songsPaths.append(newSong)
    def extend(self, iterableObj):
        self.songsPaths.extend(iterableObj)
    def add(self, newSongs):
        newSongs = list(newSongs)
        if len(newSongs) > 1:
            self.extend(newSongs)
        elif len(newSongs) == 1:
            self.append(list(newSongs)[0])
        else:
            pass
    def removeSong(self, index):
        self.songsPaths.pop(index)
    def getSongsNames(self):
        names = []
        for p in self.songsPaths:
            _, tail = split(p)
            if tail:
                names.append(tail)
        return names
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
