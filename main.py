from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import navigation
import os
import asyncio
from aiohttp import web

load_dotenv()

WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = 8080
# This URL is for local testing.
# You will need to replace it with your public URL from PythonAnywhere.
BASE_WEBHOOK_URL = ""

async def main():
    token = os.getenv("BOT_TOKEN")
    if token is None:
        raise ValueError("BOT_TOKEN environment variable is not set")
    
    # You will need to get this from your PythonAnywhere web app settings.
    base_url = os.getenv("PA_BASE_URL", BASE_WEBHOOK_URL)
    if not base_url:
        raise ValueError("BASE_WEBHOOK_URL environment variable is not set. For PythonAnywhere, set PA_BASE_URL.")

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(navigation.router)

    dp.startup.register(navigation.on_startup)
    dp.shutdown.register(navigation.on_shutdown)

    app = web.Application()
    
    webhook_requests_handler = web.Request.clone(
        default_body_size=65_536,  # 64 kb
    )
    webhook_requests_handler.add_subdivision(dp, bot=bot, base_url=base_url)
    
    app.router.add_post("/webhook", webhook_requests_handler.post)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
    await site.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
