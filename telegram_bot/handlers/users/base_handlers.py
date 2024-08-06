from typing import Union

from aiogram.types import Message, CallbackQuery
from database_api.interfaces import init_user
from telegram_bot.keyboards.reply.start_game_button import show_start_game_button


async def start_bot(message: Message):
    await message.reply("Привет! Я ваш бот.")


async def show_start(message: Union[Message, CallbackQuery]):
    init_user(oauth_id=message.from_user.id, username=message.from_user.username)
    markup = await show_start_game_button()

    if isinstance(message, Message):
        await message.answer(text="Welcome to antikiller!", reply_markup=markup)
    # elif isinstance(message, CallbackQuery):
    #     call = message
    #     await call.message.edit_text(text="Welcome to antikiller!", reply_markup=markup)
