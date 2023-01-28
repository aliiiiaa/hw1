import aioschedule
import asyncio
from aiogram import types, Dispatcher
from config import bot
from handlers import client


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def write_the_satndup():
    for id in chat_id:
        await bot.send_message(id, "Ctrl C, Ctrl V\n #StandUp\n*что сделал: дз5\n*проблемы: были\n"
                                   " *что буду делать: повторять\n *исполнитель: Абылкасымова Алия")


async def scheduler():
    aioschedule.every().thursday.at("19:30").do(write_the_satndup)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(0.1)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "напомни" in word.text)