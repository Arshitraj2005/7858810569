import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Stream is running!"

def start_stream():
    # apna YouTube stream key yaha daalo
    STREAM_KEY = "YOUR_YT_STREAM_KEY"

    # input video file ya link yaha daalo
    INPUT_VIDEO = "video.mp4"

    # ffmpeg command
    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",  # loop forever
        "-i", INPUT_VIDEO,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "2500k",
        "-maxrate", "2500k",
        "-bufsize", "5000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-f", "flv",
        f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]

    subprocess.Popen(command)

if __name__ == "__main__":
    # ffmpeg stream background me start karo
    start_stream()

    # Flask ko Render ke PORT pe bind karo
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
