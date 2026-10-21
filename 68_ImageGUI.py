# 66. PyQt5 introduction (GUI)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("icon/happy.png"))

        label = QLabel(self)
        pixmap = QPixmap("icon/happy.png")
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 250, 250)
        label.setScaledContents(True)
        label.setGeometry(
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height(),
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
