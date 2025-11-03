import os
import subprocess
videos = os.listdir('downloads')
for video in videos:
    subprocess.run(['ffmpeg', '-i', os.path.join('downloads', video),f"audio/{video}.mp3"])
    print(f"Processed {video}")
