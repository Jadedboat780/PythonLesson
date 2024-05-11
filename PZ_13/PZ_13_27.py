# 1. В матрице найти среднее арифметическое положительных элементов, кратных 3.
# 2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

def find_mean_of_multiples(matrix) -> float | str:
    multiples = [element for row in matrix for element in row if element % 3 == 0]
    if not multiples:
        raise Exception("В матрице нет положительных элементов, кратных 3")
    return sum(multiples) / len(multiples)


def increase_row_by_n(matrix, row_number) -> list[list[int]] | str:
    n = 3
    if 1 > row_number or row_number > len(matrix):
        raise Exception("Недопустимый номер строки")
    return [row[:] if i != row_number - 1 else [element + n for element in row] for i, row in enumerate(matrix)]


matrix = [[i + 3 * j for i in range(1, 4)] for j in range(3)]
print("Исходная матрица: ", matrix)

mean = find_mean_of_multiples(matrix)
print("Среднее арифметическое положительных элементов, кратных 3:", mean)

row_number = int(input("Введите номер строки для увеличения на 3: "))
result_matrix = increase_row_by_n(matrix, row_number)
print("Матрица после увеличения строки на 3:", result_matrix)
