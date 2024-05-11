# 1.В последовательности их N чисел (N – четное) в первой ее половине найти
# произведение элементов меньших 0.
# 2.Составить генератор (yield), который переведет символы строки из нижнего регистра в верхний.
from functools import reduce


def func1(n):
    mid = len(n) // 2

    filter_n = filter(lambda x: x < 0, n[:mid])
    result = reduce(lambda x, y: x * y, filter_n)

    return result


def func2(string):
    yield from string.upper()


print(func1([-1, -2, -3, 4, -5, 6, -7, -8, -9, -10]))
for char in func2("hello"):
    print(char, end="")
