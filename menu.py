from models.Days import *
from models.Answer import Answer

newWeekMenu = Week(
    days={
        WeekDay.MONDAY: Day(
            dayType=WeekDay.MONDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/monday/breakfast.jpg",
                        text="🕖Сніданок  \nОмлет з тунцем, шпинатом і вівсянкою + ківі з м’ятою\nЯйце 1 шт. \nбілки яєчні  2 шт.\nтунець у власному соку 70г\nшпинат  50г\nвівсянка (дрібна) 20г\nолія оливкова  3г\nківі 80г\nм’ята свіжа 1 гілочка\nПриготування: збити яйце, білки та вівсянку. Додати шпинат. Обсмажити на 3г олії. Подати з тунцем зверху.\nКіві нарізати, додати м’яту.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/monday/morning_snack.jpg",
                        text="🕖Перекус\nЙогурт з яблуком, чіа та корицею\nЙогурт грецький 2% 150г\nЯблуко з шкіркою 100г\nНасіння чіа 5 г\nВолоський горіх 10г\nКориця — дрібка\nПриготування: яблуко нарізати кубиками, змішати з йогуртом і чіа. Посипати корицею.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/monday/lunch.jpg",
                        text="🕖Обід  \nКуряче філе з сочевицею та овочевим салатом\nІнгредієнти:\nКуряче філе в сирому виді 120г\nСочевиця варена  120г (40-45г в сухому виді)\nОгірок  1100г\nПомідор 70г\nРукола 20г\nЛимонний сік 1 ч.л.\nОлія лляна 5г\nПриготування: філе обсмажити або запекти. Сочевицю зварити. Салат із огірка, помідора, руколою заправити олією й лимонним соком.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/monday/evening_snack.jpg",
                        text="🕖Перекус\nАвокадо-тост з полуницею і насінням\nХліб цільнозерновий  40г\nАвокадо 35г\nПолуниця  80г\nНасіння гарбуза  5г\nПриготування: хліб підсмажити. Намазати авокадо. Зверху викласти полуницю і посипати насінням.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/monday/dinner.jpg",
                        text="🕖Вечеря\nГречана запіканка з яйцем, броколі й сиром\nІнгредієнти:\nГречка варена 100г (30г в сухому виді)\nБроколі 100г\nЯйце 1 шт.\nСир кисломолочний 5% або фета 40 г\nЗелень, спеції за смаком\nПриготування: перемішати всі інгредієнти, викласти у форму. Запекти при 180°C на 15–20хв.",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.TUESDAY: Day(
            dayType=WeekDay.TUESDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/tuesday/breakfast.jpg",
                        text="🕖Сніданок \nСирники з творогу без борошна + ягідна заправка\nТворог 5% 150г\nЯйце 1 шт.\nВівсяні пластівці дрібні 25г\nНасіння чіа 5г\nВолоський горіх 5г\nПолуниця свіжа 10г\nОлія кокосова 3г (для смаження)\nЙогурт грецький 50г\nПриготування: змішати творог, яйце, вівсянку, чіа. Сформувати сирнички й обсмажити на 3 г кокосової олії або запекти. Полуницю подрібнити до консистенції соусу.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/tuesday/morning_snack.jpg",
                        text="🕖Перекус\nЙогурт з яблуком і насінням\nЙогурт грецький 2% 150г\nЯблуко з шкіркою 100г\nЧорниця або лохина 50г\nКориці  дрібка\nПриготування: яблуко нарізати кубиками, додати до йогурту. Посипати насінням і корицею.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/tuesday/lunch.jpg",
                        text="🕖Обід  \nІндичка з пшоняною кашею та овочами\nФіле індички 140г\nПшоно варене 110г (40-45г в сухому виді)\nБроколі 80 г\nМорква  40г\nОлія оливкова 5г\nСпеції, зелень\nПриготування: індичку запекти або тушкувати. Пшоно відварити. Овочі припустити на пару. Подати з ложкою олії та зеленню.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/tuesday/evening_snack.jpg",
                        text="🕖Перекус\nАвокадо-тост із бананом і насінням\nХліб цільнозерновий 40г\nАвокадо 40г\nБанан 70г\nПриготування: на підсушений хліб викласти пюре з авокадо, зверху скибочки банану та насіння.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/tuesday/dinner.jpg",
                        text="🕖Вечеря\nКіноа-запіканка з яйцем, горошком і зеленню\nКіноа (варена) 80г\nЯйце 1 шт.\nЗелений горошок  80г\nСир кисломолочний 5% 40г\nЗелень, спеції\nПриготування: змішати все, викласти у форму та запекти 15–20 хв. Можна подавати як теплу страву або холодну.",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.WEDNESDAY: Day(
            dayType=WeekDay.WEDNESDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/wednesday/breakfast.jpg",
                        text="🕖Сніданок \nОмлет з сиром фета і помідорами + груша\nЯйце 2 шт.\nСир фета 50г\nПомідори черрі 70г\nОливкова олія 3г\nГруша свіжа 150г\nПриготування: збити яйця, додати нарізану фету і помідори. Обсмажити омлет на 3 г оливкової олії. Подати з нарізаною грушею.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/wednesday/morning_snack.jpg",
                        text="🕖Перекус\nГрецький йогурт з полуницею та мигдалем\nЙогурт грецький 2%  150г\nПолуниця 130г\nМигдаль 10г\nПриготування: змішати йогурт з полуницею, посипати мигдалем.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/wednesday/lunch.jpg",
                        text="🕖Обід  \nКуряче філе з відварним рисом і тушкованими овочами\nКуряче філе 140г в сирому виді\nРис відварний (коричневий або басматі) 100г (40г в сухому виді)\nМорква тушкована  80г\nЦибуля  30г\nОливкова олія 5г\nПриготування: куряче філе обсмажити або запекти. Овочі потушкувати з олією. Подати з рисом.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/wednesday/evening_snack.jpg",
                        text="🕖Перекус\nТост з авокадо та яблуком\nХліб цільнозерновий — 40 г\nАвокадо — 40 г\nЯблуко — 80 г\nПриготування: хліб підсушити, намазати авокадо, зверху викласти скибочки яблука.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/wednesday/dinner.jpg",
                        text="🕖Вечеря\nЗапечена риба з кіноа і шпинатом\nФіле білої риби (треска, хек) 130г сирої\nКіноа варена 90г (30г сухої)\nШпинат свіжа або заморожена 100г\nОливкова олія  3г\nЛимонний сік, спеції\nПриготування: рибу запекти з лимоном і спеціями. Кіноа відварити. Шпинат обсмажити з олією. Подати разом.",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.THURSDAY: Day(
            dayType=WeekDay.THURSDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/thursday/breakfast.jpg",
                        text="🕖Сніданок \nГречаний омлет з овочами і сиром\nЯйце 2 шт.\nГречка варена 80г (в сухому виді 25г-30г)\nПомідори  60г\nЦибуля зелена 10г\nСир кисломолочний 5%  50г\nОливкова олія 3г\nПриготування: збити яйця, додати гречку, нарізані помідори, цибулю та сир. Обсмажити на оливковій олії до готовності.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/thursday/morning_snack.jpg",
                        text="🕖Перекус\nЙогурт з ківі і насінням льону\nЙогурт грецький 2% 150г\nКіві 150г\nНасіння льону 5г\nПриготування: нарізати ківі і змішати з йогуртом. Посипати насінням льону.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/thursday/lunch.jpg",
                        text="🕖Обід  \nКуряче філе з овочевим рагу та кус-кусом\nКуряче філе 140г\nКус-кус 90г сухого\nКабачок 80г\nБолгарський перець — 60 г\nПомідори 60г\nОливкова олія 5г\nЧасник, зелень, спеції\nПриготування: куряче філе обсмажити або запекти. Овочі тушкувати з часником і спеціями. Кус-кус запарити на 5-10хв. (залити окропом 1:1 або 1:1,5).  Подати разом.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/thursday/evening_snack.jpg",
                        text="🕖Перекус\nТост з авокадо і ягодами\nХліб цільнозерновий 40г\nАвокадо 50г\nПолуниця  90г\nПриготування: підсмажити хліб, намазати авокадо, викласти полуницю.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/thursday/dinner.jpg",
                        text="🕖Вечеря\nЗапечена філе тріски в лимонно-часниковому соусі з овочевим салатом\nФіле тріски 120г сирої\nЛимонний сік 10мл\nЧасник 1 зубчик\nОливкова олія  5г\nОгірок 70г\nПомідори 70г\nРукола 20г\nЗелень, сіль, перець\nПриготування: філе тріски замаринувати у лимонному соку, часнику і 3г оливкової олії 15хв. Запекти в духовці 15-20хв. Овочі нарізати, змішати з руколою і заправити залишками олії та спеціями.\nКіноа запарене 60г (ухого 20г)",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.FRIDAY: Day(
            dayType=WeekDay.FRIDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/friday/breakfast.jpg",
                        text="🕖Сніданок \nОмлет із сиром фета і шпинатом + груша\nЯйце 2 шт.\nСир фета  40г\nШпинат  50г\nОливкова олія  г\nГруша 100г\nПриготування: збити яйця, додати нарізаний шпинат і сир фета. Обсмажити омлет на оливковій олії. Подати з нарізаною грушею.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/friday/morning_snack.jpg",
                        text="🕖Перекус\nЙогурт грецький з полуницею та насінням льону\nЙогурт грецький 2% 150мл\nПолуниця 150г\nНасіння льону  5г\nПриготування: змішати йогурт із полуницею, посипати насінням льону.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/friday/lunch.jpg",
                        text="🕖Обід  \nІндичка, запечена з овочами + кус-кус\nФіле індички 140г в сирому виді\nКус-кус 100г в сухому виді\nКабачок  80г\nБолгарський перець 60г\nЦибуля 40г\nОливкова олія 5г\nСпеції, зелень\nПриготування: овочі та індичку нарізати, змішати зі спеціями і олією. Запекти в духовці 25-30хв. при 180 °C. Кус-кус залити окропом, накрити, дати настоятися 5 хв. Подати разом.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/friday/evening_snack.jpg",
                        text="🕖Перекус\nТост із сиром фета і помідорами\nХліб цільнозерновий 40г\nСир фета 40г\nПомідор 50г\nФінік 1шт.\nПриготування: підсмажити хліб, викласти сир фета і скибочки помідора.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/friday/dinner.jpg",
                        text="🕖Вечеря\nБулгур варений 60г (20г сухого)\nОвочеві «човники» з фаршем індички та сиром фета\nКабачок або патисон 150г\nФарш індички 120г\nСир фета  30г\nПомідор 50г\nЦибуля 30г\nОливкова олія  3г\nЧасник, зелень, спеції\nПриготування: кабачок розрізати вздовж, видалити середину. Фарш обсмажити з цибулею та часником. Змішати з нарізаним помідором і сиром фета. Наповнити «човники» фаршем. Запекти 20хв. при 180 °C.",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.SATURDAY: Day(
            dayType=WeekDay.SATURDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/saturday/breakfast.jpg",
                        text="🕖Сніданок \nЯєчня з овочами та сиром рікота + яблуко\nЯйце 2 шт.\nСир рікота 50г\nБолгарський перець 60г\nЦибуля зелена 10г\nОливкова олія  г\nЯблуко 100г\nПриготування: обсмажити нарізані овочі на оливковій олії, додати збиті яйця і рікоту, готувати під кришкою до готовності. Подати з яблуком.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/saturday/morning_snack.jpg",
                        text="🕖Перекус\nКефір 1,6-2% + груша + насіння соняшника\nКефір 150 мл\nГруша — 100 г\nНасіння соняшника — 12 г\nПриготування: просто з’їсти разом. Насіння можна додати до кефіру або з’їсти окремо.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/saturday/lunch.jpg",
                        text="🕖Обід  \nЗапечена курка з бататом та спаржею\nКуряче філе 160г в сирому виді\nБатат запечений 130г\nСпаржа 80г\nОливкова олія 5г\nСпеції\nПриготування: курку та батат замаринувати зі спеціями, запекти. Спаржу відварити або запекти. Подати з оливковою олією.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/saturday/evening_snack.jpg",
                        text="🕖Перекус\nТост з сиром рікота і свіжими ягодами\nХліб цільнозерновий 50г\nСир рікота 40г\nЯгоди (полуниця, чорниця) 80г\nПриготування: підсмажити хліб, намазати рікотою, викласти ягоди зверху.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/saturday/dinner.jpg",
                        text="🕖Вечеря\nЗапіканка з куркою, броколі і грибами\nКуряче філе 150г в сирому виді\nБроколі 100г\nШампіньйони 80г\nЯйце 1 шт.\nСир твердий (низької жирності 15-30%) 30г\nОливкова олія 3г\nСпеції\nПриготування: обсмажити гриби з олією, додати варену курку і броколі. Збити яйце з сиром і залити суміш у форму. Запекти 20-25хв. при 180 °C.",
                        buttons=[]
                    )
                )
            }
        ),
        WeekDay.SUNDAY: Day(
            dayType=WeekDay.SUNDAY,
            meals={
                MealType.BREAKFAST: Meal(
                    mealType=MealType.BREAKFAST,
                    answer=Answer(
                        imageSrc="images/sunday/breakfast.jpg",
                        text="🕖Сніданок \nОмлет із шпинатом і сиром моцарела + ківі\nЯйце 2 шт.\nШпинат 50г\nСир моцарела 26% 40г\nОливкова олія 3г\nКіві 100г\nПриготування: обсмажити шпинат на оливковій олії, додати збиті яйця і сир моцарела, готувати під кришкою до готовності. Подати з ківі.",
                        buttons=[]
                    )
                ),
                MealType.MORNING_SNACK: Meal(
                    mealType=MealType.MORNING_SNACK,
                    answer=Answer(
                        imageSrc="images/sunday/morning_snack.jpg",
                        text="🕖Перекус\nКефір  із яблуком і насінням гарбуза\nКефір 1,6%-2% 150мл\nЯблуко 100г\nНасіння гарбуза 10г\nПриготування: просто з’їсти разом, насіння можна додати до кефіру.",
                        buttons=[]
                    )
                ),
                MealType.LUNCH: Meal(
                    mealType=MealType.LUNCH,
                    answer=Answer(
                        imageSrc="images/sunday/lunch.jpg",
                        text="🕖Обід  \nІндичка, тушкована з броколі та морквою + кус-кус\nФіле індички 160г в сирому виді\nБроколі 100г\nМорква  80г\nКус-кус 100г в сухому виді\nОливкова олія 5г\nСпеції\nПриготування: індичку тушкувати з овочами на оливковій олії зі спеціями. Кус-кус запарити окропом. Подати разом.",
                        buttons=[]
                    )
                ),
                MealType.EVENING_SNACK: Meal(
                    mealType=MealType.EVENING_SNACK,
                    answer=Answer(
                        imageSrc="images/sunday/evening_snack.jpg",
                        text="🕖Перекус\nТост із сиром фета і свіжими огірками\nХліб цільнозерновий  50г\nСир фета 50г\nОгірок свіжий 70г\nПриготування: підсмажити хліб, викласти сир фета і скибочки огірка.",
                        buttons=[]
                    )
                ),
                MealType.DINNER: Meal(
                    mealType=MealType.DINNER,
                    answer=Answer(
                        imageSrc="images/sunday/dinner.jpg",
                        text="🕖Вечеря\nЗапечена риба (тріска або судак) з овочевим рагу\nФіле риби (тріска, судак) 120г в сирому виді\nКабачок 80г\nПомідори 60г\nЦибуля 40г\nОливкова олія 3 г\nЧасник, спеції\nПриготування: овочі нарізати, тушкувати або запекти з рибою в духовці 20-25 хв. Заправити оливковою олією.",
                        buttons=[]
                    )
                )
            }
        )
    }
)
