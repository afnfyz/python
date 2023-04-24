from pytube import YouTube
import ffmpeg
from datetime import datetime, timedelta
import io

# URL of the YouTube video
url = input("Input Youtube URL: ")

# Create YouTube object to retrieve video information
yt = YouTube(url)

# Get video duration
duration_seconds = yt.length

# Set start and end times in minutes:seconds format
start_time_input = input("Start time (mm:ss): ")
end_time_input = input("End time (mm:ss): ")

# Parse input times as time objects
start_time_obj = datetime.strptime(start_time_input, "%M:%S").time()
end_time_obj = datetime.strptime(end_time_input, "%M:%S").time()

# Calculate start and end times in seconds
start_time = start_time_obj.minute * 60 + start_time_obj.second
end_time = end_time_obj.minute * 60 + end_time_obj.second

# Validate input times
if start_time < 0 or start_time >= duration_seconds:
    print("Error: Start time is outside video duration.")
    exit()
if end_time < start_time or end_time > duration_seconds:
    print("Error: End time is outside video duration or before start time.")
    exit()

# Calculate duration of clip as timedelta object
duration = timedelta(seconds=end_time - start_time)

clip_name = input("Input name of clip: ")+".mp4"

# Stream video into memory using pytube
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
video_bytes = io.BytesIO()
stream.stream_to_buffer(video_bytes)
video_bytes.seek(0)

# Create ffmpeg input and output streams using a pipe
input_stream = ffmpeg.input('pipe:', format='mp4', loglevel='quiet', stdin=video_bytes)
output_stream = ffmpeg.output(input_stream, clip_name, ss=start_time, t=duration)

# Run ffmpeg to create the clip
ffmpeg.run(output_stream)
