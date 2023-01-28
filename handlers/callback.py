from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def quiz_2(call: types.CallbackQuery):
        marku = InlineKeyboardMarkup()
        button_call_2 = InlineKeyboardButton('3', callback_data='button_call_2')
        marku.add(button_call_2)
        question = '[67 + 27?]'
        answers = [
            '[100]',
            '[94]',
            'DOKSAAN DÖÖÖÖRT',
        ]
        await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            explanation='tabii DOKSAAN DÖÖÖÖRT canım',
            # open_period=60,
        )

async def quiz_3(call: types.CallbackQuery):
        question = 'Bu akşam ölürüm, beni kimse tutamaz...?'
        answers = [
            'yıldızlar tutamaz',
            'sen beni tutamazsın',
            'gözlerin beni tutamaz',
            'bilmem:(',
        ]
        await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=1,
            explanation='Düşlerinde büyürüm, büyürüm\nKabusun olur ölürüm',
            # open_period=60,
        )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2')