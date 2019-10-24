import pygame
from bin.songsContainer import PlayList
from bin.playerSettings import PlayerSettings

mixer = pygame.mixer

class AudioPlayer():
    # При создании выставляются настройки по умолчанию
    # создается миксер и пустой плейлист
    settings = None
    playing = False
    def __init__(self):
        self.playList = PlayList()
        AudioPlayer.settings = PlayerSettings(volume=0.15)
        mixer.init()

    # Playing music
    def play(self):
        AudioPlayer.playing = True
        NEXT = pygame.USEREVENT + 1
        pygame.event.clear()
        mixer.music.set_endevent(NEXT)
        path, trackname = self.playList.getTrack()
        print(trackname, "is playing.")
        mixer.music.set_volume(self.settings.getVolume())
        mixer.music.load(path)
        mixer.music.play()
        while AudioPlayer.playing:
            pygame.init()
            for event in pygame.event.get():
                if event.type == NEXT:
                    print(trackname, "ends.")
                    self.next()
                    path, trackname = self.playList.getTrack()
                    print(trackname, "is playing.")
                    mixer.music.load(path)
                    mixer.music.play()
                # Не уверен, что это нужно
                if event.type == pygame.QUIT:
                    AudioPlayer.playing = False
    def stop(self):
        AudioPlayer.playing = False
    def pause(self):
        mixer.music.pause()
    def unpause(self):
        mixer.music.unpause()

    def next(self):
        """Переводит на следующую песню, но не начинает играть её."""
        self.playList.currentTrack = (self._track()+1)%self.playList.len()

    def previous(self):
        """Переводит на предыдущую песню, но не начинает играть её."""
        self.playList.currentTrack = (self._track()-1)%self.playList.len()

    # PlayList
    def addNewSongs(self, newSongs):
        self.playList.add(newSongs)
    def removeSong(self, index):
        self.playList.removeSong(index)
    def saveCurrentPlayList(self):
        self.playList.save()
    def savePlayList(self):
        self.playList.save()
    def loadPlayList(self, playListName=""):
        if playListName == "":
            self.playList = PlayList.load()
        else:
            self.playList = PlayList.load(playListName)
    def IsEmpty(self):
        return self.playList.isEmpty()

    # Settings
    def volumeUp(self, value):
        AudioPlayer.settings.volumeUp(value)
    def volumeDown(self, value):
        AudioPlayer.settings.volumeDown(value)

    # Hide functions
    def _track(self):
        return self.playList.currentTrack
    def __str__(self):
        return "%s: ListOfSongs = %s" % (
            self.__class__.__name__,
            self.playList)

    @staticmethod
    def stop_playback():
        """Stop playback of all sound channels.
        This will stop all playback of all active mixer channels."""

        #AudioPlayer.playing = False
        mixer.music.set_endevent(pygame.QUIT)
        mixer.music.stop()