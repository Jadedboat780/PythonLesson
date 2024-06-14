# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Car:
    def __init__(self, mark: str, model: str, year: int):
        self.mark = mark
        self.model = model
        self.year = year


class Truck(Car):
    def __init__(self, mark: str, model: str, year: int, lifting_capacity: int):
        super().__init__(mark, model, year)
        self.lifting_capacity = lifting_capacity


class PassengerCar(Car):
    def __init__(self, mark: str, model: str, year: int, count_passengers: int):
        super().__init__(mark, model, year)
        self.count_passengers = count_passengers
