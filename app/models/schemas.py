from pydantic import BaseModel, Field


class AnalysisResponse(BaseModel):
    analysis: str = Field(..., description="AI-generated analysis")