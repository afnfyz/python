from pytube import YouTube
import ffmpeg

# URL of the YouTube video
url = input("Input Youtube URL: ")

# Download the video using pytube
yt = YouTube(url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
tmp_filename = 'video.mp4'
stream.download(output_path='./', filename=tmp_filename)

# Get video information using ffmpeg
probe = ffmpeg.probe(tmp_filename)
video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

# Set start and end times in seconds
start_time = int(input("Start time in seconds: "))
end_time = int(input("End time in seconds: "))
clip_name = input("Input name of clip: ")+".mp4"
# Create ffmpeg input and output streams
input_stream = ffmpeg.input(tmp_filename)
output_stream = ffmpeg.output(input_stream, clip_name, ss=start_time, t=end_time-start_time)

# Run ffmpeg to create the clip
ffmpeg.run(output_stream)

# Remove the temporary file
import os
os.remove(tmp_filename)
