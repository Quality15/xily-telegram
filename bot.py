from aiogram import Bot, types, Dispatcher, executor
from create import bot, dp
from datetime import datetime

from colors import *

async def on_startup(_):
    print(f'{GREEN}Bot online ({datetime.now()})')

async def on_shutdown(_):
    print(f'{RED}Bot offline ({datetime.now()})')

from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=False, on_startup=on_startup, on_shutdown=on_shutdown) # skip_updates = True