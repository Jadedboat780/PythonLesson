# 1. Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6, ...
# 2. Дан целочисленный список A размера N. Переписать в новый целочисленный список
# B все четные числа из исходного списка (в том же порядке) и вывести размер полученного список B и его содержимое.
# 3. Дано множество A из N точек (N > 2, точки заданы своими координатами x, у).
# Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A,
# и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два список: первый список для хранения абсцисс,
# второй — для хранения ординат

import math

def func1(array):
    new_array = []
    for num_element, num in enumerate(array, start=1):
        if num_element % 2 == 0:
            new_array.append(num)

    return f'1) Минимальный элемен: {min(new_array)}'

def func2(array):
    new_array = []
    for num in array:
        if num % 2 == 0:
            new_array.append(num)

    return f'2) Размер списка: {len(new_array)}\nСписок: {new_array}'

def func3(x, y):
    n = len(x)
    max_perimeter = 0
    triangle_points = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                side1 = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
                side2 = math.sqrt((x[j] - x[k]) ** 2 + (y[j] - y[k]) ** 2)
                side3 = math.sqrt((x[k] - x[i]) ** 2 + (y[k] - y[i]) ** 2)

                perimeter = side1 + side2 + side3

                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    triangle_points = [i, j, k]

    return f'3) Максимальный периметр: {round(max_perimeter, 2)}, точки наибольшего периметра: {triangle_points}'


def main():
    result1 = func1([1, 2, 3, 4, 5])
    result2 = func2([6, 7, 8, 9, 10, 11])
    result3 = func3([0, 5, 2, 3], [0, 1, 0, 2])
    print(result1, result2, result3, sep="\n")

main()