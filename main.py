import MainWindow as mv


def qq():
    print('Hello World')


if __name__ == "__main__":
    import sys
    app = mv.QtWidgets.QApplication(sys.argv)
    MyMainWindow = mv.QtWidgets.QMainWindow()
    ui = mv.Ui_Dialog()
    ui.setupUi(MyMainWindow)
    ui.pushButton.clicked.connect(qq)
    MyMainWindow.show()
    sys.exit(app.exec_())




