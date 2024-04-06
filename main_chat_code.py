from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Замените 'YOUR_OPENAI_API_KEY' на ваш ключ API от OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота от BotFather
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при команде /start."""
    update.message.reply_text('Привет! Я бот, который использует AI для генерации ответов. Отправь мне сообщение, и я отвечу на него.')

def generate_response(message_text: str) -> str:
    """Генерирует ответ на сообщение с помощью OpenAI GPT."""
    response = openai.Completion.create(
      engine="text-davinci-003",  # Можете выбрать другую модель
      prompt=message_text,
      max_tokens=50  # Максимальное количество токенов в ответе
    )
    return response.choices[0].text.strip()

def message_handler(update: Update, context: CallbackContext) -> None:
    """Обрабатывает любые текстовые сообщения и отвечает на них."""
    user_message = update.message.text
    ai_response = generate_response(user_message)
    update.message.reply_text(ai_response)

def main():
    """Запускает бота."""
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
