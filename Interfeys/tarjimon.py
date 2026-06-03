import os
os.system("cls")
import pyttsx3

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QCheckBox, QRadioButton,
    QMessageBox, QTextEdit,
    QVBoxLayout, QHBoxLayout
)
from translate import Translator
check_style = """
    font-size: 20px;
    color: black;
    font-family: Times New Roman
"""

in_style = """
    font-size: 20px;
    color: black;
    font-weight: italic;
    height: 50px;
    border: 2px solid grey;
"""


btn_style = """
    font-size: 22px;
    color: black;
    background-color: lightgreen;
    font-weight: bold;
    height: 25px;
    border: 2px solid green;
    border-radius: 10px;
"""

btn2_style = """
    font-size: 22px;
    color: black;
    background-color: #5e80db;
    font-weight: bold;
    height: 25px;
    border: 2px solid green;
    border-radius: 10px;
"""



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setStyleSheet("background-color: #8ad1d1; color:white;")
        self.setFixedWidth(400)
        self.label1 = QLabel("Translator")
        self.label1.setStyleSheet("font-size:42px; color:black;font-family:Times New Roman;")
        self.vbox.addWidget(self.label1)

        self.from_combo = QComboBox()
        self.from_combo.addItems(["O'zbek - uz", "Rus - ru", "Ingliz - en", "Turk - tr", "Arab - ar", "Qozoq - kk"])
        self.from_combo.setStyleSheet("font-size:20px; color:black; background-color: #35dede;")
        self.vbox.addWidget(self.from_combo)

        self.from_text = QTextEdit()
        self.from_text.setPlaceholderText("Matn kiriting...")
        self.from_text.setStyleSheet(in_style)
        # self.from_text.textChanged(self.translate())
        self.vbox.addWidget(self.from_text)

        self.to_combo = QComboBox()
        self.to_combo.addItems(["O'zbek - uz", "Rus - ru", "Ingliz - en", "Turk - tr", "Arab - ar", "Qozoq - kk"])
        self.to_combo.setStyleSheet("font-size:20px; color:black; background-color: #35dede;")
        self.vbox.addWidget(self.to_combo)
       
        self.to_text = QTextEdit()
        self.to_text.setEnabled(False)
        self.to_text.setStyleSheet(in_style)
        self.vbox.addWidget(self.to_text)

        self.btn1 = QPushButton("Tarjima qilish")
        self.btn1.setStyleSheet(btn_style)
        self.btn1.clicked.connect(self.translate)
        self.vbox.addWidget(self.btn1)

        self.btn2 = QPushButton("Gapirish")
        self.btn2.setStyleSheet(btn2_style)
        self.btn2.clicked.connect(self.speak)
        self.vbox.addWidget(self.btn2)
        
        self.setLayout(self.vbox)
        self.show()

    def translate(self):
        _from = self.from_combo.currentText().split()[-1]
        _to = self.to_combo.currentText().split()[-1]
        text = self.from_text.toPlainText()
        tr = Translator(from_lang=_from, to_lang=_to)
        text = tr.translate(text)
        self.to_text.setText(text)
        return text
    
    def speak(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(self.translate())
        engine.runAndWait()

app = QApplication([])
win = Window()
app.exec_()
