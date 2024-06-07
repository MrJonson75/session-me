def get_perform_calculations(arithmetic_operations):
    """ Задача 1: Фабрика функций """
    if arithmetic_operations == "addition":
        def addition(a, b):
            return a + b

        return addition
    elif arithmetic_operations == "subtraction":
        def subtraction(a, b):
            return a - b

        return subtraction
    elif arithmetic_operations == "multiplication":
        def multiplication(a, b):
            return a * b

        return multiplication
    elif arithmetic_operations == "division":
        def division(a, b):
            try:
                result = a / b
            except ZeroDivisionError as errors_division:
                return errors_division
            else:
                return result

        return division


my_addition = get_perform_calculations("addition")
my_division = get_perform_calculations("division")
my_subtraction = get_perform_calculations("subtraction")
my_multiplication = get_perform_calculations("multiplication")

print("Результат деления : {}".format(my_division(3, 3)))
print("Результат сложения : {}".format(my_addition(3, 3)))
print("Результат вычитания : {}".format(my_subtraction(3, 3)))
print("Результат умножения : {}".format(my_multiplication(3, 3)))
print("Результат деления : {}".format(my_division(3, 0)))

####################################################################################

"""                             Задача 2 лямбда"""


def to_square_def(x, y):
    return x ** y


to_square = lambda x, y: x ** y

print(f'Результат возведения в степень с помощью def :-->{to_square_def(2, 6)}')
print(f'Результат возведения в степень с помощью lambda :-->{to_square(2, 6)}')

"""                          Задача 3: Вызываемые oбъекты"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area_of_rectangle = Rectangle(2, 4)

print(f"Площадь прямоугольника со сторонами"
      f" {area_of_rectangle.a} и {area_of_rectangle.b} ---> {area_of_rectangle.__call__()}")
