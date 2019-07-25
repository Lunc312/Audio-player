# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Programming\Python\Qt5\Audio-player\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 484)
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listView_songs = QtWidgets.QListView(Dialog)
        self.listView_songs.setObjectName("listView_songs")
        self.gridLayout.addWidget(self.listView_songs, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_topMenu = QtWidgets.QHBoxLayout()
        self.horizontalLayout_topMenu.setObjectName("horizontalLayout_topMenu")
        self.pushButton_openf = QtWidgets.QPushButton(Dialog)
        self.pushButton_openf.setObjectName("pushButton_openf")
        self.horizontalLayout_topMenu.addWidget(self.pushButton_openf)
        self.pushButton_playSound = QtWidgets.QPushButton(Dialog)
        self.pushButton_playSound.setObjectName("pushButton_playSound")
        self.horizontalLayout_topMenu.addWidget(self.pushButton_playSound)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_topMenu.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_topMenu.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_topMenu, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Тут будет картинка альбома"))
        self.pushButton_openf.setText(_translate("Dialog", "Открыть папку"))
        self.pushButton_playSound.setText(_translate("Dialog", "Play"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))

