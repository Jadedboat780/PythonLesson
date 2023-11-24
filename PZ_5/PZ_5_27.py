# Вариант 27
# 1. Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.
# 2. Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
# числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K справа
# данные цифры D1 и D2, выводя результат каждого добавления.

import random

def func1():
    random_num = random.randint(1000, 9999)
    print(random_num)

    first_num = random_num // 1000
    second_num = random_num // 100 % 10
    third_num = random_num // 10 % 10
    fourth_num = random_num % 10

    num_tuple = (first_num, second_num, third_num, fourth_num)

    if len(num_tuple) != len(set(num_tuple)):
        print("Число повторяется")
    else:
        print("Число не повторяется")


def func2(d1, d2, k):
    if not (1 <= d1 <= 9) and not (1 <= d2 <= 9) :
        raise ValueError("Вы ввели число d в неправильном диапозоне")

    k = k * 10 + d1
    print(k)
    k = k * 10 + d2
    print(k)


def main():
    try:
        func1()
        d1 = int(input('Введите цислое число d1 в диопазоне от 0 до 9: '))
        d2 = int(input('Введите цислое число d2 в диопазоне от 0 до 9: '))
        k = int(input('Введите цислое число k: '))
        func2(d1, d2, k)

    except ValueError as err:
        print(err)


main()