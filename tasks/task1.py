'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
        Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

import time
import threading
from datetime import datetime

class TrafficLight:
    def __init__(self):
        self.tread = None
        self.color = None
        self.name = "TrafficLight"

    def __call__(self, *args):
        if not self.get_is_works():
            self.tread = threading.Thread(target=self.__works, args=args)
            self.tread.start()
            return True
        else:
            return False

    def get_is_works(self):
        if self.tread == None:
            return False
        return self.tread.is_alive()

    def set_color(self, color, seconds):
        self.color = color
        print(f"{datetime.now()}: {self.name} Mode = {self.color}")
        time.sleep(seconds)

    def __works(self, *args):
        args=args[0]
        print(f"{datetime.now()}: {self.name} Started")
        self.set_color("Red",args[0])
        self.set_color("Yellow",args[1])
        self.set_color("Green",args[2])
        print(f"{datetime.now()}: {self.name} Stopped")

    def running(self, *args):
        return self.__call__(args)

class Task:
    def __call__(self):
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        traffic_light = TrafficLight()
        if traffic_light.running(7,2,5):
            while traffic_light.get_is_works():
                print(f"{datetime.now()}: {traffic_light.name}: Get Mode = {traffic_light.color}")
                time.sleep(1)

main()([Task()()])