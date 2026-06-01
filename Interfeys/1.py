import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)

from PyQt5.QtGui import QFont
font1 = QFont("Times New Roman", 25)

app  = QApplication([])

window = QWidget()
window.setWindowTitle("Mening birinchi dasturim")
window.setGeometry(1400, 175, 400, 700)
window.setStyleSheet("background-color: lightblue;")

label1 = QLabel(window)
label1.setText("Counter")
label1.move(130, 10)
# label1.setStyleSheet("font-size:28px; color:red")
label1.setFont(font1)

label2 = QLabel(window)
label2.setText("0")
label2.move(175, 150)
label2.setFixedWidth(200)
label2.setStyleSheet("font-size:68px; color:orange;")

def func1():
    n = int(label2.text()) + 1
    label2.setText(str(n))

btn1 = QPushButton(window)
btn1.setText("Start")
btn1.move(100,300)
btn1.setFixedSize(200, 80)
btn1.setStyleSheet("background-color: #48d989; font-size:28px; font-weight:bold; border-radius:20px; border: 2px solid black;")
btn1.clicked.connect(func1)


def func2():
    label2.setText("0")
btn2 = QPushButton(window)
btn2.setText("Reset")
btn2.move(100,390)
btn2.setFixedSize(200, 80)
btn2.setStyleSheet("background-color: #eb2121; font-size:28px; font-weight:bold; border-radius:20px; border: 2px solid black;")
btn2.clicked.connect(func2)


window.show()
app.exec_()