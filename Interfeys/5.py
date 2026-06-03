import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox,
    QVBoxLayout, QHBoxLayout
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setStyleSheet("background-color: #f23041; color:white;")
        self.setFixedWidth(400)
        self.label1 = QLabel("Restoran Menyusi")
        self.label1.setStyleSheet("font-size:42px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.label1)

        self.selected_food = QLabel("Tanlangan ovqat: ")
        self.selected_food.setStyleSheet("font-size:22px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.selected_food)

        self.combo = QComboBox()
        self.combo.addItems(["Osh", "Manti", "Sho'rva", "Shashlik", "Somsa", "Tuhumbarak"])
        self.combo.setStyleSheet("font-size:20px; color:black; background-color: orange;")
        self.combo.currentTextChanged.connect(self.select_food)
        self.vbox.addWidget(self.combo)

        self.btn1 = QPushButton("Tugmacha 1")
        self.vbox.addWidget(self.btn1)

        
        self.setLayout(self.vbox)
        self.show()
    
    def select_food(self):
        text = self.combo.currentText()
        self.selected_food.setText(f"Tanlangan ovqat: {text}")

app = QApplication([])
win = Window()
app.exec_()
