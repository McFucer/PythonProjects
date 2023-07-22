import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6081189075:AAFSbM13QeKN9cowUPCMzBuNuhlGpSBT3Co'
wikipedia.set_lang('ru')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Добро пожаловать в Wikipeida!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Я не нашел результатов на ваш запрос, попробуйте что-то дургой")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)