# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, присутствующие во втором:
# Элементы второго файла, присутствующие в первом:
# Количество элементов:
# Количество отрицательных элементов:
# Количество положительных элементов:

import random


def generate_file(filename, num_elements, min_value, max_value):
    with open(filename, 'w', encoding='utf-8') as file:
        numbers = [str(random.randint(min_value, max_value)) for _ in range(num_elements)]
        file.write(' '.join(numbers))


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(map(int, file.read().split()))


# Генерация файлов
generate_file('file1.txt', 20, -10, 10)
generate_file('file2.txt', 10, -10, 10)

# Чтение файлов
file1_content = read_file('file1.txt')
file2_content = read_file('file2.txt')

# Вычисление требуемых параметров
elements_in_both = set(file1_content).intersection(set(file2_content))
elements_in_file1 = set(file1_content)
elements_in_file2 = set(file2_content)
count_elements = len(file1_content) + len(file2_content)
count_negative_elements = sum(1 for x in file1_content + file2_content if x < 0)
count_positive_elements = sum(1 for x in file1_content + file2_content if x > 0)

# Создание нового файла с результатами
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f"Элементы первого и второго файлов:\n")
    file.write(f"Файл 1: {' '.join(map(str, file1_content))}\n")
    file.write(f"Файл 2: {' '.join(map(str, file2_content))}\n")
    file.write(f"\nЭлементы первого файла, присутствующие во втором:\n")
    file.write(f"{' '.join(map(str, elements_in_both))}\n")
    file.write(f"\nЭлементы второго файла, присутствующие в первом:\n")
    file.write(f"{' '.join(map(str, elements_in_both))}\n")
    file.write(f"\nКоличество элементов:\n")
    file.write(f"{count_elements}\n")
    file.write(f"\nКоличество отрицательных элементов:\n")
    file.write(f"{count_negative_elements}\n")
    file.write(f"\nКоличество положительных элементов:\n")
    file.write(f"{count_positive_elements}\n")
