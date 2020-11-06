# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from sys import argv
from itertools import cycle


def cycle_list(n):
    i = 0
    while i != 5:
        for el in number_list:
            cycle_list(el)
            print(el)
        i += 1


# _, number = argv
# [print(next(cycle([i]))) for i in range(number, number * 5) if i % 2 == 0]

number_list = [1, 2, 3, 4, 5]
cycle_list(number_list)


