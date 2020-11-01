# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def check_number1(a):
    while True:
        try:
            a = float(a)
        except ValueError:
            print('Ошибка ввода')
            a = input('Введите положительное число: ')
            continue
        if a < 0:
            print('Ошибка ввода')
            a = input('Введите положительное число: ')
            continue
        break
    return a


def check_number2(a):
    while True:
        try:
            a = int(a)
        except ValueError:
            print('Ошибка ввода')
            a = input('Введите целое отрицательное число: ')
            continue
        if a > 0:
            print('Ошибка ввода')
            a = input('Введите целое отрицательное число: ')
            continue
        break
    return a


def exponentiation(x, y):
    print(x ** y)
    count = 1
    for i in range(abs(y)):
        count /= x
    print(count)


number1 = check_number1(input('Введите положительное число: '))
number2 = check_number2(input('Введите целое отрицательное число: '))
exponentiation(number1, number2)
