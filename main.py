from flask import Flask
import subprocess
import threading

app = Flask(__name__)

def run_ffmpeg():
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1", "-i", "video.mp4",
        "-c:v", "libx264", "-preset", "veryfast", "-maxrate", "3000k",
        "-bufsize", "6000k", "-g", "60", "-c:a", "aac", "-ar", "44100",
        "-b:a", "128k", "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"
    ]
    subprocess.call(cmd)

@app.route("/")
def home():
    return "✅ Stream is running!"

if __name__ == "__main__":
    threading.Thread(target=run_ffmpeg).start()
    app.run(host="0.0.0.0", port=8080)
