import pickle

if __name__ == "__main__":
    from songsContainer import ListOfSongs
else:
    from bin.songsContainer import ListOfSongs

class AudioPlayer():
    currentList = None
    def __init__(self, alist=[]):
        AudioPlayer.currentList = ListOfSongs(songsPaths=alist)
    def play(self):
        pass
    def stop(self):
        pass
    def pause(self):
        pass
    def save(self, dataFile="data"):
        with open("bin/config/"+dataFile, "wb") as file:
            pickle.dump(self, file)
    def __str__(self):
        return "%s: ListOfSongs = %s" % (self.__class__.__name__, AudioPlayer.currentList)
    @staticmethod
    def load(dataFile="data"):
        with open("bin/config/"+dataFile, "rb") as file:
            result = pickle.load(file)
        return result


if __name__ == "__main__":
    c = AudioPlayer()
    c.save()
    x = AudioPlayer.load()
    print(x)