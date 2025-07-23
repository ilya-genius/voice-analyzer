from transformers import pipeline
from app.core.config import settings


class AudioService:
    def __init__(self):
        self.pipe = pipeline(
            task="automatic-speech-recognition",
            model=settings.whisper,
            device=settings.device)
        print("AudioService initialized")

    def speech_to_text(self, audio_data: bytes) -> str:
        try:
            result = self.pipe(
                audio_data,
                return_timestamps=True
            )
            return result["text"]
        except Exception as e:
            print(f"Audio processing failed: {str(e)}")
            raise
