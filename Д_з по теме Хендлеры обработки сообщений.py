#       Цель: написать простейшего телеграм-бота, используя асинхронные функции.
#
#       Подготовка:
#       Выполните все действия представленные в этих видео, создав и подготовив Telegram-бот
#       для дальнейших заданий:

#
#       Задача "Бот поддержки (Начало)":
#       К коду из подготовительного видео напишите две асинхронные функции:
#       start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.'.
#       Запускается только когда написана команда '/start' в чате с ботом.
#       (используйте соответствующий декоратор)

#       all_massages(message) - печатает строку в консоли 'Введите команду /start,
#       чтобы начать общение.'. Запускается при любом обращении не описанном ранее.
#       (используйте соответствующий декоратор)

#       Запустите ваш Telegram-бот и проверьте его на работоспособность.
#       Пример результата выполнения программы:
#       Ввод в чат Telegram:
#       Хэй!
#       /start
#       Вывод в консоль:
#       Updates were skipped successfully.
#       Введите команду /start, чтобы начать общение.
#       Привет! Я бот помогающий твоему здоровью.


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7338414504:AAHfVzTUw8eHataZtUYNbx8RgQIHXCd-HIc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)