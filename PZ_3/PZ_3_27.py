# Вариант 27.
# 1. Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
# лежит во второй или третьей координатной четверти».
# 2. Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.).
# Вывести название соответствующего времени года («зима», «весна», «лето»,
# «осень»).

class MonthError(Exception):
    def __init__(self, message: str):
        self.message: str = message

    def __repr__(self):
        return self.message


def func1() -> bool:
    x = int(input("Введите координату х: "))
    y = int(input("Введите координату y: "))

    if (x < 0 and y > 0) or (x < 0 and y < 0):
        return True
    return False

def func2() -> str:
    month_num: int = int(input("Введите номер месяца: "))

    winter: tuple[int, int, int] = (12, 1, 2)
    spring: tuple[int, int, int] = (3, 4, 5)
    summer: tuple[int, int, int] = (6, 7, 8)
    autumn: tuple[int, int, int] = (9, 10, 11)

    if month_num in winter:
        return "Зима"
    elif month_num in spring:
        return "Весна"
    elif month_num in summer:
        return "Лето"
    elif month_num in autumn:
        return "Осень"
    else:
        raise MonthError("Вы ввели слишком большое число")

def main():
    try:
        print(func1())
        print(func2())

    except ValueError:
        print("Вы ввели строку вместо числа")

    except MonthError as err:
        print(err)

main()