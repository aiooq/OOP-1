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
        self.color = None
        self.name = "TrafficLight"

    def set_color(self, color, seconds):
        self.color = color
        print(f"{datetime.now()}: {self.name} Mode = {self.color}")
        time.sleep(seconds)

    def running(self):
        print(f"{datetime.now()}: {self.name} Started")
        self.set_color("Red",7)
        self.set_color("Yellow",2)
        self.set_color("Green",5)
        print(f"{datetime.now()}: {self.name} Stopped")

class Task:
    def __call__(self):
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        traffic_light = TrafficLight()

        tread = threading.Thread(target=traffic_light.running)
        tread.start()
        while tread.is_alive():
            print(f"{datetime.now()}: {traffic_light.name}: Get Mode = {traffic_light.color}")
            time.sleep(1)
        

        
