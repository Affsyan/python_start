# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os
import random


task5 = os.path.join(os.path.dirname(__file__), 'task5')
with open(task5, 'w', encoding='UTF-8') as test:
    test.write(' '.join(map(str, [random.randrange(0, 100) for i in range(0, 100)])))
with open(task5, 'r', encoding='UTF-8') as test:
    for el in test:
        number_list = el.split(' ')
        print(sum(map(int, number_list)))
