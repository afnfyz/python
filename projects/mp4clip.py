import os
import ffmpeg
from datetime import datetime, timedelta

video_filename = "video.mp4"

if not os.path.exists(video_filename):
    print(f"Error: '{video_filename}' not found in the current directory.")
    exit()

# Get video information using ffmpeg
probe = ffmpeg.probe(video_filename)
video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

# Convert duration to seconds
duration_seconds = round(float(video_info['duration']))

while True:
    # Get start and end times from user
    start_time_str = input("Start time (mm:ss): ")
    end_time_str = input("End time (mm:ss): ")

    # Convert start and end times to timedelta objects
    try:
        start_time_timedelta = datetime.strptime(start_time_str, '%M:%S') - datetime(1900, 1, 1)
        end_time_timedelta = datetime.strptime(end_time_str, '%M:%S') - datetime(1900, 1, 1)
    except ValueError:
        print("Invalid time format. Please use mm:ss.")
        continue

    # Convert start and end times to seconds
    start_time = int(start_time_timedelta.total_seconds())
    end_time = int(end_time_timedelta.total_seconds())

    # Validate input times
    if start_time < 0 or start_time >= duration_seconds:
        print("Error: Start time is outside video duration.")
        continue
    if end_time < start_time or end_time > duration_seconds:
        print("Error: End time is outside video duration or before start time.")
        continue

    clip_name = input("Input name of clip: ")+".mp4"

    # Create ffmpeg input and output streams
    input_stream = ffmpeg.input(video_filename)
    output_stream = ffmpeg.output(input_stream, clip_name, ss=start_time, t=end_time-start_time)

    # Try to create the clip
    try:
        ffmpeg.run(output_stream)
    except:
        print("Error creating clip.")
        continue

    # Ask the user if they want to create another clip
    response = input("Do you want to create another clip? (y/n) ")
    if response.lower() == 'n':
        break
