from App.Handlers.handlers_level_3 import router_three
from App.Handlers.handlers_level_2 import router
from App.Handlers.handlers_level_1 import router_two
import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from Configuration.config import settings
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


async def main():
    dp.include_routers(router_two, router, router_three)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



