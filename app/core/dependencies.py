from app.services.audio_service import AudioService
from app.services.ai_service import AIService
from functools import lru_cache

@lru_cache()
def get_audio_service() -> AudioService:
    return AudioService()

@lru_cache()
def get_ai_service() -> AIService:
    return AIService()
