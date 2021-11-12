'''4. Реализуйте базовый класс Car. 
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
    Для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. 
    Выполните доступ к атрибутам, выведите результат. 
    Выполните вызов методов и также покажите результат.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Car:
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def __call__(self):
        self.show_speed()
        self.stop()
        self.go(100)
        self.turn("вправо")
        print(f"name: {self.name}")
        print(f"\tspeed: {self.speed}")
        print(f"\tcolor: {self.color}")
        print(f"\tis_police: {self.is_police}")

    def __str__(self):
        return self.name

    def go(self, speed):
        self.speed = speed
        print(f"Автомобиль {self.name}, поехал, скорость = {self.speed} км/ч")

    def stop(self):
        self.speed = 0
        print(f"Автомобиль {self.name}, остановился, скорость = {self.speed} км/ч")

    def turn(self, direction):
        print(f"Автомобиль {self.name}, повернул {direction}")

    def show_speed(self):
        print(f"Автомобиль {self.name}, текущая скорость = {self.speed} км/ч")

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color, True)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f"Автомобиль {self.name}, текущая скорость = {self.speed} км/ч [превышение]")
        Car.show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"Автомобиль {self.name}, текущая скорость = {self.speed} км/ч [превышение]")
        Car.show_speed()        

class Task:
    def __init__(self):
        print(f"Start: {__file__}")

    def __del__(self):
        print(f"End: {__file__}")

    def __call__(self):
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        sport_car = SportCar("Ford Mustang", 100, "red")
        police_car = PoliceCar("Ford", 50, "black")
        town_car = TownCar("Town Car", 70, "red")
        work_car = WorkCar("Work Car", 50, "red")

        for car in [sport_car,police_car,town_car,work_car]:
            car()

        print(sport_car.name)
        town_car.show_speed()

main()([Task()()])