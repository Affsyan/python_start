# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

task4 = os.path.join(os.path.dirname(__file__), 'task4')
d_en = {}
d_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open(task4, 'r', encoding='UTF-8') as test:
    for line in test:
        i = line.split(' ')
        i[0] = d_ru[i[0]]
        test = open('task4.txt', 'a', encoding='UTF-8')
        test.write(' '.join(i))
test.close()
