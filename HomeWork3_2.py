# Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True),

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)  # Функция должна выводить эти параметры.


# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.

print_params()
print_params(25)
print_params(25, 38)
print_params(25, 38, 61)

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.

values_list = ["str", 56, False]

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.

values_dict = {"a": "str", "b": int, "c": bool}

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря).

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:

# Создайте список values_list_2 с двумя элементами разных типов

values_list_2 = [True, int]

# Проверьте, работает ли print_params(*values_list_2, 42)

print_params(*values_list_2, 42)
