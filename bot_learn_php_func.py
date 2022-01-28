# Description
# Привет!👋
# Хочешь за несколько вечеров запомнить все функции языка PHP так, чтобы они отскакивали от зубов? Чтобы в очередной раз не гуглить какую функцию применить в той или иной ситуации?
# Тогда погнали!🚀
# Нажми: /start
# 
# 
# 
# start - Начать работу с ботом🚀
# 
# 

import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Хочу посмотреть QR!", "Хочу показать свой QR!"]
#     keyboard.add(*buttons)
#     # await message.answer("Как подавать котлеты?", reply_markup=keyboard)
#     await message.answer("Привет!\nХочешь посмотреть, как выглядит <b>QR-код COVID</b> или хочешь показать <b>свой</b>?\n")



# @dp.message_handler(commands="start")
# async def welcome(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Хочу посмотреть QR!"]
#     keyboard.add(*buttons)
#     await message.answer("Привет!\nХочешь посмотреть, как выглядит <u>официальный рабочий</u> <b>QR-код COVID</b>?\n", reply_markup=keyboard)

inline_btn_1 = InlineKeyboardButton('Первый вариант!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Второй вариант!', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Третий вариант!', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('Четвертый вариант!', callback_data='button4')
inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4)
# inline_kb_full.add(inline_btn_2, inline_btn_3, inline_btn_4)

@dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == correct_answer:
        await bot.answer_callback_query(callback_query.id, text='"Это правильный ответ!😉"')
    # elif code == 5:
    #     await bot.answer_callback_query(
    #         callback_query.id,
    #         text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, text='"Неправильно...😔\nПравильный ответ: \nПовторим это позже!"')
    # await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.reply("Первая функция", reply_markup=inline_kb_full)

# @dp.message_handler(commands="start")
# async def welcome(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Хочу посмотреть QR!"]
#     keyboard.add(*buttons)
#     await message.answer("Привет!\nХочешь посмотреть, как выглядит <u>официальный рабочий</u> <b>QR-код COVID</b>?\n", reply_markup=keyboard)

# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Хочу посмотреть QR!", "Хочу показать свой QR!"]
#     keyboard.add(*buttons)
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)


# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         '''
#         # Old fashioned way:
#         await bot.send_photo(
#             message.chat.id,
#             photo,
#             caption='Cats are here 😺',
#             reply_to_message_id=message.message_id,
#         )
#         '''

#         await message.reply_photo(photo, caption='Cats are here 😺')


# @dp.message_handler()
# async def echo(message: types.Message):

#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)