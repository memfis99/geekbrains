'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). П
роверить работу примера, создав экземпляр и вызвав описанный метод.'''

import time


class TrafficLight:
    color = ['Red', 'Yellow', 'Green']

    def running(self):
        col_red = 'Red'
        col_yellow = 'Yellow'
        col_green = 'Green'
        for i in self.color:
            print(i)
            if i == col_red:
                time.sleep(7)
            elif i == col_yellow:
                time.sleep(2)
            elif i == col_green:
                time.sleep(5)


Run = TrafficLight()

Run.running()
