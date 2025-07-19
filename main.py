from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from menu import newWeekMenu
import os
import asyncio

import asyncio

load_dotenv()
token = os.getenv("BOT_TOKEN")
if token is None:
    raise ValueError("BOT_TOKEN environment variable is not set")
bot = Bot(token=token)
dp = Dispatcher()

MEALS = ["breakfast", "morningSnack", "lunch", "eveningSnack", "dinner"]
DAYS = [
    ("Понеділок", 0), ("Вівторок", 1), ("Середа", 2), ("Четвер", 3),
    ("П’ятниця", 4), ("Субота", 5), ("Неділя", 6)
]

def menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Меню", callback_data="menu")]
        ]
    )

def days_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=day, callback_data=f"day_{idx}")]
            for day, idx in DAYS
        ]
    )

def meals_keyboard(day_idx):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=meal, callback_data=f"meal_{day_idx}_{idx}")]
            for idx, meal in enumerate(["Сніданок", "Перекус", "Обід", "Полуденок", "Вечеря"])
        ]
    )

def meal_nav_keyboard(day_idx, meal_idx):
    buttons = [
        InlineKeyboardButton(text="⬅️ До вибору прийому", callback_data=f"back_to_meals_{day_idx}")
    ]
    if day_idx < 6:
        buttons.append(InlineKeyboardButton(text="➡️ Далі", callback_data=f"next_meal_{day_idx}_{meal_idx}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])

def get_answer(day_idx, meal_idx):
    day = newWeekMenu.days[day_idx]
    meal_name = MEALS[meal_idx]
    meal = getattr(day, meal_name)
    return meal.answer

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("👋 Вітаю! Це бот-меню на тиждень.", reply_markup=menu_keyboard())

@dp.callback_query(F.data == "menu")
async def show_days(call: types.CallbackQuery):
    await call.message.edit_text("Оберіть день:", reply_markup=days_keyboard())
    await call.answer()

@dp.callback_query(F.data.startswith("day_"))
async def show_meals(call: types.CallbackQuery):
    day_idx = int(call.data.split("_")[1])
    await call.message.edit_text(f"Оберіть прийом їжі для {DAYS[day_idx][0]}:", reply_markup=meals_keyboard(day_idx))
    await call.answer()

@dp.callback_query(F.data.startswith("meal_"))
async def show_meal(call: types.CallbackQuery):
    _, day_idx, meal_idx = call.data.split("_")
    day_idx, meal_idx = int(day_idx), int(meal_idx)
    answer = get_answer(day_idx, meal_idx)
    image = FSInputFile(answer.imageSrc)
    await call.message.delete()
    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=image,
        caption=answer.text,
        reply_markup=meal_nav_keyboard(day_idx, meal_idx)
    )
    await call.answer()

@dp.callback_query(F.data.startswith("back_to_meals_"))
async def back_to_meals(call: types.CallbackQuery):
    day_idx = int(call.data.split("_")[-1])
    await call.message.delete()
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=f"Оберіть прийом їжі для {DAYS[day_idx][0]}:",
        reply_markup=meals_keyboard(day_idx)
    )
    await call.answer()

@dp.callback_query(F.data.startswith("next_meal_"))
async def next_meal(call: types.CallbackQuery):
    _, day_idx, meal_idx = call.data.split("_")
    day_idx, meal_idx = int(day_idx), int(meal_idx)
    if meal_idx < 4:
        meal_idx += 1
    else:
        day_idx += 1
        meal_idx = 0
    answer = get_answer(day_idx, meal_idx)
    image = FSInputFile(answer.imageSrc)
    await call.message.delete()
    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=image,
        caption=answer.text,
        reply_markup=meal_nav_keyboard(day_idx, meal_idx)
    )
    await call.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())