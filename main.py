from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards
import sqlite3

language = ['Українська', 'Русский', 'English']
digits = '0123456789 +-'

bot = Bot(token='')
dp = Dispatcher(bot)

meeting_date = ["day", "start", "end"]
meeting_registration = False
low_hour = 0


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
        meeting_date[0] = message.text
        await bot.send_message(message.chat.id, f'Клас, {message.text}!'
                                                f'\nЗ котрої години ви могли б підїхати до нас?',
                               reply_markup=keyboards.markup_3)
    else:
        pass


@dp.message_handler(Text(keyboards.buttons_3))
async def get_meeting_end(message: types.Message):
    if meeting_registration:
        if message.text == keyboards.buttons_3[-1]:
            await bot.send_message(message.chat.id, f'У який день Ви хотіли б прийти до нас?',
                                   reply_markup=keyboards.markup_2)
        else:
            global low_hour
            low_hour = int(message.text[2:4])
            meeting_date[1] = message.text
            await bot.send_message(message.chat.id, f'Супер, {message.text}.\nДо котрої години маєте час?',
                                   reply_markup=keyboards.markup_4)
    else:
        pass


@dp.message_handler(Text(keyboards.buttons_4))
async def get_meeting_accept(message: types.Message):
    if meeting_registration:
        if message.text == keyboards.buttons_4[-1]:
            await bot.send_message(message.chat.id, f'З котрої години ви могли б підїхати до нас?',
                                   reply_markup=keyboards.markup_3)
        else:
            if int(meeting_date[1][2:4]) > int(message.text[3:5]):
                await bot.send_message(message.chat.id, f'Хмм, спочатку вкажіть час початку, потім закінчення, а не навпаки.',
                                       reply_markup=keyboards.markup_3)
            else:
                meeting_date[2] = message.text
                await bot.send_message(message.chat.id, f'Ви бажаєте зустрітись у {meeting_date[0]}, {meeting_date[1]} {meeting_date[2]}?',
                                       reply_markup=keyboards.markup_5)
    else:
        pass


@dp.message_handler(Text(keyboards.buttons_5))
async def get_number(message: types.Message):
    global meeting_registration
    if meeting_registration:
        if message.text == keyboards.buttons_5[0]:
            global decision
            decision = True
            await bot.send_message(message.chat.id, f'🤗 Ура! Вийшло!'
                                                    f'Ми отримали Вашу заявку на зустріч.\n'
                                                    f'Підтверждення зустрічі виконає менеджер, який зателефонує Вам'
                                                    f', щойно матиме нагоду.\n'
                                                    f'Будь-ласка, залиште свій контактний номер телефону, для зв’язку '
                                                    f'з менеджером.', reply_markup=keyboards.markup_6)
        elif message.text == keyboards.buttons_5[1]:
            await bot.send_message(message.chat.id, f'Добре, тоді спробуйте ще раз, або оберіть інший пункт меню.',
                                   reply_markup=keyboards.markup_1)
            meeting_registration = False


@dp.message_handler(content_types=['contact'])
async def get_number(message: types.Message):
    global meeting_registration
    if meeting_registration:
        await bot.send_message(message.chat.id, f'Дякуємо, {message.chat.first_name}.\n'
                                                f'Наш менеджер зв’яжеться з Вами за номером телефону:\n'
                                                f'{message.contact.phone_number}')
        await bot.send_message(message.chat.id, f'Якщо Вас цікавить щось ще - оберіть необхідний пункт меню.',
                               reply_markup=keyboards.markup_1)
        meeting_registration = False
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp)
