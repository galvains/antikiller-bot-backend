from typing import Union

from aiogram.types import Message, CallbackQuery
from database_api.interfaces import init_user
from telegram_bot.keyboards.reply.start_game_button import show_start_game_button


async def start_bot(message: Message):
    await message.reply("Привет! Я ваш бот.")


async def show_start(message: Union[Message, CallbackQuery]):
    init_user(data=message.from_user.__dict__)
    markup = await show_start_game_button()

    if isinstance(message, Message):
        await message.answer(text=f"Welcome to antikiller!\n Your username: {message.from_user.__dict__}",
                             reply_markup=markup)
