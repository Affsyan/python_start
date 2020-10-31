# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def check(a):
    while True:
        if len(a) > 2:
            print('Ошибка ввода')
            a = input('Введите не более 3х чисел через пробел: ').split(' ')
        else:
            try:
                for i
            except ValueError:
                print('Ошибка ввода')
                a = input('Введите числа через пробел: ').split(' ')
                continue
        break
    return a


def sum_max (a, b, c, *d):
    print(a + b + c)


user_number = input('Введите числа через пробел: ').split(' ')
sum_max(*user_number)

