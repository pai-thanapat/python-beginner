# 74. Style Sheet
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first GUI")
        self.setWindowIcon(QIcon("icon/happy.png"))

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px;
                               font-family: Arial;
                               padding: 15px 75px;
                               margin: 25px;
                               border: 3px solid;
                               border-radius: 15px;
                           }
                           QPushButton#button1{
                               background-color: rgb(232, 95, 95);
                           }
                           QPushButton#button2{
                               background-color: hsl(130, 75%, 64%);
                           }
                           QPushButton#button3{
                               background-color: #5ea5e8;
                           }
                           QPushButton#button1:hover{
                               background-color: hsl(130, 75%, 64%);
                           }
                           QPushButton#button2:hover{
                               background-color: #5ea5e8;
                           }
                           QPushButton#button3:hover{
                               background-color: rgb(232, 95, 95);
                           }
                           """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
