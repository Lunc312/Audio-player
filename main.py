from PyQt5 import QtWidgets
from MainWindow import Ui_Dialog
import sys

import songs

playlist = []


def check():
    if len(playlist) != 0:
        songs.play_song(playlist[0])


class mywindow(QtWidgets.QDialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_playSound.clicked.connect(check)

    def show_dialog(self):
        path_to_folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))

        global playlist
        playlist = songs.get_songs_list(path_to_folder)


app = QtWidgets.QApplication([])
application = mywindow()
application.ui.pushButton_openf.clicked.connect(application.show_dialog)
application.show()

sys.exit(app.exec())




