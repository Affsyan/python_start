# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def check(a):
    while True:
        if len(a) != 3:
            print('Ошибка ввода')
            a = input('Введите 3 числа через пробел: ').split(' ')
            if type(a) != tuple:
                print('Ошибка ввода')
                a = input('Введите 3 числа через пробел: ').split(' ')
            continue
        else:
            try:
                a = float(a[0]) + float(a[1]) + float(a[2])
            except ValueError:
                print('Ошибка ввода')
                a = input('Введите 3 числа через пробел: ').split(' ')
                continue
        break
    print(a)
    return a

user_number = input('Введите 3 числа через пробел: ').split(' ')
number = check(user_number)


