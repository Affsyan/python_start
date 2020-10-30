# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

while True:
    length_list = input('Введите длинну списка: ')
    if length_list.isdigit():
        length_list = int(length_list)
        break
    print('Введите целое число')
count = 0
first_list = []
while count < length_list:
    first_list.insert(count, input(f'Введите {count} элемент списка: '))
    count += 1
else:
    count = 0
print(f'Ваш список {first_list}')
while count < length_list:
    element = first_list.pop(count)
    first_list.insert(count+1, element)
    count += 2
print(f'После преобразования {first_list}')
