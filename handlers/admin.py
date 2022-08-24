from tabnanny import check
from aiogram import Bot, types, Dispatcher, executor
from create import dp, bot

async def check_admin(message: types.Message):
    if message.from_user.id == '2146970447':
        await bot.send_message(message.chat.id, f'Вы админ!')
    else:
        await bot.send_message(message.chat.id, f'Вы не админ')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(check_admin, commands=['is_admin', 'check_admin'])