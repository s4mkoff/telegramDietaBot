from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import InputMediaPhoto
from aiogram.types import InputMediaUnion
from aiogram.types import URLInputFile
from aiogram.types import message_entity
from dotenv import load_dotenv
import os

import asyncio

load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

image = URLInputFile(
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    filename="python-logo.png"
)

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Продовжити перегляд", callback_data="continue")],
    [InlineKeyboardButton(text="Моя кімнатка", callback_data="room"),
     InlineKeyboardButton(text="Поточні проекти", callback_data="projects")],
    [InlineKeyboardButton(text="Розклад", callback_data="schedule"),
     InlineKeyboardButton(text="Пошук", callback_data="search")],
    [InlineKeyboardButton(text="Опитування ❓", callback_data="poll"),
     InlineKeyboardButton(text="❤️ Підтримати", callback_data="support")],
    [InlineKeyboardButton(text="👾 Проблеми з ботом", callback_data="issues")]
])


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Amanogawa", reply_markup=menu)

@dp.callback_query(F.data)
async def handle_callback(call: types.CallbackQuery):
    media = InputMediaPhoto(media=image, caption=f"👉 Ви обрали: {call.data}")
    await call.message.edit_media(media=media, reply_markup=menu)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


