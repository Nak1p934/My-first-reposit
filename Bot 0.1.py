from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "8417220012:AAFKjrPX0pKLdrp6uj_aPOrQV9m1E8EVQqc"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.reply("Hello! I'm your friendly bot. How can I assist you today?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
