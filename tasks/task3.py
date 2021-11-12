'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
    Создать класс Position (должность) на базе класса Worker. 
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return self.name

class Position(Worker):
    def __call__(self):
        print(f"get_full_name(): {self.get_full_name()}")
        print(f"\tname: {self.name}")
        print(f"\tsurname: {self.surname}")
        print(f"\tposition: {self.position}")
        print(f"\tget_income(): {self.get_income()}")

    def get_full_name(self):
        return " ".join([self.name,self.surname])

    def get_income(self):
        return self.income["wage"]+self.income["bonus"]

class Task:
    def __init__(self):
        print(f"Start: {__file__}")

    def __del__(self):
        print(f"End: {__file__}")

    def __call__(self):
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        position_1 = Position("Василий", "Петров", "Слесарь", 100, 10)
        position_2 = Position("Алексей", "Сидоров", "Инженер", 1000, 100)

        position_1()
        position_2()

main()([Task()()])