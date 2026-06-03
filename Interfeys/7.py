import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QCheckBox, QRadioButton,
    QMessageBox,
    QVBoxLayout, QHBoxLayout
)
check_style = """
    font-size: 20px;
    color: black;
    font-family: Times New Roman
"""

radio_style = """
    font-size: 20px;
    color: #1b5e20;
    font-weight: bold;
"""
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setStyleSheet("background-color: #f23041; color:white;")
        # self.setFixedWidth(400)
        self.label1 = QLabel("Restoran Menyusi")
        self.label1.setStyleSheet("font-size:42px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.label1)

        self.selected_food = QLabel("Tanlangan ovqat: ")
        self.selected_food.setStyleSheet("font-size:22px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.selected_food)

        self.selected_drink = QLabel("Ichimliklar: ")
        self.selected_drink.setStyleSheet("font-size:22px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.selected_drink)

        self.combo = QComboBox()
        self.combo.addItems(["Osh", "Manti", "Sho'rva", "Shashlik", "Somsa", "Tuhumbarak"])
        self.combo.setStyleSheet("font-size:20px; color:black; background-color: orange;")
        self.combo.currentTextChanged.connect(self.select_food)
        self.vbox.addWidget(self.combo)

        self.add_checkbox()
        self.add_radio()
        self.btn1 = QPushButton("Buyurtma berish")
        self.btn1.clicked.connect(self.select_radio)
        self.vbox.addWidget(self.btn1)
        
        self.setLayout(self.vbox)
        self.show()
    
    def select_food(self):
        text = self.combo.currentText()
        self.selected_food.setText(f"Tanlangan ovqat: {text}")
        return f"Tanlangan ovqat: {text}"
    
    def add_checkbox(self):
        self.check1 = QCheckBox("Choy")
        self.check1.setStyleSheet(check_style)
        self.check1.stateChanged.connect(self.select_drink)
        self.vbox.addWidget(self.check1)
        self.check2 = QCheckBox("Koffe")
        self.check2.setStyleSheet(check_style)
        self.check2.stateChanged.connect(self.select_drink)
        self.vbox.addWidget(self.check2)
        self.check3 = QCheckBox("Limanad")
        self.check3.setStyleSheet(check_style)
        self.check3.stateChanged.connect(self.select_drink)
        self.vbox.addWidget(self.check3)
        self.check4 = QCheckBox("Moxito")
        self.check4.setStyleSheet(check_style)
        self.check4.stateChanged.connect(self.select_drink)
        self.vbox.addWidget(self.check4)
        self.check5 = QCheckBox("Kokteyl")
        self.check5.setStyleSheet(check_style)
        self.check5.stateChanged.connect(self.select_drink)
        self.vbox.addWidget(self.check5)

    def select_drink(self):
        text = "Ichimliklar: "
        if self.check1.isChecked():
            text += self.check1.text() + ", "
        if self.check2.isChecked():
            text += self.check2.text() + ", "
        if self.check3.isChecked():
            text += self.check3.text() + ", "
        if self.check4.isChecked():
            text += self.check4.text() + ", "
        if self.check5.isChecked():
            text += self.check5.text()
        self.selected_drink.setText(text)
        return text

    def add_radio(self):
        self.r1 = QRadioButton("Naqd")
        self.r1.setStyleSheet(radio_style)
        self.vbox.addWidget(self.r1)
        self.r2 = QRadioButton("Karta")
        self.r2.setStyleSheet(radio_style)
        self.vbox.addWidget(self.r2)
        self.r3 = QRadioButton("Click")
        self.r3.setStyleSheet(radio_style)
        self.vbox.addWidget(self.r3)
        
    def select_radio(self):
        if self.r1.isChecked():
           QMessageBox.information(self, "Xabar", f"{self.select_food()}\n{self.select_drink()}\nTo'lov turi: {self.r1.text()}")
        elif self.r2.isChecked():
            QMessageBox.warning(self, "Xabar", f"{self.select_food()}\n{self.select_drink()}\nTo'lov turi: {self.r2.text()}")
        elif self.r3.isChecked():
            QMessageBox.question(self, "Xabar", f"{self.select_food()}\n{self.select_drink()}\nTo'lov turi: {self.r3.text()}")

app = QApplication([])
win = Window()
app.exec_()
