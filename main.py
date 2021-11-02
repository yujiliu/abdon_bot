from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards

language = ['Українська', 'Русский', 'English']

bot = Bot(token='2025283165:AAGh1D_nL0D3IuxWsa3zAb56Y9zr7rpvtaQ')
dp = Dispatcher(bot)

meeting_date = []
meeting_registration = False


@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    await bot.send_message(message.chat.id, f'Доброго дня, {message.from_user.first_name}!\nЩо Вас цікавить?',
                           reply_markup=keyboards.markup_1)


@dp.message_handler(Text(equals='👥Хочу потрапити до вас на зустріч'))
async def meeting_process(message: types.Message):
    global meeting_registration
    meeting_registration = True
    await bot.send_message(message.chat.id, f'Потрапити до нас у салон можна за попередньою домовленістю.\n'
                                            f'Усі зустрічі необхідно спланувати хоча б за один день до візиту.\n'
                                            f'Скажіть будь-ласка, у який день Ви хотіли б прийти до нас?',
                           reply_markup=keyboards.markup_2)


@dp.message_handler(Text(keyboards.buttons_2))
async def get_meeting_start(message: types.Message):
    if meeting_registration:
        await bot.send_message(message.chat.id, f'Клас, {message.text}!'
                                                f'\nЗ котрої години ви могли б підїхати до нас?',
                               reply_markup=keyboards.markup_3)
    else:
        pass


@dp.message_handler(Text(keyboards.buttons_3))
async def get_meeting_end(message: types.Message):
    if meeting_registration:
        if message.text == "Змінити день?":
            await bot.send_message(message.chat.id, f'У який день Ви хотіли б прийти до нас?',
                                   reply_markup=keyboards.markup_2)
        else:
            await bot.send_message(message.chat.id, f'Супер, {message.text}.')
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp)
