from aiogram import types
from aiogram.dispatcher.handler import SkipHandler

from bot.dispacher import dp, bot

user_id_required =  1899968635
chat_id_required = user_id_required  # Change for use in groups (user_id == chat_id in pm)


@dp.message_handler(user_id=user_id_required)
async def handler1(msg: types.Message):
    await bot.send_message(msg.chat.id, "Hello, checking with user_id=")
    raise SkipHandler  # just for demo


@dp.message_handler(chat_id=chat_id_required)
async def handler2(msg: types.Message):
    await bot.send_message(msg.chat.id, "Hello, checking with chat_id=")
    raise SkipHandler  # just for demo


@dp.message_handler(user_id=user_id_required, chat_id=chat_id_required)
async def handler3(msg: types.Message):
    await msg.answer("Hello from user= & chat_id=")


@dp.message_handler(user_id=[user_id_required, 42])
async def handler4(msg: types.Message):
    await msg.answer("Checked user_id with list!")