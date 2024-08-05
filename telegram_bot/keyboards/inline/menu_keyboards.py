from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, WebAppInfo, KeyboardButton


async def test_keyboard():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Play game', callback_data='test'),
            InlineKeyboardButton(text='Scoreboards', callback_data='test')
        ]
    ])

    return markup
