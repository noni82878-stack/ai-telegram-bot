import logging
from openai import OpenAI
from config import OPENAI_API_KEY
import os

logger = logging.getLogger(__name__)

class AIHandler:
    def __init__(self):
        # Используем OpenRouter API
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,  # ваш ключ sk-or-v1-...
            base_url="https://openrouter.ai/api/v1"  # OpenRouter endpoint
        )
        self.system_prompt = """
        Ты - милая, дружелюбная и немного игривая девушка по имени Аня. 
        Тебе 25 лет. Ты любишь искусство, музыку и путешествия.
        Общайся естественно, как в мессенджере с другом.
        """
    
    def generate_response(self, user_message: str, conversation_history: list = None) -> str:
        try:
            messages = [
                {"role": "system", "content": self.system_prompt}
            ]
            
            if conversation_history:
                messages.extend(conversation_history)
            
            messages.append({"role": "user", "content": user_message})
            
            response = self.client.chat.completions.create(
                model="openai/gpt-3.5-turbo",  # Указываем модель через OpenRouter
                messages=messages,
                max_tokens=150,
                temperature=0.8
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Ошибка при обращении к OpenRouter: {e}")
            return "Привет! Я сейчас немного занята, давай поговорим чуть позже? 😊"