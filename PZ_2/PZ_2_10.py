# Вариант 10. Даны целые положительные числа A и B (A > B). На отрезке длины A размещено
# максимально возможное количество отрезков длины B (без наложений).
# Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.

def main(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("Делить на ноль нельзя")
    return a // b


if __name__ == "__main__":
    try:
        a = int(input("Введите число А: "))
        b = int(input("Введите число В: "))
        result: int = main(a, b)
        print(f'Ответ: {result}')

    except ZeroDivisionError:
        print("Нельзя делить на ноль")

    except ValueError:
        print("Вы ввели не число")

    finally:
        print("Конец программы")
