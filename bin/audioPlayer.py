import pygame
from bin.songsContainer import PlayList
from bin.pickleClass import Pickler
from bin.playerSettings import PlayerSettings

mixer = pygame.mixer

class AudioPlayer(Pickler):
    currentList:PlayList = None
    settings = None
    playing = False
    def __init__(self):
        AudioPlayer.currentList = PlayList()
        AudioPlayer.settings = PlayerSettings(volume=0.5)
        mixer.init()
    def play(self):
        AudioPlayer.playing = True
        # if mixer.music.get_busy():
        #     mixer.music.unpause()
        #     return
        NEXT = pygame.USEREVENT + 1
        mixer.music.set_endevent(NEXT)
        path, trackname = self.currentList.getTrack()
        mixer.music.set_volume(self.settings.getVolume())
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.init()
            for event in pygame.event.get():
                if event.type == NEXT:
                    self.next()
                if event.type == pygame.QUIT:
                    AudioPlayer.playing = False
        print(AudioPlayer.currentlist[self._track()], "ends.")
        for event in pygame.event.get():
            print(event.type)
            if event.type == NEXT:
                self.next()
            if event.type == pygame.QUIT:
                AudioPlayer.playing = False
    def stop(self):
        AudioPlayer.playing = False
    def pause(self):
        AudioPlayer.playing = False
        mixer.music.pause()

    def next(self):
        AudioPlayer.currentList.currentTrack = (self._track()+1)%AudioPlayer.currentList.len()
        self.play()
    def previous(self):
        AudioPlayer.currentList.currentTrack = (self._track()-1)%AudioPlayer.currentList.len()
        self.play()

    # PlayList
    def addNewSongs(self, newSongs):
        AudioPlayer.currentList.add(newSongs)
    def removeSong(self, index):
        AudioPlayer.currentList.removeSong(index)
    def saveCurrentPlayList(self):
        AudioPlayer.currentList.save()
    def savePlayList(self):
        AudioPlayer.currentList.save()
    def loadPlayList(self, playListName=""):
        if playListName == "":
            AudioPlayer.currentList = PlayList.load()
        else:
            AudioPlayer.currentList = ListOfSong.load(playListName)

    # Settings
    def volumeUp(self, value):
        AudioPlayer.settings.volumeUp(value)
    def volumeDown(self, value):
        AudioPlayer.settings.volumeDown(value)

    # Hide functions
    def _track(self):
        return AudioPlayer.currentList.currentTrack
    def __str__(self):
        return "%s: ListOfSongs = %s" % (
            self.__class__.__name__,
            AudioPlayer.currentList)
