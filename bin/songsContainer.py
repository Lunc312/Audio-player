class ListOfSongs():
    def __init__(self, songsPaths=[]):
        self.songsPaths = songsPaths
    def append(self, newSong):
        self.songsPaths.append(newSong)
    def extend(self, iterableObj):
        self.songsPaths.extend(iterableObj)
    def __str__(self):
        return str(self.songsPaths)
    