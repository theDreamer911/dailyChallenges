from pytube import YouTube
from moviepy.editor import *
import os
import shutil


def get_mp3():
    # Get URL
    url = input('Enter The Link: ')
    output = input('Which format you will use (wav/mp3): ')
    print('Converting...')

    # Download video and converting
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split('.mp4', 1)[0] + f".{output}"

    # Get audio
    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    # Ending


get_mp3()
