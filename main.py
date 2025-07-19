from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import navigation
import os
import asyncio

load_dotenv()

async def main():
    token = os.getenv("BOT_TOKEN")
    if token is None:
        raise ValueError("BOT_TOKEN environment variable is not set")
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(navigation.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())