from enum import Enum
from dataclasses import dataclass
from typing import List
from models.Answer import Answer

class WeekDay(Enum):
    MONDAY = "Понеділок"
    TUESDAY = "Вівторок"
    WEDNESDAY = "Середа"
    THURSDAY = "Четвер"
    FRIDAY = "П’ятниця"
    SATURDAY = "Субота"
    SUNDAY = "Неділя"

class MealType(Enum):
    BREAKFAST = "Сніданок"
    MORNING_SNACK = "Обідній перекус"
    LUNCH = "Обід"
    EVENING_SNACK = "Вечерній перекус"
    DINNER = "Вечеря"

@dataclass
class Meal:
    mealType: MealType
    answer: Answer

@dataclass
class Day:
    dayType: WeekDay
    breakfast: Meal
    morningSnack: Meal
    lunch: Meal
    eveningSnack: Meal
    dinner: Meal

@dataclass
class Week:
    days: List[Day]
        