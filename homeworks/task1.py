# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def check(a):
    while True:
        try:
            a = float(a)
        except ValueError:
            print('Ошибка ввода')
            a = input('Повторно введите число: ')
            continue
        break
    return a


def division(a, b):
    if b == 0:
        print('Невозможно поделить на 0')
    else:
        print(f'{a}/{b} = {a/b}')


number1 = check(input('Введите первое число: '))
number2 = check(input('Введите второе число: '))
division(number1, number2)
