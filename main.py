import logging

from aiogram import executor , types , Dispatcher , Bot
import environ
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = environ.Env(DEBUG =(bool , False))
environ.Env.read_env()

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = env('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot , storage=MemoryStorage())

@dp.message_handler(commands = 'start')
async def start_handler(msg: types.Message):
    await msg.reply('<b>Assalomu alaykum</b>','HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





