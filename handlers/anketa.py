from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import ADMINS
from uuid import uuid4
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    group = State()
    dir = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.from_user.id in ADMINS:
        await FSMAdmin.name.set()
        await message.answer("Как зовут ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Вы не админ!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = str(uuid4())
        data["name"] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет ментору?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 15 < int(message.text) < 70:
        await message.answer("Доступ ограничен!")
    else:
        async with state.proxy() as data:
            data["age"] = message.text
        await FSMAdmin.next()
        await message.answer("Группа?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
    await FSMAdmin.next()
    await message.answer("Направление ментора?",
                         reply_markup=client_kb.group_markup)



async def load_dir(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["dir"] = message.text
    await message.answer(f"имя: {data['name']}\n ID: {data['id']}\n возраст: {data['age']}\n"
                         f" группа: {data['group']}\n направление: {data['dir']}\n")
    await FSMAdmin.next()
    await message.answer("Все верно?",
                         reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
    elif message.text.lower() == "заново":
        await FSMAdmin.name.set()
        await message.answer("Как зовут ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Данной команды не существует!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_dir, state=FSMAdmin.dir)

    dp.register_message_handler(submit, state=FSMAdmin.submit)