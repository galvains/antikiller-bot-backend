from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


async def show_start_game_button():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Play game', web_app=WebAppInfo(url='https://www.sagemath.org'))
        ]
    ])

    return markup
