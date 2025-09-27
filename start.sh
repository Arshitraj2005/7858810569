#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Install ffmpeg
apt-get update && apt-get install -y ffmpeg

# Run main script
python3 main.py
