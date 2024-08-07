
'''         Цель: написать простейшие CRUD функции для взаимодействия с базой данных.
'''


#       Задача "Регистрация покупателей":
#           Подготовка:
#       Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его,
#       следуя пунктам задачи ниже.
#
#       Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
#           initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
#           Эта таблица должна содержать следующие поля:
#               1. id - целое число, первичный ключ
#               2. username - текст (не пустой)
#               3. email - текст (не пустой)
#               4. age - целое число (не пустой)
#               5. balance - целое число (не пустой)

#       add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
#       Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
#       Баланс у новых пользователей всегда равен 1000. Для добавления записей в
#       таблице используйте SQL запрос.

#       is_included(username) принимает имя пользователя и возвращает True, если такой пользователь
#       есть в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.
#
#       Изменения в Telegram-бот:
#       Кнопки главного меню дополните кнопкой "Регистрация".
#       Напишите новый класс состояний RegistrationState с следующими объектами класса
#       State: username, email, age, balance(по умолчанию 1000).
#       Создайте цепочку изменений состояний RegistrationState.
#       Фукнции цепочки состояний RegistrationState:

#       sing_up(message):
#       Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
#       Эта функция должна выводить в Telegram-бот сообщение
#       "Введите имя пользователя (только латинский алфавит):".
#       После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
#       set_username(message, state):
#       Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
#       Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя
#       (только латинский алфавит):".
#       Если пользователя message.text ещё нет в таблице, то должны обновляться данные в
#       состоянии username на message.text. Далее выводится сообщение "Введите свой email:"
#       и принимается новое состояние RegistrationState.email.
#       Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует,
#       введите другое имя" и запрашивать новое состояние для RegistrationState.username.

#       set_email(message, state):
#       Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
#       Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
#       Далее выводить сообщение "Введите свой возраст:":
#       После ожидать ввода возраста в атрибут RegistrationState.age.

#       set_age(message, state):
#       Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
#       Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
#       Далее брать все данные (username, email и age) из состояния и записывать в таблицу
#       Users при помощи ранее написанной crud-функции add_user.
#       В конце завершать приём состояний при помощи метода finish().

#       Перед запуском бота пополните вашу таблицу Products 4 или более записями для
#       последующего вывода в чате Telegram-бота.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import sqlite3
import time
from crud_functions import *

api = "7338414504:AAF_qkRMXWLwCI-9JehERGoyo3wLRg-VSYk"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
items = get_all_products()

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить'),
         KeyboardButton(text='Регистрация')]
    ], resize_keyboard=True
)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Рассчитать норму калорий ', callback_data='calories'),
         InlineKeyboardButton('Формулы расчёта', callback_data='formulas')]
    ]
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Продукт 1',
                              callback_data="product_buying"),
         InlineKeyboardButton('Продукт 2',
                              callback_data="product_buying"),
         InlineKeyboardButton('Продукт 3',
                              callback_data="product_buying"),
         InlineKeyboardButton('Продукт 4',
                              callback_data="product_buying")]
    ]
)


class UserState(StatesGroup):
    weight = State()
    growth = State()
    age = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()



@dp.message_handler(commands=['start'])
async def start(message):
    with open('images/logo.jpg', "rb") as img:
        await message.answer_photo(img, f'Уважаемый(ая) {message.from_user.username}, '
                                        f'добро пожаловать в магазин Витамины для всех!', reply_markup=start_menu)


@dp.message_handler(text='Рассчитать')
async def get_calories(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.message_handler(text='Информация')
async def get_info(message):
    with open('images/intro.png', "rb") as img:
        await message.answer_photo(img,
                                   'онлайн-магазин по продаже нутрицевтиков и натуральных экологичных '
                                   'товаров для здоровья, молодости и красоты.'
                                   )


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for item in items:
        await message.answer(f'Название: {item[1]} | Описание: {item[2]} | Цена: {item[3]}')
        with open(f'images/{item[0]}.png', "rb") as prod1:
            await message.answer_photo(prod1)
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


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


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age_reg(message, state):
    await state.update_data(age=message.text)
    users_data = await state.get_data()
    add_user(username=users_data["username"], email=users_data["email"], age=int(users_data["age"]))
    await state.finish()
    await message.answer("Регистрация прошла успешно")
    time.sleep(1)
    with open('images/intro.png', "rb") as img:
        await message.answer_photo(img, f'Уважаемый(ая) {message.from_user.username}, '
                                        f'добро пожаловать в магазин Витамины для всех!', reply_markup=start_menu)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
