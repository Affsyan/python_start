# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Черчение'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} ручкой.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} карандашом.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} маркером.')


test = Stationery()
test1 = Pen()
test2 = Pencil()
test3 = Handle()

test.draw()
test1.draw()
test2.draw()
test3.draw()