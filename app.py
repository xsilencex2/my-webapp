import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.client.default import DefaultBotProperties

# 🔑 Токен твоего Telegram-бота
TOKEN = "7906993633:AAFtMKmNZAt_j6J5xLNOKFy0aIXdX23R9VI"

# 🌐 URL твоего WebApp (например: GitHub Pages, Vercel и т.п.)
WEBAPP_URL = "https://xsilencex2.github.io/my-webapp/"

# 🔧 Создаем бота с дефолтным парсингом HTML
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# 📦 Dispatcher
dp = Dispatcher(storage=MemoryStorage())

# 👋 Обработка команды /start
@dp.message(lambda message: message.text == "/start")
async def start(message: Message):
    # Кнопка для WebApp
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Меню кафе", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])

    await message.answer(
        f"""
🍰 <b>Добро пожаловать в наше уютное кафе, {message.from_user.first_name}!</b>

☕ Здесь вы можете ознакомиться с меню и сделать заказ прямо через Telegram.

Нажмите кнопку ниже, чтобы открыть Web-приложение меню:
        """,
        reply_markup=keyboard
    )

# 🚀 Запуск бота
async def main():
    print("Бот запущен... 🟢")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
