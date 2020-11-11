# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import os

task3 = os.path.join(os.path.dirname(__file__), 'task3')
strings = 0
average = 0
min_salary = ''
with open(task3, 'r', encoding='UTF-8') as test:
    for line in test:
        i = line.split(' ')
        strings += 1
        average += int(i[1])
        if int(i[1]) < 20000:
            min_salary += i[0] + ' '
print(f'Средняя зарплата сотрудников {average/strings} \n'
      f'Сотрудники с зарплатой <20тыс {min_salary}')
