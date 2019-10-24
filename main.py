from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MyMainWindow import Ui_MainWindow
from bin.audioPlayer import AudioPlayer
import sys

import songs


class MyWindow(QMainWindow):
    # Плеер: список песен, настройки, логика работы
    player = AudioPlayer()
    # Была нажата кнопка play и музыка играет? True - Да, False - Нет
    playing:bool = False

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Прикрепляем макет из Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем к QAction функцию и hotkey???
        self.ui.actionOpen_Directory.triggered.connect(self.show_dialog)
        self.ui.actionSave_current_AudioPlayer.triggered.connect(self.savePlayer)
        self.ui.actionLoad_AudioPlayer.triggered.connect(self.loadPlayer)

        self.ui.actionOpen_Directory.setShortcut( QKeySequence("Ctrl+o") )

        # Подключаем к слотам кнопок функции
        self.ui.pushButton_play.clicked.connect(MyWindow.player.play)
        self.ui.pushButton_pause.clicked.connect(MyWindow.player.pause)
        self.ui.pushButton_next.clicked.connect(MyWindow.player.next)
        self.ui.pushButton_previous.clicked.connect(MyWindow.player.previous)

    def show_dialog(self):
        songspaths = str(QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))

        # При отмене диалога, результатом будет пустая строка
        if songspaths == '':
            return

        MyWindow.player.addNewSongs(songspaths)

        self.updateList()

    def play(self):
        # Если список не пустой и песни не играют
        if (self.alist != []) & (not self.playing):
            self.start_playing()
            songs.play_song(self.alist)


    def pause_unpause(self):
        # Если список не пустой и песня играет
        if (self.alist != []):
            self.playing = False
            songs.Pause.toggle()

    def next(self):
        if self.alist != []:
            # Сразу воспроизводится
            self.start_playing()
            songs.song_next(self.alist)

    def previous(self):
        if self.alist != []:
            # Сразу воспроизводится
            self.start_playing()
            songs.song_previous(self.alist)

    def closeEvent(self, event):
        # Закрываем(убиваем процесс) плеер pygame.mixer
        songs.stop_playback()
        can_exit = True
        if can_exit:
            event.accept() # Let the window close
        else:
            event.ignore()

    def start_playing(self):
        self.playing = True
        # Если до этого была нажата кнопка паузы - отжимаем её
        if self.ui.pushButton_pause.isChecked():
            self.ui.pushButton_pause.toggle()
            songs.Pause.toggle()

    def updateList(self):
        # Создаём модель данных для ListView
        model = QStandardItemModel()
        self.ui.listView_songs.setModel(model)

        # Добавляем данные в модель
        for song in MyWindow.player.currentList.getSongsNames():
            item = QStandardItem(song)
            model.appendRow(item)

    def savePlayer(self):
        MyWindow.player.savePlayList()

    def loadPlayer(self):
        MyWindow.player.loadPlayList()
        self.updateList()



app = QApplication(sys.argv)
app.setWindowIcon(QIcon('./icons/hand-horns.png'))
window = MyWindow()
window.show()

sys.exit(app.exec())

