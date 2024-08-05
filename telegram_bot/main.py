import asyncio
import os
from loguru import logger
from dotenv import load_dotenv

from aiogram.filters import CommandStart
from aiogram import Dispatcher

from handlers.users.base_handlers import *

load_dotenv()

logger.add('../debug.log', format='{time} | {level} | {message}', level='INFO',
           rotation='20 mb', compression='zip')

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()


async def main() -> None:
    try:
        bot = Bot(TOKEN)

        dp.message.register(show_start, CommandStart())

        try:
            await dp.start_polling(bot)
        finally:
            await bot.session.close()
    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    asyncio.run(main())
