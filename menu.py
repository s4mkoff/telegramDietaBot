from models.Days import *
from models.Answer import Answer, KiloType

newWeekMenu = Week(
    days={
        WeekDay.MONDAY: Day(
            dayType=WeekDay.MONDAY,
            meals={
                
            }
        )
    }
)

# MealType.BREAKFAST: Meal(
#                     mealType=MealType.BREAKFAST,
#                     answers=[
#                         Answer(
#                             imageSrc="image/monday/breakfast.jpg",
#                             text={
#                                 KiloType.K_1300: "Breakfast for 1300 kcal",
#                                 KiloType.K_1500: "Breakfast for 1500 kcal",
#                                 KiloType.K_1700: "Breakfast for 1700 kcal"
#                             }
#                         ),
#                         Answer(
#                             imageSrc="image/monday/breakfast_variant.jpg",
#                             text={
#                                 KiloType.K_1300: "Another breakfast for 1300 kcal",
#                                 KiloType.K_1500: "Another breakfast for 1500 kcal",
#                                 KiloType.K_1700: "Another breakfast for 1700 kcal"
#                             }
#                         )
#                     ]
#                 ),


# MealType.BREAKFAST: Meal(
#                     mealType=MealType.BREAKFAST,
#                     answers=[
#                         Answer(
#                             imageSrc="image/monday/breakfast.jpg",
#                             text={
#                                 KiloType.K_1300: "Breakfast for 1300 kcal",
#                                 KiloType.K_1500: "Breakfast for 1500 kcal",
#                                 KiloType.K_1700: "Breakfast for 1700 kcal"
#                             }
#                         )
#                     ]
#                 )