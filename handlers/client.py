from aiogram import Bot, types, Dispatcher, executor
from create import dp, bot

# @dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Интеграция Дискорд бота в Телеграм')

async def show_id(message: types.Message):
    await bot.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(show_id, commands=['id'])