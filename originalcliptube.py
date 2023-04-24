from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

# URL of the YouTube video
url = "https://www.youtube.com/watch?v=XKxUGGQSU-o"

# Download the video using pytube
yt = YouTube(url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
filename = stream.download()

# Clip the video using moviepy
clip = VideoFileClip(filename).subclip(10, 20)
clip.write_videofile('clip.mp4')
