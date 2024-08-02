'''     Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.
'''

#   Задача "Ещё больше выбора":
#       Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать'
#       присылалась Inline-клавиатруа.

#       Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:

#           1. С текстом 'Рассчитать норму калорий' и callback_data='calories'
#           2. С текстом 'Формулы расчёта' и callback_data='formulas'

#       Создайте новую функцию main_menu(message), которая:
#
#           1. Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
#           2. Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
#
#       Создайте новую функцию get_formulas(call), которая:
#
#           1. Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
#           2. Будет присылать сообщение с формулой Миффлина-Сан Жеора.
#
#       Измените функцию set_age и декоратор для неё:

#           1. Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
#           2. Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
#
#        По итогу получится следующий алгоритм:
#
#           1. Вводится команда /start
#           2. На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
#           3. В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
#           4. По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
#           5. По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7338414504:AAF_qkRMXWLwCI-9JehERGoyo3wLRg-VSYk"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
bottom = KeyboardButton(text='Рассчитать')
bottom2 = KeyboardButton(text='Информация')
kb.row(bottom, bottom2)
inline_kb = InlineKeyboardMarkup()
inline_bottom1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_bottom2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_kb.row(inline_bottom1, inline_bottom2)


class UserState(StatesGroup):
    weight = State()
    growth = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = (10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"])) + 5
    await message.answer(f"Калорий для оптимального похудения {calories}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
