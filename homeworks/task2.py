# 2. Представлен список чисел. Необходимо вывести элементы исходного списка
# , значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random


def max_element(number_list):
    max_number = []
    count = 0
    while count < len(number_list):
        if number_list[count] > number_list[count + 1]:
            max_number.append(number_list[count])
        else:
            max_number.append(number_list[count+1])
        count += 2
    print(max_number)


number = []
for i in range(20):
    number.append(random.randint(0, 100))
print(number)
max_element(number)
