# 1. Создайте список из 5 машин - ["BMW", "MB", "LADA", "KIA", "HONDA"]

my_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]

# 2. Создайте цикл for и в цикле распечатайте каждый из автомобилей в
# строке 'Я езжу на автомабиле марки'

for i in my_list:
    print('Я езжу на автомабиле марки: ', i)

# 3. Создайте целочисленную переменную cars_count = 0

cars_count = 0

# 4. Напишите в цикле из шага номер 2 увеличение переменной
# на 10 в каждом шаге цикла (cars_count += 10)


for i in [10 for j in range(2)]:
    cars_count += i
    print(cars_count)
print('The End')
