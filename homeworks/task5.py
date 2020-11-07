# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def check(user_len):
    while True:
        user_len_copy = list(user_len)
        if 'q' in user_len_copy:
            user_len_copy = user_len_copy[0:(user_len_copy.index('q'))-1]
        try:
            for el in user_len_copy:
                int(el)
        except ValueError:
            print('Ошибка ввода')
            user_len = input('Введите числа через пробел (Для завершения программы введите q):  ').split(' ')
            continue
        break
    return user_len


sum_number = 0
i = 0
while i != 'q':
    user_number = check(input('Введите числа через пробел (Для завершения программы введите q): ').split(' '))
    for i in user_number:
        if i == 'q':
            break
        sum_number += int(i)
        continue
    print(f'Сумма чисел равна: {sum_number}')
print('Завершение программы')


