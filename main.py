from PyQt5 import QtWidgets, QtGui
from MainWindow import Ui_Dialog
import sys

import songs


class mywindow(QtWidgets.QDialog):
    # Список путей к трекам
    alist = []
    # Список названий песен
    songs_names = []
    # Была нажата кнопка play и музыка играет? True-  Да, False - Нет
    playing:bool = False

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def show_dialog(self):
        path_to_folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))
        self.alist, self.songs_names = songs.get_songs_list(path_to_folder)

        print (self.alist)

        # Создаём модель данных для ListView
        model = QtGui.QStandardItemModel()
        self.ui.listView_songs.setModel(model)

        # Добавляем данные в модель
        for song in self.songs_names:
            item = QtGui.QStandardItem(song)
            model.appendRow(item)

    def play(self):
        # Если список не пустой и песни не играют
        if (self.alist != []) & (not self.playing):
            self.playing = True
            songs.play_song(self.alist)


    def pause_unpause(self):
        # Если список не пустой и песня играет
        if (self.alist != []):
            self.playing = False
            songs.Pause.toggle()

    def next(self):
        if self.alist != []:
            self.playing = True
            songs.song_next(self.alist)

    def previous(self):
        if self.alist != []:
            self.playing = True
            songs.song_previous(self.alist)


app = QtWidgets.QApplication([])
application = mywindow()
application.ui.pushButton_openf.clicked.connect(application.show_dialog)
application.ui.pushButton_play.clicked.connect(application.play)
application.ui.pushButton_stop.clicked.connect(application.pause_unpause)
application.ui.pushButton_next.clicked.connect(application.next)
application.ui.pushButton_previous.clicked.connect(application.previous)
application.show()

sys.exit(app.exec())

