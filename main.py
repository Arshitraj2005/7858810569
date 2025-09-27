import threading
from stream import download_files, start_stream

if __name__ == "__main__":
    print("🔄 Downloading required files...")
    download_files()

    print("🚀 Starting Stream Thread...")
    stream_thread = threading.Thread(target=start_stream)
    stream_thread.start()
