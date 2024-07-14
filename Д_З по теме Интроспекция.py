# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
# проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль,
# и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о
# переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
from pprint import pprint


class PaginationHelper:
    """ Класс предназначен для получения массива значений и целого числа,
        указывающего, сколько элементов будет разрешено на каждой странице.
        Типы значений, содержащихся в коллекции/массиве, не имеют значения."""

    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        """# возвращает количество элементов во всей коллекции"""
        return self._item_count

    def page_count(self):
        """ # returns количество страниц"""
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        """# возвращает количество элементов на данной странице.
        page_index отсчитывается от нуля
        # этот метод должен возвращать -1 для page_index значений,
         находящихся вне диапазона"""
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        """# определяет, на какой странице находится элемент в данном индексе.
        Индексы, отсчитываемые от нуля.
        # этот метод должен возвращать -1 для item_index значений,
        находящихся вне диапазона"""
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'f', 'g'], 4)

helper.page_count()
helper.item_count()
print(helper.page_item_count(0))  # должен = = 4


# print(helper.page_item_count(1))  # последняя страница - должно = = 2
# print(helper.page_item_count(2))  # должен = = -1, так как страница недопустима
#
# print(helper.page_index(5))            # должен = = 1 (отсчитываемый от нуля индекс)
# print(helper.page_index(2))           # должен = = 0
# print(helper.page_index(20))         # должен = = -1
# print(helper.page_index(-10))          # должен = = -1, так как отрицательные индексы недопустимы


def introspection_info(obj):
    return_dict = dict()
    return_dict['type'] = type(obj)
    return_dict['attributes'] = [i for i in dir(obj)]
    return_dict['method'] = [getattr(obj, i) for i in dir(obj)
                             if "<class 'method'>" in str(type(getattr(obj, i)))]
    return_dict['module'] = helper.__class__
    return return_dict


number_info = introspection_info(helper)
pprint(number_info)
