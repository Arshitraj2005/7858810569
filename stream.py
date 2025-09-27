import os
import subprocess

# ==== CONFIG ====
VIDEO_ID = "1-MJuCDwkcLmUuTTHVuRKqKVY1fCb2qm6"   # Google Drive Video ID
AUDIO_ID = "1SqqVbApLnkj8rSnmfYBH7Yva90MxhPwa"   # Google Drive Audio ID
STREAM_KEY = "2c4f-5sy5-q7tx-cz4t-0c8r"          # YouTube Stream Key

VIDEO_FILE = "video.mp4"
AUDIO_FILE = "audio.mp3"

def download_files():
    if not os.path.exists(VIDEO_FILE):
        print("📥 Downloading video...")
        os.system(f"gdown --id {VIDEO_ID} -O {VIDEO_FILE}")

    if not os.path.exists(AUDIO_FILE):
        print("📥 Downloading audio...")
        os.system(f"gdown --id {AUDIO_ID} -O {AUDIO_FILE}")

def start_stream():
    print("🚀 Starting YouTube Live Stream...")

    command = [
        "ffmpeg",
        "-stream_loop", "-1", "-re", "-i", VIDEO_FILE,   # video loop
        "-stream_loop", "-1", "-re", "-i", AUDIO_FILE,   # audio loop
        "-c:v", "libx264", "-preset", "veryfast", "-b:v", "2500k",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-pix_fmt", "yuv420p",
        "-shortest",  # dono sath me rahe
        "-g", "60", "-keyint_min", "60",  # YouTube keyframe fix
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]

    subprocess.run(command)
