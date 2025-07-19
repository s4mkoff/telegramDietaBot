from aiogram import Router, F, Bot
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InputMediaPhoto
from menu import newWeekMenu
from models.Days import WeekDay, MealType
from models.Answer import KiloType
from keyboards.inline import (
    menu_keyboard, days_keyboard, meals_keyboard, meal_nav_keyboard, kilo_keyboard,
    MenuCallback, DayCallback, MealCallback, KiloCallback, StartCallback
)

router = Router()

def get_answer(day: WeekDay, meal: MealType, kilo_type: KiloType, variant_index: int = 0):
    return newWeekMenu.days[day].meals[meal].answers[variant_index].text[kilo_type]

#Start
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    image = FSInputFile("images/main_banner.jpg")
    await message.answer_photo(
        photo=image,
        caption="👋 Вітаю! Це бот-меню на тиждень. Оберіть калорійність:",
        reply_markup=kilo_keyboard()
   )
    
# Callbacks
@router.callback_query(StartCallback.filter())
async def start_menu(call: types.CallbackQuery):
    image = FSInputFile("images/main_banner.jpg")
    await call.message.edit_media(
            media=InputMediaPhoto(media=image, caption="👋 Вітаю! Це бот-меню на тиждень. Оберіть калорійність:", parse_mode="HTML"),
            reply_markup=kilo_keyboard()
        )

@router.callback_query(KiloCallback.filter())
async def show_menu(call: types.CallbackQuery, callback_data: KiloCallback):
    kilo_type = KiloType(int(callback_data.kilo_type))
    await call.message.edit_caption(
        caption = f"Ви обрали {kilo_type.value} ккал. Оберіть день:",
        reply_markup=days_keyboard(kilo_type)
    )

@router.callback_query(MenuCallback.filter(F.action == "days"))
async def show_days(call: types.CallbackQuery, callback_data: MenuCallback):
    kilo_type = KiloType(int(callback_data.kilo_type)) if callback_data.kilo_type else None
    await call.message.edit_caption(
        caption="Оберіть день:",
        reply_markup=days_keyboard(kilo_type)
    )

@router.callback_query(DayCallback.filter())
async def show_meals(call: types.CallbackQuery, callback_data: DayCallback):
    day = WeekDay[callback_data.day]
    kilo_type = KiloType(int(callback_data.kilo_type))
    await call.message.edit_caption(
        caption=f"Оберіть прийом їжі для {day.value}:", 
        reply_markup=meals_keyboard(day, kilo_type)
    )

@router.callback_query(MealCallback.filter(F.action == "show"))
async def show_meal(call: types.CallbackQuery, callback_data: MealCallback, bot: Bot):
    day = WeekDay[callback_data.day]
    meal = MealType[callback_data.meal]
    variant_index = callback_data.variant_index
    kilo_type = KiloType(int(callback_data.kilo_type))
    answer_text = get_answer(day, meal, kilo_type, variant_index)
    image = FSInputFile(newWeekMenu.days[day].meals[meal].answers[variant_index].imageSrc)
    caption = f"{day.value} - {meal.value} - {kilo_type.value}ккал\n\n{answer_text}"
    await call.message.edit_media(
        media=InputMediaPhoto(media=image, caption=caption, parse_mode="HTML"),
        reply_markup=meal_nav_keyboard(day, meal, variant_index, kilo_type)
    )
    

@router.callback_query(MealCallback.filter(F.action == "next"))
async def next_meal_handler(call: types.CallbackQuery, callback_data: MealCallback):
    current_day = WeekDay[callback_data.day]
    current_meal = MealType[callback_data.meal]
    kilo_type = KiloType(int(callback_data.kilo_type))

    meal_types = list(MealType)
    current_meal_index = meal_types.index(current_meal)

    if current_meal_index < len(meal_types) - 1:
        next_meal_type = meal_types[current_meal_index + 1]
    else:
        await call.answer("Це останній прийом їжі на сьогодні.")
        return

    answer_text = get_answer(current_day, next_meal_type, kilo_type)
    image = FSInputFile(newWeekMenu.days[current_day].meals[next_meal_type].answers[0].imageSrc)
    
    caption = f"{current_day.value} - {next_meal_type.value} - {kilo_type.value}ккал\n\n{answer_text}"

    await call.message.edit_media(
        media=InputMediaPhoto(media=image, caption=caption, parse_mode="HTML"),
        reply_markup=meal_nav_keyboard(current_day, next_meal_type, 0, kilo_type)
    )
    

