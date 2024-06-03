class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class RomanNumerals:

    @staticmethod
    def to_roman(val: int) -> str:
        """Принимает любое десятичное число от 1 до 4000,
        возвращяет строковое римское"""
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                         'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman_ = ''
        for letter, value in roman_numbers.items():
            while val >= value:
                roman_ += letter
                val -= value
        return roman_

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """Принимает строковое значение римское число от I до MMMM,
         возвращает в десятичном формате"""
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                         'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0
        index = 0
        for numeral, integer in roman_numbers.items():
            while roman_num[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result


num = RomanNumerals()
while True:
    print("Римское в десятичное 1")
    print("Десятичное в римское 2")
    print("Выход 3")
    try:
        my_menu = int(input("выберите 1-3: "))
        if my_menu > 3 or my_menu < 1:
            raise MyError("Число в не диапазона")
    except MyError as my_error_2:
        print(my_error_2)
    except ValueError as my_error_1:
        print(f"Ошибка ввода {my_error_1}")
    else:
        if my_menu == 1:
            roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            roman_number = ""
            roman = input("Введите римское число: ")
            for number in roman:
                if number in roman_list:
                    roman_number += number
            if roman == roman_number:
                print(f"\033[33mДесятичное число ---> {num.from_roman(roman)}\033[0m")
            else:
                try:
                    raise MyError("Такова римского числа не существует")
                except MyError as my_error:
                    print(my_error)
                finally:
                    print("Попробуйте еще раз")
        elif my_menu == 2:
            try:
                my_number = int(input("Введите десятичное число от 1 до 4000: "))
                if my_number < 1 or my_number > 4000:
                    raise MyError("Число в не диапазона")
            except MyError as my_error_3:
                print(my_error_3)
            except ValueError as my_error_4:
                print(my_error_4)
            else:
                print(f"\033[33mРимское число ---> {num.to_roman(my_number)}\033[0m")
        elif my_menu == 3:
            break
