import whisper
audio_path = rf"audio\Core structure of HTML and Meta tags ｜ Hindi.mp4.mp3"
model = whisper.load_model("small")
result = model.transcribe(audio_path, language="hi", task='translate', word_timestamps=False)    
print(result['segments'])