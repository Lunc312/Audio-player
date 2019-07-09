from PyQt5 import QtWidgets
from MainWindow import Ui_Dialog
import sys

import songs


class mywindow(QtWidgets.QDialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def show_dialog(self):
        filename = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку с музыкой"))

        print(songs.get_songs_list(filename))


app = QtWidgets.QApplication([])
application = mywindow()
application.ui.pushButton_openf.clicked.connect(application.show_dialog)
application.show()

sys.exit(app.exec())
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MyMainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Dialog()
#     ui.setupUi(MyMainWindow)
#     ui.pushButton_openf.clicked.connect(qq)
#     MyMainWindow.show()
#     sys.exit(app.exec_())




