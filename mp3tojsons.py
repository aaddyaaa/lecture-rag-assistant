# ==========================================================
# VIDEO RAG PROJECT
# Stage 2: Audio -> Chunks + Metadata
#
# Input:
# audios/
# ├── 1_first video.mp3
# ├── 2_second video.mp3
# ├── 3_third video.mp3
# └── 4_fourth video.mp3
#
# Output:
# jsons/
# ├── 1_first video.mp3.json
# ├── 2_second video.mp3.json
# ├── 3_third video.mp3.json
# └── 4_fourth video.mp3.json
#
# Each JSON contains:
# - Full transcript
# - Whisper segments
# - Video metadata
#
# ==========================================================

import os
import json
import whisper

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")

# Create output folder if it doesn't exist
os.makedirs("jsons", exist_ok=True)

# Read all audio files
audios = os.listdir("audios")

for audio in audios:

    # Skip non-mp3 files
    if not audio.endswith(".mp3"):
        continue

    # Example:
    # 1_first video.mp3

    number = audio.split("_")[0]
    title = audio.split("_")[1][:-4]

    print(f"\nProcessing: {audio}")
    print(f"Video Number: {number}")
    print(f"Video Title : {title}")

    # Speech-to-text using Whisper
    result = model.transcribe(
        audio=f"audios/{audio}",
        language="en",
        task="transcribe",
        word_timestamps=False
    )

    chunks = []

    # Extract timestamped segments
    for segment in result["segments"]:

        chunks.append({
            "number": number,
            "title": title,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    # Store full transcript + chunks
    chunks_with_metadata = {
        "video_number": number,
        "video_title": title,
        "text": result["text"],
        "chunks": chunks
    }

    # Save JSON
    output_path = f"jsons/{audio}.json"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks_with_metadata,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(f"Saved: {output_path}")

print("\nAll videos processed successfully!")