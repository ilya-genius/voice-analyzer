import os
from fastapi import UploadFile, HTTPException

ALLOWED_MIME_TYPES = [
    "mp3",
    "wav",
    "ogg",
    "flac"
]


async def validate_audio_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext[1:] not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file extension. Allowed: {ALLOWED_MIME_TYPES}"
        )
    return file
