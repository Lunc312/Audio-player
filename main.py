from MainWindow import QtWidgets, Ui_Dialog


def qq():
    print('Hello World')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyMainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MyMainWindow)
    ui.pushButton.clicked.connect(qq)
    MyMainWindow.show()
    sys.exit(app.exec_())




