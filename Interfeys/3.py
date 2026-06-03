import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel
)

app = QApplication([])

# window = QWidget()
# window.setWindowTitle("Dastur")
# window.setGeometry(1300, 175, 400, 700)

# label1 = QLabel(window)
# label1.setText("Salom Dunyo")
# window.show()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dastur")
        self.setGeometry(1300, 175, 400, 700)
        self.label1 = QLabel(self)
        self.label1.setText("Salom Dunyo")
        self.show()

win = Window()
app.exec_()
