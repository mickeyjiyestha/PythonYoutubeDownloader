from pytube import YouTube
from sys import argv

link = input("Masukan Link Youtube Video :")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('C:/Users/HP/Documents/MICKEY/PYTHON/.vscode/linkdownloader/videodownload')