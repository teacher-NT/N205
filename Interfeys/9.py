import os
os.system("cls")

import requests as rq

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QVBoxLayout, QHBoxLayout
)

from PyQt5.QtCore import Qt

title_style = """
    font-size: 42px;
    font-family: Times New Roman;
"""
combo_style = """
    font-size: 25px;
    background-color: orange;
    color: white;
    border: 2px solid black;
    border-radius: 10px;
"""

btn_style = """
    font-size: 28px;
    background-color: green;
    color: yellow;
    border: 2px solid black;
    border-radius: 10px;
"""

class Convertor(QWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(500, 700)
        self.setStyleSheet("background-color: #bbbbbb;")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()

        self.title_label = QLabel("Valyutalar Kursi")
        self.title_label.setStyleSheet(title_style)
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.vbox.addWidget(self.title_label)

        self.add_input()
        self.add_combo()
        self.add_btn()

        self.setLayout(self.vbox)
        self.show()

    def add_input(self):
        self.input = QLineEdit()
        self.input.setFixedWidth(240)
        self.input.setAlignment(Qt.AlignCenter)
        self.result = QLabel("Natija")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setFixedHeight(40)
        self.input.setStyleSheet("""
                QLineEdit {
                    background-color: #f0f0f0;
                    border: 2px solid #cccccc;
                    border-radius: 5px;
                    padding: 8px;
                    font-size: 18px;
                    font-family: Arial;
                    color: #333333;
                }
                QLineEdit:focus {
                    border: 2px solid #4CAF50;
                    background-color: #ffffff;
                }
                QLineEdit:hover {
                    border: 2px solid #999999;
                }
            """)
        self.result.setStyleSheet("""
            QLabel {
                background-color: #e8f5e9;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                color: #1b5e20;
                font-family: Arial;
            }
        """)
        self.hbox1.addWidget(self.input)
        self.hbox1.addWidget(self.result)
        self.vbox.addLayout(self.hbox1)

    def add_combo(self):
        data = rq.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()
        self.valyutalar = QComboBox()
        self.valyutalar.addItems([i['CcyNm_UZ'] for i in data])
        self.valyutalar.setStyleSheet(combo_style)
        self.hbox2.addWidget(self.valyutalar)

        self.dir = QComboBox()
        self.dir.addItems(["So'mdan", "So'mga"])
        self.dir.setStyleSheet(combo_style)
        self.hbox2.addWidget(self.dir)

        self.vbox.addLayout(self.hbox2)

    def add_btn(self):
        self.btn1 = QPushButton("Hisoblash")
        self.btn1.setStyleSheet(btn_style)
        self.btn1.clicked.connect(self.hisoblash)
        self.hbox3.addWidget(self.btn1)

        self.btn2 = QPushButton("Narxlar")
        self.btn2.setStyleSheet(btn_style)
        self.hbox3.addWidget(self.btn2)

        self.vbox.addLayout(self.hbox3)

    def hisoblash(self):
        val = self.valyutalar.currentText()
        dir = self.dir.currentText()
        qiymat = float(self.input.text())
        data = rq.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()
        for i in data:
            if i['CcyNm_UZ'] == val:
                narx = float(i['Rate'])
                if dir == "So'mga":
                    res = narx * qiymat
                    self.result.setText(str(res))
                else:
                    res = qiymat / narx
                    self.result.setText(str(res))
                break


app = QApplication([])
win = Convertor()
app.exec_()

        