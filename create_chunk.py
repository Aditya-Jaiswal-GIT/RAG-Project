import os
import whisper
import json

# Load Whisper model
model = whisper.load_model("small")
print("Model loaded successfully")
number = 0
# Directory setup
audio_dir = "audio"
output_dir = "json"



# Get list of audio files
audios = os.listdir(audio_dir)

for audio in audios:
    audio_path = os.path.join(audio_dir, audio)
    print("Processing file:", audio)

    # Transcribe the audio file
    result = model.transcribe(audio_path, language="hi", task='translate', word_timestamps=False)

    # Build the chunk data
    chunk = []
    for segment in result.get('segments', []):
        chunk.append({
            'start': segment.get('start'),
            'end': segment.get('end'),
            'text': segment.get('text'),
            'audio_file': audio,
            'title' : audio.split(".mp3")[0],
            'number': number
        })
    
    # Create metadata
    chunk_metadata = {
        'chunks': chunk,
        'text': result.get('text', '')
    }
    number += 1
    # Create .json filename instead of .mp3
    json_filename = os.path.splitext(audio)[0] + ".json"
    json_path = os.path.join(output_dir, json_filename)

    # Save metadata to json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(chunk_metadata, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved JSON file to: {json_path}\n")
