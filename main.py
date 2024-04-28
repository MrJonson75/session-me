#Пространство имен и области видимости.
def test_function(): #Первая функция
    print("Привет ")
    def inner_function(): #Функция которую нужно вызвать из первой функции.
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
# inner_function() напрямую вызвать функцию нельзя, ниже код как можно
def test_function1(flag=0):
    def inner_function1():
        print("Я в области видимости функции test_function1")

    if flag:
        print("Вызов из вложенной функции")
    else:
        inner_function1()
test_function1()
test_function1(1)