import asyncio
import os

from backend.app import app
from database_api.interfaces import init_questions
from database_api.models import Base, engine
from dotenv import load_dotenv
from loguru import logger

from telegram_bot.handlers.users.base_handlers import show_start, test

from aiogram.filters import CommandStart
from aiogram import Dispatcher, Bot

load_dotenv()

logger.add('debug.log', format='{time} | {level} | {message}', level='INFO',
           rotation='20 mb', compression='zip')
TOKEN = os.getenv('BOT_TOKEN')


async def start_app():
    try:
        Base.metadata.create_all(engine)
        init_questions()

        dp = Dispatcher()
        bot = Bot(TOKEN)
        app.run(port=5000)

        dp.message.register(show_start, CommandStart())

        try:
            await dp.start_polling(bot)
        finally:
            await bot.session.close()
    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    asyncio.run(start_app())
