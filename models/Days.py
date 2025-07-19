from enum import Enum
from dataclasses import dataclass
from typing import Dict
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
    answers: list[Answer]

@dataclass
class Day:
    dayType: WeekDay
    meals: Dict[MealType, Meal]

@dataclass
class Week:
    days: Dict[WeekDay, Day]
        