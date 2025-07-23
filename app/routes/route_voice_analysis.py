from fastapi import APIRouter, UploadFile, File, Depends
from app.models.schemas import AnalysisResponse
from app.services.audio_validation import validate_audio_file
from app.services.audio_service import AudioService
from app.services.ai_service import AIService
from app.core.dependencies import get_audio_service, get_ai_service
from app.core.config import settings

api_router = APIRouter()


async def audio_file_dependency(file: UploadFile = File(...)):
    await validate_audio_file(file)
    return file

@api_router.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Analyze voice message"
)
async def analyze_voice(
        file: UploadFile = Depends(audio_file_dependency),
        audio_service: AudioService = Depends(get_audio_service),
        ai_service: AIService = Depends(get_ai_service)):
    audio_data: bytes = await file.read()
    text = audio_service.speech_to_text(audio_data)
    analysis = ai_service.analyze_text(text)
    return AnalysisResponse(analysis=analysis)
