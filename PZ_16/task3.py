# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle


class Student:
    def __init__(self, name: str, surname: str, estimation: tuple[int, ...]):
        self.name = name
        self.surname = surname
        self.estimation = estimation

    def average_score(self) -> float:
        return sum(self.estimation) / len(self.estimation)

    def is_excellent(self) -> bool:
        return self.average_score() >= 4.5

    def __str__(self):
        return f'{self.name} {self.surname}'


class Picle:
    @staticmethod
    def save_def(students: list[Student], file_name: str) -> None:
        with open(file_name, 'wb') as file:
            pickle.dump(students, file)

    @staticmethod
    def load_def(file_name: str):
        with open(file_name, 'rb') as file:
            return pickle.load(file)


filename = 'example.bin'

student1 = Student("Nikita", "Tokin", (5, 4, 3))
student2 = Student("Alice", "Sim", (4, 5, 5))
student3 = Student("Bob", "Joh", (3, 3, 4))
students = [student1, student2, student3]

Picle.save_def(students, filename)
loaded_students = Picle.load_def(filename)

for student in loaded_students:
    print(student)
