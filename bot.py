from aiogram import Bot, types, Dispatcher, executor

token = open('token.txt', 'r').read()

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Интеграция Дискорд бота в Телеграм')

executor.start_polling(dp, skip_updates=False) # skip_updates = True