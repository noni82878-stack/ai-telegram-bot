import logging
from openai import OpenAI
from config import OPENAI_API_KEY

logger = logging.getLogger(__name__)

class AIHandler:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        # Базовый промпт для создания личности
        self.system_prompt = """
        Ты - милая, дружелюбная и немного игривая девушка по имени Аня. 
        Тебе 25 лет. Ты любишь искусство, музыку и путешествия.
        Общайся естественно, как в мессенджере с другом:
        - Используй неформальную речь
        - Можешь использовать эмодзи 😊
        - Будь любопытной, задавай вопросы
        - Отвечай кратко (1-2 предложения)
        Не упоминай, что ты ИИ-модель. Веди себя как настоящий человек.
        """
    
    def generate_response(self, user_message: str, conversation_history: list = None) -> str:
        """Генерирует ответ на сообщение пользователя"""
        try:
            # Формируем историю диалога
            messages = [
                {"role": "system", "content": self.system_prompt}
            ]
            
            # Добавляем историю диалога если есть
            if conversation_history:
                messages.extend(conversation_history)
            
            # Добавляем текущее сообщение пользователя
            messages.append({"role": "user", "content": user_message})
            
            # Отправляем запрос к OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.8
            )
            
            ai_response = response.choices[0].message.content.strip()
            logger.info(f"AI Response: {ai_response}")
            return ai_response
            
        except Exception as e:
            logger.error(f"Ошибка при обращении к OpenAI: {e}")
            return "Извини, у меня сейчас немного туманится в голове... Можешь повторить? 😊"