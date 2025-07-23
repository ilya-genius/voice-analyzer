from openai import OpenAI
from app.core.config import settings


class AIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.deepseek_key,
            base_url=settings.base_url
        )
        print("AIService initialized")

    def analyze_text(self, text: str):
        try:
            response = self.client.chat.completions.create(
                model=settings.genai,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a text analysis assistant. Your task:
                    1. If the input contains a direct question - provide a concise answer first, then add explanations if needed
                    2. For statements/claims - give a balanced analysis highlighting key points, supporting evidence, and potential counterarguments
                    3. For ambiguous inputs - ask clarifying questions
                    4. Always maintain neutral, professional tone
                    5. Structure responses with clear paragraphs and bullet points when listing items"""
                    },
                    {"role": "user", "content": text}
                ],
                temperature=0.4,
                top_p=0.9,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI analysis failed: {str(e)}")
            raise