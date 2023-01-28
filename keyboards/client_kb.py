from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")

start_markup.add(start_button, quiz_button)


cancel_button = KeyboardButton("CANCEL")


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    cancel_button
)


group_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("backend dev"),
    KeyboardButton("frontendend dev"),
    KeyboardButton("UX/UI designer"),
    KeyboardButton("android  dev"),
    KeyboardButton("ios dev"),
    cancel_button
)


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    cancel_button
)