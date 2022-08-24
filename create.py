from aiogram import Bot, types, Dispatcher, executor

token = open('token.txt', 'r').read()

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)