import os
os.system("cls")

from pytubefix import YouTube
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit
)

app  = QApplication([])
window = QWidget()

window.setGeometry(1400, 175, 400,700)
window.setStyleSheet("background-color: lightblue")

input1 = QLineEdit(window)
input1.setFixedSize(250, 50)
input1.move(75, 50)
input1.setStyleSheet("font-size: 20px; border: 2px solid black")
input1.setPlaceholderText("enter link...")

label1 = QLabel(window)
label1.setText("Video linkini joylang")
label1.setStyleSheet("font-size:30px; color:orange;")
label1.move(80, 150)
def downloader():
    link = input1.text()
    if not link:
        label1.setText("Iltimos link kiriting")
        return
    print(link)
    try:
        label1.setText("Ulanmoqda...")
        yt = YouTube(link)
        label1.setText("Jarayonda...")
        video = yt.streams.get_highest_resolution()
        label1.setText("Yuklanmoqda...")
        video.download("videos/")
    except:
        label1.setText("Yuklashda xatolik...")
    else:
        label1.setText("Yuklandi...")

btn1 = QPushButton(window)
btn1.setText("Download")
btn1.move(100,300)
btn1.setFixedSize(180, 60)
btn1.setStyleSheet("background-color: #10b040; font-size:28px; font-weight:bold; border-radius:20px; border: 2px solid black;")
btn1.clicked.connect(downloader)





window.show()
app.exec_()