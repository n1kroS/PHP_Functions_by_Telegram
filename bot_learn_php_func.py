
import token
import logging

from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token.TOKEN, parse_mode=types.ParseMode.HTML)
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



@dp.message_handler(commands="start")
async def welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Хочу посмотреть QR!"]
    keyboard.add(*buttons)
    await message.answer("Привет!\nХочешь посмотреть, как выглядит <u>официальный рабочий</u> <b>QR-код COVID</b>?\n", reply_markup=keyboard)

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


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)