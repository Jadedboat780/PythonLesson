# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником

class Student:
    def __init__(self, name: str, surname: str, estimation: tuple[int]):
        self.name = name
        self.surname = surname
        self.estimation = estimation

    def average_score(self) -> float:
        return sum(self.estimation) / len(self.estimation)

    def is_excellent(self) -> bool:
        return self.average_score() >= 4.5


student = Student("Nikita", "Tokin", (4, 5, 3))
print(student.average_score())
print(student.is_excellent())
