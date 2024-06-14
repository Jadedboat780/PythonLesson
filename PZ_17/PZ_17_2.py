# Дано трехзначное число.
# Вывести вначале его последнюю цифру (единицы),
# а затем - его среднюю цифру (десятки)


import tkinter as tk
from tkinter import messagebox


def get_nums(number) -> None:
    last_digit = number % 10
    middle_digit = (number % 100) // 10
    result = f"Последняя цифра (единица): {last_digit}\nСредняя цифра (десятки): {middle_digit}"
    messagebox.showinfo("Результат", result)


def check_number() -> None:
    number_str = entry.get()
    try:
        number = int(number_str)
        if len(str(number)) == 3:
            get_nums(number)
        else:
            messagebox.showerror("Ошибка", "Введенное вами число не трехзначное")
    except ValueError:
        messagebox.showerror("Ошибка", "Требуется ввести число")


root = tk.Tk()
root.title("Анализ трёхзначного числа")
label = tk.Label(root, text="Введите трёхзначное число:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
button = tk.Button(root, text="Проверить", command=check_number)
button.pack(pady=10)

root.mainloop()
