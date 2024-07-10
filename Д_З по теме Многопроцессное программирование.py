# -*- coding: utf-8 -*-
# Цель задания:
#
# Освоить механизмы создания процессов в Python.
# Практически применить знания, создав несколько параллельных процессов и запустив их.


# Задание:
# Моделирование программы для управления данными о движении товаров на складе и эффективной
# обработки запросов на обновление информации в многопользовательской среде.
#
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на
# обновление информации о поступлении товаров и отгрузке товаров.
# Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти
# запросы в многопользовательской среде, с использованием механизма мультипроцессорности для
# обеспечения быстрой реакции на поступающие данные.
#
# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить
# значение ключа, если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
#
# 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает
# его(start) и замораживает(join).

# # Выводим обновленные данные о складских запасах
# print(manager.data)
#
# Вывод на консоль:
# {"product1": 70, "product2": 100, "product3": 200}

import multiprocessing
from multiprocessing import Process, Queue

requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]


class WarehouseManager:
    def __init__(self):
        self.data = {}


    def process_request(self, request, shared_dict, lock):
        lock.acquire()
        try:
            product_name, action, quantity = request
            if action == "receipt":
                if product_name in shared_dict:
                    shared_dict[product_name] += quantity
                else:
                    shared_dict[product_name] = quantity
            elif action == "shipment":
                if product_name in shared_dict and shared_dict[product_name] >= quantity:
                    shared_dict[product_name] -= quantity
                else:
                    print("нет нужного количества товара")
        finally:
            lock.release()


    def run(self, requests):
        shared_dict= multiprocessing.Manager().dict()
        lock = multiprocessing.Lock()
        processes = [multiprocessing.Process(target=self.process_request, args=(i, shared_dict, lock))
                     for i in requests]
        for p in processes:
            p.start()

        for p in processes:
            p.join()

        self.data = shared_dict



if __name__ == '__main__':
    # создаем менеджера склада
    manager = WarehouseManager()
    # запускаем обработку запросов
    manager.run(requests)
    # выводим обновленные данные о складских запасах
    print(manager.data)
