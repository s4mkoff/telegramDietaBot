from models.Days import *
from models.Answer import MenuButton

newWeekMenu = Week(
    days=[
        Day(
            dayType=WeekDay.MONDAY,
            breakfast=Meal(
                mealType=MealType.BREAKFAST,
                answer=Answer(
                    imageSrc="images/monday/breakfast.jpg",
                    text="🕖 Сніданок\nОмлет з тунцем, шпинатом і вівсянкою + ківі з м’ятою\nЯйце 1 шт.\nБілки яєчні 2 шт.\nТунець у власному соку 70г\nШпинат 50г\nВівсянка (дрібна) 20г\nОлія оливкова 3г\nКіві 80г\nМ’ята свіжа 1 гілочка\nПриготування: збити яйце, білки та вівсянку. Додати шпинат. Обсмажити на 3г олії. Подати з тунцем зверху.\nКіві нарізати, додати м’яту.",
                    buttons=[ 
                        MenuButton(text="Назад", callback="back_to_menu"),
                        MenuButton(text="Далі", callback="next_meal") 
                    ]
                )
            ),
            morningSnack=Meal(
                mealType=MealType.MORNING_SNACK,
                answer=Answer(
                    imageSrc="images/monday/morning_snack.jpg",
                    text="🕖 Перекус\nЙогурт з яблуком, чіа та корицею\nЙогурт грецький 2% 150г\nЯблуко з шкіркою 100г\nНасіння чіа 5г\nВолоський горіх 10г\nКориця — дрібка\nПриготування: яблуко нарізати кубиками, змішати з йогуртом і чіа. Посипати корицею.",
                    buttons=[ 
                        MenuButton(text="Назад", callback="back_to_menu"),
                        MenuButton(text="Далі", callback="next_meal") 
                    ]
                )
            ),
            lunch=Meal(
                mealType=MealType.LUNCH,
                answer=Answer(
                    imageSrc="images/monday/lunch.jpg",
                    text="🕖 Обід\nКуряче філе з сочевицею та овочевим салатом\nКуряче філе в сирому виді 120г\nСочевиця варена 120г (40-45г в сухому виді)\nОгірок 110г\nПомідор 70г\nРукола 20г\nЛимонний сік 1 ч.л.\nОлія лляна 5г\nПриготування: філе обсмажити або запекти. Сочевицю зварити. Салат із огірка, помідора, руколою заправити олією й лимонним соком.",
                    buttons=[ 
                        MenuButton(text="Назад", callback="back_to_menu"),
                        MenuButton(text="Далі", callback="next_meal") 
                    ]
                )
            ),
            eveningSnack=Meal(
                mealType=MealType.EVENING_SNACK,
                answer=Answer(
                    imageSrc="images/monday/evening_snack.jpg",
                    text="🕖 Перекус\nАвокадо-тост з полуницею і насінням\nХліб цільнозерновий 40г\nАвокадо 35г\nПолуниця 80г\nНасіння гарбуза 5г\nПриготування: хліб підсмажити. Намазати авокадо. Зверху викласти полуницю і посипати насінням.",
                    buttons=[ 
                        MenuButton(text="Назад", callback="back_to_menu"),
                        MenuButton(text="Далі", callback="next_meal") 
                    ]
                )
            ),
            dinner=Meal(
                mealType=MealType.DINNER,
                answer=Answer(
                    imageSrc="images/monday/dinner.jpg",
                    text="🕖 Вечеря\nГречана запіканка з яйцем, броколі й сиром\nГречка варена 100г (30г в сухому виді)\nБроколі 100г\nЯйце 1 шт.\nСир кисломолочний 5% або фета 40г\nЗелень, спеції за смаком\nПриготування: перемішати всі інгредієнти, викласти у форму. Запекти при 180°C на 15–20хв.",
                    buttons=[ 
                        MenuButton(text="Назад", callback="back_to_menu"),
                        MenuButton(text="Далі", callback="next_meal") 
                    ]
                )
            ),
        ),
    ]
)