from random import choice
from aiogram import types, Dispatcher

async def game(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС!!")
        else:
            dices = ['🏀', '⚽', '🎯', '🎲', '🎰', '🎳']
            await bot.send_message(message.chat.id, random.choice(dices))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])