#!/bin/bash
echo "🚀 Starting YouTube Live Stream service..."

# Run Flask (background me)
python3 main.py &

# Run Stream
python3 stream.py
