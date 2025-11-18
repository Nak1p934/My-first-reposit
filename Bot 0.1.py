from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
bot = "8417220012:AAFKjrPX0pKLdrp6uj_aPOrQV9m1E8EVQqc"
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Зиг халь")
    await message.reply_photo(photo="https://images.unsplash.com/photo-1761864534000-337153e88c92?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxODY2Nzh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjM0NjcxNTd8&ixlib=rb-4.1.0&q=80&w=1080", caption="Зацени")
@dp.message(Command("place"))
async def place(message: Message):
    await message.answer("IP: 333.222.111.000")

async def main():
    await dp.start_polling(Bot(bot))

if __name__ == "__main__":
    asyncio.run(main())









#from aiogram import Bot, Dispatcher
#from aiogram.types import Message
#from aiogram import F

#import asyncio

#TOKEN_API = "8417220012:AAFKjrPX0pKLdrp6uj_aPOrQV9m1E8EVQqc"

#bot = Bot(TOKEN_API)
#dp = Dispatcher()

#@dp.message(F.text)   # фильтр текста
#async def send_welcome(message: Message):
#    await message.answer("Hello! I'm your friendly bot. How can I assist you today?")

#async def main():
#    await dp.start_polling(bot)

#if __name__ == "__main__":
#    asyncio.run(main())
