import os
import subprocess
import threading
from flask import Flask

# === CONFIG ===
STREAM_URL = f"rtmp://a.rtmp.youtube.com/live2/{os.getenv('STREAM_KEY')}"  
VIDEO_SOURCE = os.getenv("VIDEO_SOURCE", "video.mp4")  # Local file ya URL

app = Flask(__name__)
process = None

def start_stream():
    global process
    if process is not None:
        return "Stream already running!"

    # ✅ Optimized FFmpeg command for YouTube
    command = [
        "ffmpeg",
        "-re",  # real-time mode
        "-stream_loop", "-1",  # loop video forever
        "-i", VIDEO_SOURCE,  # input file/url
        "-c:v", "libx264",  # video codec
        "-preset", "veryfast",  # encoding speed
        "-b:v", "2500k",  # video bitrate (2.5 Mbps stable for Render free)
        "-maxrate", "2500k",
        "-bufsize", "5000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",  # keyframe interval (2s at 25fps)
        "-c:a", "aac",  # audio codec
        "-b:a", "128k",  # audio bitrate
        "-ar", "44100",  # audio sample rate
        "-f", "flv", STREAM_URL
    ]

    process = subprocess.Popen(command)
    return "Stream started!"

def stop_stream():
    global process
    if process:
        process.terminate()
        process = None
        return "Stream stopped!"
    return "No stream running!"

@app.route("/")
def home():
    return "✅ YouTube Livestream Bot Running!"

@app.route("/start")
def start():
    return start_stream()

@app.route("/stop")
def stop():
    return stop_stream()

@app.route("/status")
def status():
    return "Running ✅" if process else "Stopped ❌"

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000)).start()
