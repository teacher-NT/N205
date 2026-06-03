import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setStyleSheet("background-color: lightblue; color:white;")
        self.setGeometry(1300, 175, 400, 700)
        self.label1 = QLabel("Salom Dunyo")
        self.vbox.addWidget(self.label1)

        self.btn1 = QPushButton("Tugmacha 1")
        self.vbox.addWidget(self.btn1)

        self.btn2 = QPushButton("Tugmacha 2")
        self.vbox.addWidget(self.btn2)

        self.btn3 = QPushButton("Tugmacha 3")
        self.vbox.addWidget(self.btn3)

        self.btn4 = QPushButton("Tugmacha 4")
        self.vbox.addWidget(self.btn4)
        self.setLayout(self.vbox)

        self.show()

app = QApplication([])
win = Window()
app.exec_()
