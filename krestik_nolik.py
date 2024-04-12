# Крестики нолики
def print_pole_list():  # функция перерисовки поля
    for i in pole_list:
        print("          ", *i)
    print()
def check_victory():
    s_1, s_2, s_3 = " ", " ", " "
    n = 3
    m = 3
    # **************************************************************
    # Проверка строк
    for j in range(n):
        for i in range(m):
            if i == 0:
                s_1 = pole_list[j][i]
            elif i == 1:
                s_2 = pole_list[j][i]
            elif i == 2:
                s_3 = pole_list[j][i]
        if s_1 == s_2 == s_3 == "X":
            return "X"
        elif s_1 == s_2 == s_3 == "0":
            return "0"

    # **************************************************************
    # Проверка столбцов

    for j in range(n):
        for i in range(m):
            if i == 0:
                s_1 = pole_list[i][j]
            elif i == 1:
                s_2 = pole_list[i][j]
            elif i == 2:
                s_3 = pole_list[i][j]
        if s_1 == s_2 == s_3 == "X":
            return "X"
        elif s_1 == s_2 == s_3 == "0":
            return "0"

    # *****************************************************************
    # Проверка диагоналей

    for i in range(n):
        for j in range(m):
            if j == 2 and i == 0:
                s_1 = pole_list[i][j]
            elif j == 1 and i == 1:
                s_2 = pole_list[i][j]
            elif j == 0 and i == 2:
                s_3 = pole_list[i][j]
    if s_1 == s_2 == s_3 == "X":
        return "X"
    elif s_1 == s_2 == s_3 == "0":
        return "0"

    for i in range(n):
        for j in range(m):
            if j == 0 and i == 0:
                s_1 = pole_list[i][j]
            elif j == 1 and i == 1:
                s_2 = pole_list[i][j]
            elif j == 2 and i == 2:
                s_3 = pole_list[i][j]
    if s_1 == s_2 == s_3 == "X":
        return "X"
    elif s_1 == s_2 == s_3 == "0":
        return "0"

    return "*"


pole_list = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("   Поиграем Х и 0")
print()
print_pole_list()
for step_my in range(1, 10):
    print(f"Ход: {step_my}")
    if step_my % 2 == 0:
        print("     Ходят нолики")
        tern_char = "0"
    else:
        print("     Ходят крестики")
        tern_char = "X"

    row = int(input("Введите номер строки(1, 2, 3) ")) - 1
    while row < 0 or row > 2:
        print("Ошибка ввода !")
        row = int(input("Введите номер строки(1, 2, 3) ")) - 1

    column = int(input("Введите номер колонки(1, 2, 3) ")) - 1
    while column < 0 or column > 2:
        print("Ошибка ввода !")
        column = int(input("Введите номер колонки(1, 2, 3) ")) - 1

    while pole_list[column][row] != "*":
        print("Ячейка занята выберете другую")
        row = int(input("Введите номер строки(1, 2, 3) ")) - 1
        column = int(input("Введите номер колонки(1, 2, 3) ")) - 1
    else:
        pole_list[column][row] = tern_char
    print_pole_list()

    if check_victory() == "X":
        print("П О Б Е Д А   Х !!!")
        break
    if check_victory() == "0":
        print("П О Б Е Д А   0 !!!")
        break
    if check_victory() == "*" and step_my == 9:
        print("У ВАС НИЧЬЯ")
№