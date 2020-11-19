# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
import math


class Wear(ABC):

    @property
    @abstractmethod
    def consumption(self):
        pass

    @property
    @abstractmethod
    def params(self):
        pass


class Suit(Wear):

    def __init__(self, name, height):
        self.height = height
        self.name = name

    @property
    def consumption(self):
        return f"Для пошива {self.name} нужно {math.ceil(2 * self.height + 0.3)} ткани."

    @property
    def params(self):
        return


class Coat(Wear):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def consumption(self):
        return f"Для пошива {self.name} нужно {math.ceil(self.size / 6.5 + 0.5)} ткани."

    @property
    def params(self):
        return


test = Coat('Пальто', 25)
print(test.consumption)
test1 = Suit('Пиджак', 170)
print(test1.consumption)
