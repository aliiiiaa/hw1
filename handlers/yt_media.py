from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from pytube import YouTube
from config import dp, bot
from uuid import uuid4
import os

class Download(StatesGroup):
    download = State()

def download_video(url, type='audio'):
    yt = YouTube(url)
    audio_id = uuid4().fields[-1]
    if type == 'audio':
        yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
        return f"{audio_id}.mp3"
    elif type == 'video':
        return f"{audio_id}.mp4"


async def start_dow(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}, скинь ссылку на видео и я отправлю ее тебе ввиде аудио.")
    await Download.download.set()

async def dowload(message: types.Message, state: FSMContext):
    title = download_video(message.text)
    audio = open(f'audio/{title}', 'rb')
    await message.answer(text=" На, держи")
    try:
        await bot.send_audio(message.chat.id, audio)
        await bot.send_message(message.chat.id, text='')
    except:
        return Exception
    os.remove(f'audio/{title}')
    await state.finish()


def register_handlers_yt(dp: Dispatcher):
    dp.register_message_handler(start_dow, commands='audio')
    dp.register_message_handler(dowload, state=Download.download)
