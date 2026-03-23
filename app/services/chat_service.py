from openai import OpenAI

from app.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ChatService:
    def __init__(self):
        settings.validate()
        self.client = OpenAI(
            api_key=settings.api_key,
            base_url=settings.base_url,
        )
        self.model_name = settings.model_name

    def ask(self, user_input: str) -> str:
        logger.info("开始调用模型，model=%s", self.model_name)

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "你是一个简洁、可靠的中文 AI 助手。"},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.2,
            )

            answer = response.choices[0].message.content or ""
            logger.info("模型调用成功，返回长度=%s", len(answer))
            return answer

        except Exception as e:
            logger.error("模型调用失败: %s", e)
            raise