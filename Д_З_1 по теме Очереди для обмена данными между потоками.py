# Цель задания:
#
# Освоить механизмы создания потоков и очередей для обмена данных между ними в Python.
# Практически применить знания, создав и запустив несколько потоков и очередь.

# Задание:
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
# прибывающих для заказа пищи и уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду,
# занимают столик, употребляют еду и уходят. Если столик свободен, новый посетитель
# принимается к обслуживанию, иначе он становится в очередь на ожидание.

# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты:
# number(int) - номер стола, is_busy(bool) - занят стол или нет.

# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
# Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя
# (запуск потока), в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)

# Пример работы:


# Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.

import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Customer(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.holding_time = 2
        self.tables_id = 0

    def run(self):
        time.sleep(self.holding_time)


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()
        self.queue_arrival = Queue()
        self.table = None
        self.current_customer = 0

    def free_table(self):
        """Проверка свободного стола, возвращает индекс свободного стола
        или None если все столики заняты"""
        for free_id in range(len(self.tables)):
            if self.tables[free_id].is_busy:
                return free_id
        else:
            return None

    def start_customer(self, customer):
        with lock:
            print(f"\033[3m\033[34m Посетитель номер {customer.number} "
                  f"сел за стол {self.tables[customer.tables_id].number}. (начало обслуживания)\033[0m")
            self.tables[customer.tables_id].is_busy = False

    def finish_customer(self, customer):
        with lock:
            customer.start()
            print(f"\033[33mПосетитель номер {customer.number} начал кушать (в процессе обслуживания)\033[0m")
            customer.join()
            print(f"\033[96m Посетитель номер {customer.number} покушал и ушёл. (конец обслуживания)\033[0m")
            self.tables[customer.tables_id].is_busy = True
            print(f"\033[3m\033[31m Стол № {self.tables[customer.tables_id].number} свободен\033[0m")

    def customer_arrival(self):

        for numbers in range(1, 21):
            customer = Customer(numbers)
            print(f"\033[92m Посетитель номер {customer.number} прибыл.\033[0m")
            self.queue.put(customer)
            time.sleep(1)

    def serve_customer(self):
        time.sleep(1)
        while not self.queue.empty():  # цикл пока очередь не пуста
            self.table = self.free_table()
            if self.table is not None:
                self.current_customer = self.queue.get()
                self.current_customer.tables_id = self.table
                self.start_customer(self.current_customer)
                self.queue_arrival.put(self.current_customer)
                time.sleep(2)
            if self.table is None:
                self.current_customer = self.queue_arrival.get()
                self.finish_customer(self.current_customer)
        while not self.queue_arrival.empty():  # до последнего клиента
            self.current_customer = self.queue_arrival.get()
            self.finish_customer(self.current_customer)
        print()
        print('\033[3m\033[35m' + 'Все посетители обслужены!'+"\033[0m")


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)
lock = threading.Lock()
# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Запускаем поток для обслуживания посетителей
serve_arrival_thread = threading.Thread(target=cafe.serve_customer)
serve_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# Ожидаем завершения работы обслуживания посетителей
serve_arrival_thread.join()
