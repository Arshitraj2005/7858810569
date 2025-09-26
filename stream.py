import gdown
import subprocess
import os

# 🎬 Google Drive IDs
video_drive_id = "1-MJuCDwkcLmUuTTHVuRKqKVY1fCb2qm6"   # Tumhara video ID
audio_drive_id = "1ilOvOl76gwquhWU-Xz78rcTOwLPdnizY"   # Tumhara audio ID

# Local file names
video_file = "video.mp4"
audio_file = "audio.mp3"

# 🔑 YouTube stream key
stream_key = "2c4f-5sy5-q7tx-cz4t-0c8r"   # Tumhara stream key
stream_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

def download_file(drive_id, output):
    if os.path.exists(output):
        print(f"✅ {output} already exists, skipping download.")
        return
    url = f"https://drive.google.com/uc?id={drive_id}"
    print(f"📥 Downloading {output}...")
    gdown.download(url, output, quiet=False)

def start_stream():
    # Download video + audio
    download_file(video_drive_id, video_file)
    download_file(audio_drive_id, audio_file)

    print("🚀 Starting 24x7 stream with video + audio (looped)...")
    command = [
        "ffmpeg", "-re",
        "-stream_loop", "-1", "-i", video_file,      # Loop video infinite
        "-stream_loop", "-1", "-i", audio_file,      # Loop audio infinite
        "-c:v", "libx264", "-preset", "veryfast",
        "-b:v", "2500k", "-maxrate", "2500k", "-bufsize", "5000k",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-map", "0:v:0", "-map", "1:a:0",
        "-g", "50", "-keyint_min", "50",   # Keyframe every 2 sec (25fps)
        "-f", "flv", stream_url
    ]

    subprocess.run(command)

if __name__ == "__main__":
    start_stream()
