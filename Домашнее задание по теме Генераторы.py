# Цель работы
import itertools


# Более глубоко понять особенности работы с функциями генераторами
# и оператором yield в Python.

# Задание

# Напишите функцию-генератор all_variants, которая будет возвращать все
# подпоследовательности переданной строки. В функцию передаётся только сама строка.

# Примечание

# Используйте оператор yield

def all_variants(my_str):
    """ принимаем список"""
    temp_list = []  # создаем пустой список
    for lst_1 in range(1, len(my_str) + 1):
        """ Используя цикл и библиотеку itertools создаем матрицу кортежей 
        всех последовательностей входящей строки"""
        temp_list.append(list(itertools.combinations(my_str, lst_1)))
    for lst_2 in temp_list:  # проходимся по временному списку
        for lst_3 in lst_2:  # проходимся по вложенному списку
            if ''.join(lst_3) != 'ac':
                yield ''.join(lst_3)


a = all_variants("abc")
for i in a:
    print(i)
