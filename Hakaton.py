from cgitb import handler
from codecs import BOM_UTF16
from unicodedata import name
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message,\
    InlineKeyboardButton, InlineKeyboardMarkup
TOKEN = '5648532002:AAEfiIK-CuDJU76VdJ7ToKH0wzTcVhYCQd8'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - описание бота"""
DESCRIPTION  = """Этот бот сделан Командой "Yellow Bogdan".
Наше детище поможет тебе найти единомышленников в твоей сфере деятельности. Достаточно просто написать команду "/start"!"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton(text = 'Выбор отдела')
    keyboard1.add(bt1)
    await message.answer(text=f'Привет, {message.chat.first_name} {message.chat.last_name}! Для начала нужно заполнить анкету', reply_markup = keyboard1)
    await message.delete()

@dp.message_handler(Text(equals="Выбор отдела"))
async def areplynswer_bt1(message: types.Message):
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt2 = types.KeyboardButton(text = 'HR')
    bt3 = types.KeyboardButton(text = 'Анкета')
    bt4 = types.KeyboardButton(text = 'Команда разработчиков')
    keyboard2.add(bt2).add(bt3).add(bt4)
    await message.answer(f"Я Вас понял, {message.chat.first_name}. Выберите, пожалуйста, ваш отдел", reply_markup = keyboard2)

@dp.message_handler(Text(equals='Анкета'))
async def questionnaire1(message: types.Message):
    keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt4 = types.KeyboardButton(text = 'MAN')
    bt5 = types.KeyboardButton(text = 'GIRL')
    keyboard3.add(bt4).add(bt5)
    await message.answer('Какой у вас пол?', reply_markup=keyboard3)

@dp.message_handler(Text(equals='MAN'or'GIRL'))
async def questionnaire2(message: types.Message):
    keyboard4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    bt6 = types.KeyboardButton(text = 'Спорт')
    bt7 = types.KeyboardButton(text = 'Шоппинг')
    bt8 = types.KeyboardButton(text = 'Еда')
    bt9 = types.KeyboardButton(text = 'IT')
    keyboard4.add(bt6).add(bt7).add(bt8).add(bt9)
    await message.answer('Чем вы любите увлекаться в свободное время?', reply_markup= keyboard4)

    



    



if __name__ == '__main__':
    executor.start_polling(dp)
 
