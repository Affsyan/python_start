# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def check(user_len):
    while True:
        try:
            for el in user_len:
                int(el)
        except ValueError:
            print('Ошибка ввода')
            user_len = input('Введите 3 числа через пробел: ').split(' ')
            continue
        if len(user_len) != 3:
            print('Ошибка ввода')
            user_len = input('Введите 3 числа через пробел: ').split(' ')
            continue
        break
    print(user_len)
    return user_len


def sum_number(*args):
    args = sorted(args)
    print(args)
    print(f'Самые большие числа {args[-1]} и {args[-2]}')
    print(f'Сумма чисел равна: {int(args[-2]) + int(args[-1])}')


user_number = input('Введите 3 числа через пробел: ').split(' ')
check(user_number)
sum_number(*user_number)
