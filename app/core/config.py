from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    deepseek_key: str = ""
    base_url: str = "https://api.deepseek.com"
    whisper: str = "openai/whisper-tiny"
    genai: str = "deepseek-chat"
    device: str = "cpu"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
