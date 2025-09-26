import gdown
import subprocess
import os

# 🎬 Google Drive IDs
video_drive_id = "1-MJuCDwkcLmUuTTHVuRKqKVY1fCb2qm6"
audio_drive_id = "1ilOvOl76gwquhWU-Xz78rcTOwLPdnizY"

# Local file names
video_file = "video.mp4"
audio_file = "audio.mp3"

# 🔑 Your YouTube stream key
stream_key = "2c4f-5sy5-q7tx-cz4t-0c8r"
stream_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

def download_file(drive_id, output):
    if os.path.exists(output):
        print(f"✅ {output} already exists, skipping download.")
        return
    url = f"https://drive.google.com/uc?id={drive_id}"
    print(f"📥 Downloading {output}...")
    gdown.download(url, output, quiet=False)

def start_stream():
    download_file(video_drive_id, video_file)
    download_file(audio_drive_id, audio_file)

    print("🚀 Starting stream with video + audio...")
    command = [
        "ffmpeg", "-re",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "libx264", "-preset", "veryfast", "-tune", "zerolatency",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        "-map", "0:v:0", "-map", "1:a:0",  # video from 1st input, audio from 2nd
        "-shortest",
        "-f", "flv", stream_url
    ]

    subprocess.run(command)

if __name__ == "__main__":
    start_stream()
