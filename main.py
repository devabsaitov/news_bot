import logging
from aiogram import executor
from bot.handler import *

if __name__ == '__main__':
    log = logging.getLogger('broadcast')
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)





