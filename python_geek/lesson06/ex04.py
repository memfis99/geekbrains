'''4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости'''

import random


class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    show_speed: int

    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed
        my_dict = ['left', 'right', 'turnaround']
        self.my_dict = my_dict

    def go(self):
        return print(f'The car {self.name} gone')

    def stop(self):
        return print(f'The car {self.name} stop')

    def turn(self):
        return print(f' The car {self.name} turn {random.choices(self.my_dict)}')

    def just_car(self):
        print(self.go())
        print(self.stop())
        print(self.turn())


class TownCar(Car):

    def town_car(self):
        print(self.just_car())
        if self.speed > 60:
            print(f'speed limit exceeded {self.show_speed}]')


class WorkCar(Car):

    def work_car(self):
        print(self.just_car())
        if self.speed > 40:
            print(f'speed limit exceeded {self.show_speed}]')


car1 = Car(50, 'red', 'mazda', False, 50)
car2 = WorkCar(50, 'green', 'honda', False, 40)
car3 = TownCar(70, 'blue', 'kia', False, 60)

car1.just_car()
car2.work_car()
car3.town_car()
