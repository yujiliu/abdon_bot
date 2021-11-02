from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# START MENU
buttons_1 = ["👥Хочу потрапити до вас на зустріч", "🏷️Мені потрібен прорахунок меблів", "✨Щось інше..."]

markup_1 = ReplyKeyboardMarkup(resize_keyboard=True)
for button in buttons_1:
    markup_1.add(KeyboardButton(button))

# MEETING MENU
# choose day
buttons_2 = ["Понеділок", "Вівторок", "Середа", "Четвер", "П’ятниця", "Субота"]
markup_2 = ReplyKeyboardMarkup(resize_keyboard=True)
for button in buttons_2:
    markup_2.add(KeyboardButton(button))

# choose low hour
buttons_3 = ["з " + str(x) + ":00" for x in range(10, 20)]
buttons_3.append("Змінити день?")
markup_3 = ReplyKeyboardMarkup(resize_keyboard=True)
for button in buttons_3:
    markup_3.add(KeyboardButton(button))

# choose up hour
buttons_4 = ["до " + str(x) + ":00" for x in range(10, 21)]
buttons_4.append("Змінити час початку?")
markup_4 = ReplyKeyboardMarkup(resize_keyboard=True)
for button in buttons_4:
    markup_4.add(KeyboardButton(button))

# confirm meeting
buttons_5 = ["Так", "Ні"]
markup_5 = ReplyKeyboardMarkup(resize_keyboard=True)
for button in buttons_5:
    markup_5.add(KeyboardButton(button))

# give contact
buttons_6 = "Дозволити доступ до номеру телефону"
markup_6 = ReplyKeyboardMarkup(resize_keyboard=True)
markup_6.add(KeyboardButton(buttons_6, request_contact=True))