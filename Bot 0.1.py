from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F

import asyncio

TOKEN_API = "твой токен"

bot = Bot(TOKEN_API)
dp = Dispatcher()

@dp.message(F.text)   # фильтр текста
async def send_welcome(message: Message):
    await message.answer("Hello! I'm your friendly bot. How can I assist you today?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
