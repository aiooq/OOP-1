'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
    Значения данных атрибутов должны передаваться при создании экземпляра класса. 
    Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. 
    Проверить работу метода.
    Например: 20м * 5000м * 25кг * 5см = 12500 т'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def __call__(self, mass, thickness):
        return self.get_mass_of_asphalt(self, mass, thickness)

    def get_mass_of_asphalt(self, mass, thickness):
        return self._width * self._length * mass * thickness

class Task:
    def __call__(self):
        config = (({"out":"Результат = {0} т","def":self.main}))
        return config

    def main(self, value, out):
        road = Road(5000,20)
        return out.format(road.get_mass_of_asphalt(25,5))

main()([Task()()])