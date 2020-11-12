# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

import random


class Car:
    speed = 70
    color = 'red'
    name = 'BMW'
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        direction = random.randrange(0, 2)
        if direction == 1:
            print('Машина повернула направо')
        else:
            print('Машина повернула налево')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def show_speed(self):
        print('Едем')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def show_speed(self):
        print('Едем')


test1 = Car()
test2 = WorkCar()
test3 = PoliceCar()
test1.turn()
test2.show_speed()
test3.show_speed()
