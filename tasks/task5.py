'''5. Реализовать класс Stationery (канцелярская принадлежность). 
    Определить в нем атрибут title (название) и метод draw (отрисовка). 
    Метод выводит сообщение “Запуск отрисовки.” 
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
    В каждом из классов реализовать переопределение метода draw. 
    Для каждого из классов методы должен выводить уникальное сообщение. 
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Stationery:
    def __init__(self, title):
        self.title = title

    def __call__(self):
        self.draw()

    def __str__(self):
        return self.title

    def draw(self):
        print(f"{self.title}: Запуск отрисовки. 0")

class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, "Ручка")

    def draw(self):
        print(f"{self.title}: Запуск отрисовки. 123")

class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, "Карандаш")

    def draw(self):
        print(f"{self.title}: Запуск отрисовки. 456")

class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self, "Маркер")

    def draw(self):
        print(f"{self.title}: Запуск отрисовки. 789")


class Task:
    def __init__(self):
        print(f"Start: {__file__}")

    def __del__(self):
        print(f"End: {__file__}")

    def __call__(self):
        config = (({"def":self.main}))
        return config

    def main(self, value, out):

        for item in [Stationery("канцелярская принадлежность"), Pen(),Pencil(),Handle()]:
            item.draw()

main()([Task()()])