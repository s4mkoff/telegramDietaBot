from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.Days import WeekDay, MealType
from models.Answer import KiloType
from menu import newWeekMenu

class MenuCallback(CallbackData, prefix="menu"):
    action: str
    kilo_type: str | None = None

class KiloCallback(CallbackData, prefix="kilo"):
    kilo_type: str

class DayCallback(CallbackData, prefix="day"):
    day: WeekDay
    kilo_type: str

class MealCallback(CallbackData, prefix="meal"):
    day: WeekDay
    meal: MealType
    action: str
    variant_index: int = 0
    kilo_type: str
    
class StartCallback(CallbackData, prefix="start"):
    action: str

def kilo_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"{kilo.value} ккал", callback_data=KiloCallback(kilo_type=str(kilo.value)).pack())]
            for kilo in KiloType
        ]
    )

def menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Меню", callback_data=MenuCallback(action="days").pack())]
        ]
    )

def days_keyboard(kilo_type: KiloType):
    inline_keyboard=[
            [InlineKeyboardButton(text=day.value, callback_data=DayCallback(day=day, kilo_type=str(kilo_type.value)).pack())]
            for day in WeekDay
        ]
    inline_keyboard.append(
            [InlineKeyboardButton(text="⬅️ До вибору кілокалорій", callback_data=StartCallback(action="start").pack())]
        )
    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )

def meals_keyboard(day: WeekDay, kilo_type: KiloType):
    keyboard = [
        [InlineKeyboardButton(text=meal.value, callback_data=MealCallback(day=day, meal=meal, action="show", kilo_type=str(kilo_type.value)).pack())]
        for meal in MealType
    ]
    keyboard.append([InlineKeyboardButton(text="⬅️ До вибору дня", callback_data=MenuCallback(action="days", kilo_type=str(kilo_type.value)).pack())])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def meal_nav_keyboard(day: WeekDay, meal: MealType, variant_index: int, kilo_type: KiloType):
    buttons = [
        InlineKeyboardButton(text="⬅️ До вибору прийому", callback_data=DayCallback(day=day, kilo_type=str(kilo_type.value)).pack())
    ]
    
    meal_obj = newWeekMenu.days[day].meals[meal]
    if len(meal_obj.answers) > 1:
        next_variant_index = (variant_index + 1) % len(meal_obj.answers)
        buttons.append(InlineKeyboardButton(text="Інший варіант", callback_data=MealCallback(day=day, meal=meal, action="show", variant_index=next_variant_index, kilo_type=str(kilo_type.value)).pack()))

    meal_types = list(MealType)
    current_meal_index = meal_types.index(meal)
    
    if current_meal_index < len(meal_types) - 1:
        buttons.append(InlineKeyboardButton(text="➡️ Далі", callback_data=MealCallback(day=day, meal=meal, action="next", kilo_type=str(kilo_type.value)).pack()))
    else:
        buttons.append(InlineKeyboardButton(text="✅ Завершити", callback_data=DayCallback(day=day, kilo_type=str(kilo_type.value)).pack()))

    return InlineKeyboardMarkup(inline_keyboard=[buttons])
