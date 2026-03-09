from faster_whisper import WhisperModel

class WhisperEngine:
    def __init__(self, model_size="base"):
        self.model = WhisperModel(model_size)

    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path)

        text = ""
        for segment in segments:
            text += segment.text + " "

        return text.strip()