from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6081189075:AAFSbM13QeKN9cowUPCMzBuNuhlGpSBT3Co')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Hello {message.from_user.first_name}')


@dp.message_handler(commands=['help'])
async def help(message):
    await message.answer('Help urself')


executor.start_polling(dp)


