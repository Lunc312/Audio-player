from bin.pickleClass import Pickler

class PlayerSettings(Pickler):
    def __init__(self, volume=0.5):
        self.volume = volume
    def volumeUp(self, value):
        if value >= 0:
            self.volume = value % 100
    def volumeDown(self, value):
        if value >= 0:
            self.volume = value % 100
    def getVolume(self):
        return self.volume

    def save(self, dataFile="settings"):
        Pickler.save(self, dataFile)
    @staticmethod
    def load(dataFile="settings"):
        return Pickler.load(dataFile)
