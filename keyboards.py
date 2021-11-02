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
