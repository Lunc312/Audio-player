from PyQt5 import QtWidgets
from MainWindow import Ui_Dialog
import sys

import songs


class mywindow(QtWidgets.QDialog):
    alist=[]
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def show_dialog(self):
        path_to_folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))
        mywindow.alist=songs.get_songs_list(path_to_folder)

        print (mywindow.alist)

    def play(self):
        songs.play_song(mywindow.alist)

    def stop(self):
        songs.Pause.toggle()

    def next(self):
        songs.song_next(mywindow.alist)

    def previous(self):
        songs.song_previous(mywindow.alist)


app = QtWidgets.QApplication([])
application = mywindow()
application.ui.pushButton_openf.clicked.connect(application.show_dialog)
application.ui.pushButton_play.clicked.connect(application.play)
application.ui.pushButton_stop.clicked.connect(application.stop)
application.ui.pushButton_next.clicked.connect(application.next)
application.ui.pushButton_previous.clicked.connect(application.previous)
application.show()

sys.exit(app.exec())

