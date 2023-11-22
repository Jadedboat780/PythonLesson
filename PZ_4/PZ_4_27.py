# Вариант 27.
# 1. Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
# 2. Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых
# сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму.

def func1(number):
    if number < 0:
        raise ValueError("Вы ввели число в неправильном диапозоне")

    sum = 0

    for num in range(1, number + 1):
        sum += 1 / num

    return sum

def func2(number):
    if number < 1:
        raise ValueError("Вы ввели число в неправильном диапозоне")

    sum = 0
    k = 0
    flag = True

    while flag:
        k += 1
        sum += k

        if sum >= number:
            flag = False

    return k, sum


def main():
    try:
        number1 = int(input("Введите целое число для задачи 1, оно должно быть больше нуля: "))
        print(func1(number1))

        number2 = int(input("Введите целое число для задачи 1, оно должно быть больше единицы: "))
        print(func2(number2))

    except ValueError as err:
        print(err)


main()