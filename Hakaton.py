from email import message
from turtle import setx
from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from requests import request   



TOKEN = "5796328526:AAHwcp2XzN1oJ-G-05RwoughoBZ3PJAbJno"
storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)

def kb1() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('HR','PR','Команда разработчкиков'))
    return kb


def kb2() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Женский','Мужской'))
    return kb


def kb3()-> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('IT','Путешествия','Спорт','Музыка'))
    return kb

class QuestionnaireStatesGroup(StatesGroup):
    department = State()
    sex = State()
    age = State()
    hobbies = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await message.answer(f'Привет, {message.chat.first_name} {message.chat.last_name}! Для начала нужно заполнить анкету, для этого нажми /create')


@dp.message_handler(commands=['create'])
async def create_command(message: types.Message) -> None:
    await message.answer('Давай же начнем! Для начала выбери свой отдел')
    await QuestionnaireStatesGroup.department.set()

@dp.message_handler(content_types=['text'], state=QuestionnaireStatesGroup.department)
async def load_department(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['department'] = message.text

    await message.answer('Теперь укажи свой пол')
    await QuestionnaireStatesGroup.next()

@dp.message_handler(state=QuestionnaireStatesGroup.sex)
async def load_sex(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['sex'] = message.text

    await message.answer('Сколько тебе лет?')
    await QuestionnaireStatesGroup.next()

@dp.message_handler(state=QuestionnaireStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text

    await message.answer('Теперь укажи своё хобби')
    await QuestionnaireStatesGroup.next()

@dp.message_handler(state=QuestionnaireStatesGroup.hobbies)
async def load_hobbies(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['hobbies'] = message.text
        await bot.send_message(chat_id=message.from_user.id, text=f"{data['department']},{data['sex']},{data['age']},{data['hobbies']}")

    await message.answer('Ваша анкета успешно создана!)')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
 


 

