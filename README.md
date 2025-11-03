# 🎙️ Hindi Audio to English Text Transcriber (Whisper)

This project uses the **Whisper** speech-to-text model to transcribe Hindi audio files and translate them into English text. The output is saved in a structured JSON format for easy use in further applications such as NLP, search, or RAG systems.

---

## 🚀 Features

- Supports multiple audio files placed inside the `audio/` directory.
- Automatically transcribes and translates spoken Hindi into English text.
- Saves detailed metadata (including start & end time of segments, filename, and more) in `.json` format.
- Organizes JSON results into a dedicated `json/` directory.

---

## 🛠️ Requirements

- Python 3.8 or above
- [OpenAI Whisper Model](https://github.com/openai/whisper)
- `ffmpeg` installed and available in system PATH (for audio processing)

Python dependencies can be installed using:
```bash
pip install openai-whisper
