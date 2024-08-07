from typing import Union

from aiogram.types import Message, CallbackQuery
from database_api.interfaces import init_user, append_points, update_tasks, append_solved_user
from telegram_bot.keyboards.reply.start_game_button import show_start_game_button


async def test(message: Message):
    await message.reply("добавлены очки!")


async def show_start(message: Union[Message, CallbackQuery]):
    init_user(data=message.from_user.__dict__)
    # append_points(message.from_user.id, 1000)
    # update_tasks(task_id=2, value=34)
    append_solved_user(my_telegram_id=message.from_user.id, executor_id=23)
    markup = await show_start_game_button()

    if isinstance(message, Message):
        await message.answer(text=f"{message.from_user.username}, welcome to antikiller!", reply_markup=markup)
