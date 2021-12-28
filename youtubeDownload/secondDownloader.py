import pytube
url = "https://www.youtube.com/watch?v=xhln61FaG-8"

youtube = pytube.YouTube(url)

choice = youtube.streams
for i in choice:
    print(i)

video = youtube.streams.get_by_resolution("360p")
video.download()

# video = youtube.streams.get_highest_resolution()

# video.download()