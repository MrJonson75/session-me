# 1 Создайте новую функцию def test... с произвольным числом
# параметров разного типа, функция должна распечатывать эти
# параметры внутри своего тела

def test_param(*n, name="txt,", **m):
    print(n, m, name)


test_param(1, 3, 5, 6, name="my_dict", i1="test1", i2="test2", i3="test3")


# 2 Создайте рекурсивную функцию, которая будет считать факториал
# от числа n, n - передается в параметре

def test_factorial(n):
    if n == 1:
        return 1
    else:
        return n * test_factorial(n - 1)


test1 = test_factorial(3)
print()
print("!3 =", test1)
test2 = test_factorial(6)
print("!6 =", test2)
print("!3 + !6 = ", test1 + test2)