import pygame
from bin.songsContainer import ListOfSongs
from bin.pickleClass import Pickler
from bin.playerSettings import PlayerSettings

mixer = pygame.mixer

class AudioPlayer(Pickler):
    currentList = None
    settings = None
    playing = False
    def __init__(self, alist=[]):
        AudioPlayer.currentList = ListOfSongs(songsPaths=alist)
        AudioPlayer.settings = PlayerSettings(volume=0.5)
        mixer.init()
    def play(self):
        AudioPlayer.playing = True
        NEXT = pygame.USEREVENT + 1
        mixer.music.set_endevent(NEXT)
        path, trackname = self.currentList.getTrack()
        mixer.music.set_volume(self.settings.getVolume())
        mixer.music.load(path)
        mixer.music.play()
        while pygame.mixer.music.get_busy():
            print("Playing track  - %s, volume: %s" % (trackname, self.settings.getVolume()))
            pygame.time.Clock().tick(0.5)
            pygame.init()
            for event in pygame.event.get():
                if event.type == NEXT:
                    self.next()
                if event.type == pygame.QUIT:
                    AudioPlayer.playing = False
    def stop(self):
        self.playing = False
    def pause(self):
        self.playing = False
    def next(self):
        AudioPlayer.currentList.currentTrack = (self._track()+1)%AudioPlayer.currentList.len()
        self.play()
    def previous(self):
        AudioPlayer.currentList.currentTrack = (self._track()-1)%AudioPlayer.currentList.len()
        self.play()
    def addNewSongs(self, newSongs):
        AudioPlayer.currentList.add(newSongs)
    def removeSong(self, index):
        AudioPlayer.currentList.removeSong(index)
    def saveCurrentPlayList(self):
        AudioPlayer.currentList.save()
    def volumeUp(self, value):
        AudioPlayer.settings.volumeUp(value)
    def volumeDown(self, value):
        AudioPlayer.settings.volumeDown(value)
    def _track(self):
        return AudioPlayer.currentList.currentTrack
    def __str__(self):
        return "%s: ListOfSongs = %s" % (
            self.__class__.__name__,
            AudioPlayer.currentList)
