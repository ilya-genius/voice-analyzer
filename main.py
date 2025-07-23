import uvicorn
from fastapi import FastAPI
from app.routes import route_voice_analysis


def create_app():
    app = FastAPI(
        title="Voice Analysis API",
        version="0.1.0"
    )

    app.include_router(
        route_voice_analysis.api_router
    )

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
