import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        self.model_name = os.getenv("MODEL_NAME", "default-model")

    def validate(self):
        if not self.api_key:
            raise ValueError("缺少 OPENAI_API_KEY")
        if not self.base_url:
            raise ValueError("缺少 BASE_URL")
        if not self.model_name:
            raise ValueError("缺少 MODEL_NAME")


settings = Settings()