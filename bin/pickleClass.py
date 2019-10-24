import pickle

class Pickler:
    def save(self, dataFile="data"):
        with open("bin/config/"+dataFile, "wb") as file:
            pickle.dump(self, file) # 836
    @staticmethod
    def load(dataFile="data"):
        with open("bin/config/"+dataFile, "rb") as file:
            result = pickle.load(file)
        return result