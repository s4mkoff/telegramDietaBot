from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.Days import WeekDay, MealType

class MenuCallback(CallbackData, prefix="menu"):
    action: str

class DayCallback(CallbackData, prefix="day"):
    day: WeekDay

class MealCallback(CallbackData, prefix="meal"):
    day: WeekDay
    meal: MealType
    action: str

def menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Меню", callback_data=MenuCallback(action="days").pack())]
        ]
    )

def days_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=day.value, callback_data=DayCallback(day=day).pack())]
            for day in WeekDay
        ]
    )

def meals_keyboard(day: WeekDay):
    keyboard = [
        [InlineKeyboardButton(text=meal.value, callback_data=MealCallback(day=day, meal=meal, action="show").pack())]
        for meal in MealType
    ]
    keyboard.append([InlineKeyboardButton(text="⬅️ До вибору дня", callback_data=MenuCallback(action="days").pack())])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def meal_nav_keyboard(day: WeekDay, meal: MealType):
    buttons = [
        InlineKeyboardButton(text="⬅️ До вибору прийому", callback_data=DayCallback(day=day).pack())
    ]
    
    meal_types = list(MealType)
    current_meal_index = meal_types.index(meal)
    
    if current_meal_index < len(meal_types) - 1:
        buttons.append(InlineKeyboardButton(text="➡️ Далі", callback_data=MealCallback(day=day, meal=meal, action="next").pack()))
    else:
        buttons.append(InlineKeyboardButton(text="✅ Завершити", callback_data=DayCallback(day=day).pack()))

    return InlineKeyboardMarkup(inline_keyboard=[buttons])
