from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel
)

app  = QApplication([])

window = QWidget()
window.setWindowTitle("Mening birinchi dasturim")
window.setGeometry(1400, 175, 400, 700)
window.setStyleSheet("background-color: lightblue;")

label1 = QLabel(window)
label1.setText("Salom Suhrob")
label1.move(100, 10)
label1.setStyleSheet("font-size:28px; color:red")



window.show()
app.exec_()