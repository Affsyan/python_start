# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

length_list = int(input('Введите длинну списка: '))
count = 0
first_list = []
while count < length_list:
    first_list.insert(count, input(f'Введите {count} элемент списка: '))
    count += 1
print(f'Ваш список {first_list}')
for i in first_list:
    first_list[i] =
print (first_list)