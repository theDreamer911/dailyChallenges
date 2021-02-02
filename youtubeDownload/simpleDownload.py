from pytube import YouTube
from pathlib import Path
import sys
link = input('Link of Video: ')
save = input('Save into: ')
data_folder = Path(save)
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download(data_folder)
