import os
import subprocess

os.makedirs("audios", exist_ok=True)

files = os.listdir("videos")

for file in files:

    tutorial_number = file.split("[")[0].split("#")[1].strip()
    file_name = file.split("[")[1].split("]")[0]

    print(f"Processing: {file}")
    print(f"Output: audios/{tutorial_number}_{file_name}.mp3")

    subprocess.run([
        "ffmpeg",
        "-i",
        f"videos/{file}",
        f"audios/{tutorial_number}_{file_name}.mp3"
    ])
# ==========================================================
# VIDEO RAG PROJECT
# Stage 1: Video -> Audio Conversion
# ==========================================================
#
# PURPOSE
# -------
# This script converts lecture videos (.mp4) into audio files
# (.mp3) using FFmpeg.
#
# WHY THIS STAGE EXISTS
# ---------------------
# Large Language Models and vector databases cannot directly
# understand video files.
#
# Before we can generate transcripts, embeddings, or perform
# retrieval, the spoken content inside the videos must first
# be extracted as audio.
#
# The extracted audio will later be passed to Whisper for
# speech-to-text transcription.
#
# PIPELINE FLOW
# -------------
# Videos (.mp4)
#      ↓
# Audio Extraction (This Script)
#      ↓
# MP3 Files (.mp3)
#      ↓
# Whisper Transcription
#      ↓
# Transcript JSON
#      ↓
# Chunking
#      ↓
# Embeddings
#      ↓
# Vector Database
#      ↓
# Retrieval
#      ↓
# LLM Answer Generation
#
# INPUT EXAMPLE
# -------------
# videos/
# ├── Tutorial #1 [first video].mp4
# ├── Tutorial #2 [second video].mp4
#
# OUTPUT EXAMPLE
# --------------
# audios/
# ├── 1_first video.mp3
# ├── 2_second video.mp3
#
# NAMING STRATEGY
# ---------------
# The tutorial number is extracted from the filename:
#
#   Tutorial #1 [first video].mp4
#             ↑
#             tutorial number
#
# The text inside square brackets is extracted:
#
#   Tutorial #1 [first video].mp4
#                ↑
#                file name
#
# Result:
#
#   1_first video.mp3
#
# WHY KEEP THIS NAMING?
# ---------------------
# It creates a clear mapping between:
#
# video
#   ↓
# audio
#   ↓
# transcript
#
# Example:
#
# Tutorial #1 [first video].mp4
#          ↓
# 1_first video.mp3
#          ↓
# 1_first video.json
#
# This makes debugging and tracing files across the pipeline
# much easier.
#
# TOOLS USED
# ----------
# os
#   - Access files and folders
#   - Read video directory contents
#   - Create output directories
#
# subprocess
#   - Execute FFmpeg commands from Python
#
# ffmpeg
#   - Extract audio streams from video files
#
# SUCCESS CRITERIA
# ----------------
# For every video inside the videos/ folder:
#
# 1. An MP3 file is generated.
# 2. The output filename follows the project convention.
# 3. The MP3 plays correctly.
# 4. The file is ready for Whisper transcription.
#
# ==========================================================