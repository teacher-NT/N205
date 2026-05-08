import os
os.system("cls")

from pytubefix import YouTube

link = input("Video linkini kiriting: ")
try:
    yt = YouTube(link)
    print("Video yuklanmoqda...")
    video = yt.streams.get_highest_resolution()
    video.download("videolar/")
except:
    print("Video yuklashda xatolik...")
else:
    print("Video yuklandi...")