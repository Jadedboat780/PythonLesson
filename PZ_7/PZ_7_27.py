# 1. Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S.
# 2. Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти количество слов в строке.

def func1(c: str, s: str) -> str:
    new_s: str = ''
    for char in s:
        if char == c:
            new_s += char*2
        else:
            new_s += char

    return new_s



def func2(string: str) -> int:
    return len(string.split())


def main():
    print(func1("o", "hello word"))
    print(func2("hello word!"))

main()
