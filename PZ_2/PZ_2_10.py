#Вариант 10

def main(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("Делить на ноль нельзя")

    return a // b


def tests() -> None:
    '''Тесты для задачи'''

    assert main(5, 12) == 0
    assert main(21, 5) == 4


if __name__ == "__main__":
    tests()

    a = int(input("Введите число А: "))
    b = int(input("Введите число В: "))
    result = main(a, b)

    print(result)