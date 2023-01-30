from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,  ADMINS
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random, sql_command_delete
from parser.doramy import parser_
from parser.anime import parser

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"мераба {message.from_user.first_name}")

async def quiz_1(message: types.Message):
    if message.chat.type != "private":
        markup = InlineKeyboardMarkup()
        button_call_1 = InlineKeyboardButton('2', callback_data='button_call_1')
        button_call_2 = InlineKeyboardButton('3', callback_data='button_call_2')
        markup.add(button_call_1)
        markup.add(button_call_2)

        question = "niçin manas?"
        answers = [
            "iyi eğitim",
            "Türkiye'de staj",
            "yemek",
        ]
        await bot.send_poll(
            chat_id=message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            explanation="tabii yemek",
            reply_markup=markup
        )

async def cmd_image(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=photo)

photo = open("media/img.jpg", 'rb')


async def pin(message: types.Message):
    if message.chat.type != "private":
        if not message.reply_to_message:
            await message.answer("Укажи что закрепить!")
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.id)
    else:
        await message.answer("Пиши в группе!")


async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    markup = None
    if message.from_user.id in ADMINS:
        markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(f"delete {random_user[0]}",
                                 callback_data=f"delete {random_user[0]}"))
    await message.answer(f"{random_user[0]} {random_user[1]} {random_user[2]} "
                f"{random_user[3]}",
        reply_markup=markup)


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await bot.send_message(call.data.replace("delete ", ""), "анкета метора удалена!")
    await call.answer(text="Deleted!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


async  def anime(message: types.Message):
    anime = parser()
    for i in anime:
        await bot.send_message(
            message.from_user.id,
            f"{i['Link']}\n\n"
            f"{i['Title']}\n"
            f"{i['Description']}\n"
            f"{i['Info']}"
        )
async  def doramy(message: types.Message):
    doramy = parser()
    for i in doramy:
        await bot.send_message(
            message.from_user.id,
            f"{i['Link']}\n\n"
            f"{i['Title']}\n"
            f"{i['Real_name']}\n"
            f"{i['Status']}"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cmd_image, commands=['meme'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!/")
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
    dp.register_message_handler(anime, commands=['anime'])
    dp.register_message_handler(doramy, commands=['dor'])
