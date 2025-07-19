from aiogram import Router, F, Bot
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InputMediaPhoto
from menu import newWeekMenu
from models.Days import WeekDay, MealType
from keyboards.inline import (
    menu_keyboard, days_keyboard, meals_keyboard, meal_nav_keyboard, 
    MenuCallback, DayCallback, MealCallback
)

router = Router()

def get_answer(day: WeekDay, meal: MealType):
    return newWeekMenu.days[day].meals[meal].answer

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("👋 Вітаю! Це бот-меню на тиждень.", reply_markup=menu_keyboard())

@router.callback_query(MenuCallback.filter(F.action == "days"))
async def show_days(call: types.CallbackQuery, callback_data: MenuCallback):
    await call.message.edit_text("Оберіть день:", reply_markup=days_keyboard())
    await call.answer()

@router.callback_query(DayCallback.filter())
async def show_meals(call: types.CallbackQuery, callback_data: DayCallback, bot: Bot):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=f"Оберіть прийом їжі для {callback_data.day.value}:", 
        reply_markup=meals_keyboard(callback_data.day)
    )
    await call.answer()

@router.callback_query(MealCallback.filter(F.action == "show"))
async def show_meal(call: types.CallbackQuery, callback_data: MealCallback, bot: Bot):
    day = callback_data.day
    meal = callback_data.meal
    answer = get_answer(day, meal)
    image = FSInputFile(answer.imageSrc)
    
    caption = f"{day.value} - {meal.value}\n\n{answer.text}"

    await call.message.delete()
    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=image,
        caption=caption,
        reply_markup=meal_nav_keyboard(day, meal),
        parse_mode="HTML"
    )
    await call.answer()

@router.callback_query(MealCallback.filter(F.action == "next"))
async def next_meal_handler(call: types.CallbackQuery, callback_data: MealCallback):
    current_day = callback_data.day
    current_meal = callback_data.meal

    meal_types = list(MealType)
    current_meal_index = meal_types.index(current_meal)

    if current_meal_index < len(meal_types) - 1:
        next_meal_type = meal_types[current_meal_index + 1]
    else:
        await call.answer("Це останній прийом їжі на сьогодні.")
        return

    answer = get_answer(current_day, next_meal_type)
    image = FSInputFile(answer.imageSrc)
    
    caption = f"{current_day.value} - {next_meal_type.value}\n\n{answer.text}"

    await call.message.edit_media(
        media=InputMediaPhoto(media=image, caption=caption),
        reply_markup=meal_nav_keyboard(current_day, next_meal_type),
        parse_mode="HTML"
    )
    await call.answer()
