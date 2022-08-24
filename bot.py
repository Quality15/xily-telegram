from aiogram import Bot, types, Dispatcher, executor
from datetime import datetime

from colors import *

token = open('token.txt', 'r').read()

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)

async def on_startup(_):
    print(f'{GREEN}Bot online ({datetime.now()})')

async def on_shutdown(_):
    print(f'{RED}Bot offline ({datetime.now()})')


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Интеграция Дискорд бота в Телеграм')

executor.start_polling(dp, skip_updates=False, on_startup=on_startup, on_shutdown=on_shutdownc;) # skip_updates = True