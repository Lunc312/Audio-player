from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MyMainWindow import Ui_MainWindow
from bin.audioPlayer import AudioPlayer
import sys

import songs

__version__ = 0.1.1


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
        self.ui.pushButton_play.clicked.connect(self.playStart)
        self.ui.pushButton_next.clicked.connect(self.playNextSong)
        self.ui.pushButton_previous.clicked.connect(self.playPrevSong)

    def show_dialog(self):
        songspaths = str(QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))

        # При отмене диалога, результатом будет пустая строка
        if songspaths == '':
            return

        MyWindow.player.addNewSongs(songspaths)

        self.updateList()

    def closeEvent(self, event):
        # Закрываем(убиваем процесс) плеер pygame.mixer
        AudioPlayer.stop_playback()
        can_exit = True
        if can_exit:
            event.accept() # Let the window close
        else:
            event.ignore()

    def updateList(self):
        """Обновляет список песен в правой части плеера."""
        # Создаём модель данных для ListView
        model = QStandardItemModel()
        self.ui.listView_songs.setModel(model)

        # Добавляем данные в модель
        for song in MyWindow.player.playList.getSongsNames():
            item = QStandardItem(song)
            model.appendRow(item)

    def closeEvent(self, event):
        # Закрываем(убиваем процесс) плеер pygame.mixer
        songs.stop_playback()
        can_exit = True
        if can_exit:
            event.accept() # Let the window close

    # Взаимодействие с плеером
    def savePlayer(self):
        MyWindow.player.savePlayList()

    def loadPlayer(self):
        MyWindow.player.loadPlayList()
        self.updateList()

    def playNextSong(self):
        MyWindow.player.stop_playback()
        MyWindow.player.next()
        MyWindow.player.play()

    def playPrevSong(self):
        MyWindow.player.stop_playback()
        MyWindow.player.previous()
        MyWindow.player.play()

    def playStop(self):
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/control.png"), QIcon.Normal, QIcon.Off)
        self.ui.pushButton_play.setIcon(icon2)
        self.ui.pushButton_play.setText("&Play")
        self.ui.pushButton_play.clicked.disconnect()
        self.ui.pushButton_play.clicked.connect(self.playStart)
        QMainWindow.update(self)
        MyWindow.player.pause()

    def playStart(self):
        if MyWindow.player.IsEmpty(): return
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/control-pause.png"), QIcon.Normal, QIcon.Off)
        self.ui.pushButton_play.setIcon(icon1)
        self.ui.pushButton_play.setText("&Pause")
        self.ui.pushButton_play.clicked.disconnect()
        self.ui.pushButton_play.clicked.connect(self.playStop)
        QMainWindow.update(self)

        if MyWindow.player.playing:
            MyWindow.player.unpause()
        else:
            MyWindow.player.play()




app = QApplication(sys.argv)
app.setWindowIcon(QIcon('./icons/hand-horns.png'))
window = MyWindow()
window.show()

sys.exit(app.exec())

