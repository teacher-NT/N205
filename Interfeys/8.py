import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout
)

class AboutWindow(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main_win = main_win
        self.vbox = QVBoxLayout()
        # self.setFixedWidth(400)
        self.setFixedSize(400, 700)
        self.setStyleSheet("background-color: lightblue;")

        self.label = QLabel("About")
        self.label.setStyleSheet("font-size: 20px; color: #000; ")
        self.vbox.addWidget(self.label)

        self.btn1 = QPushButton("Back")
        self.btn1.setStyleSheet("background-color: #102f85; font-size: 20px; color: white;")
        self.btn1.clicked.connect(self.back)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

    def back(self):
        self.main_win.show()
        self.hide()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        # self.setFixedWidth(400)
        self.setFixedSize(400, 700)
        self.setStyleSheet("background-color: #ccccad")

        self.label = QLabel("WeChat")
        self.label.setStyleSheet("font-size: 20px; color: #000; ")
        self.vbox.addWidget(self.label)

        self.btn1 = QPushButton("Next")
        self.btn1.setStyleSheet("background-color: #102f85; font-size: 20px; color: white;")
        self.btn1.clicked.connect(self.open_about)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
        self.show()

    def open_about(self):
        self.about = AboutWindow(self)
        self.about.show()
        self.hide()


app = QApplication([])
win = MainWindow()
app.exec_()