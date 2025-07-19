from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import InputMediaPhoto
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from models.Answer import Answer, MenuButton
import os

import asyncio

load_dotenv()
token = os.getenv("BOT_TOKEN")
if token is None:
    raise ValueError("BOT_TOKEN environment variable is not set")
bot = Bot(token=token)
dp = Dispatcher()

answer1 = Answer(
    imageSrc="images/image1.jpg",
    text="Привіт, я бот!",
    isKeyboard=True,
    buttons=[
        MenuButton(text="Continue", callback="continue")
    ]
)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привіт, я дієта-бот!", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text ="Меню", callback_data="menu")]]))

@dp.callback_query(F.data)
async def handle_callback(call: types.CallbackQuery):
    answer = answer1
    menu = answer.buttons
    image = FSInputFile(answer.imageSrc)
    keyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=btn.text, callback_data=btn.callback)]
            for btn in menu if isinstance(btn, MenuButton)
        ]
    )
    media = InputMediaPhoto(media=image, caption=f"{answer.text}")
    if call.message:
        await bot.edit_message_media(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            media=media,
            reply_markup=keyboardMarkup
        )
    else:
        await call.answer("Cannot edit media for this message.", show_alert=True)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


