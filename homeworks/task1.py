# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    data = ''

    def __init__(self, data: str):
        Data.data = data

    @classmethod
    def number(cls):
        number = cls.data.split('-')
        number = list(map(int, number))
        Data.valid(number)

    @staticmethod
    def valid(number):
        m30 = (4, 6, 9, 11)  # месяцы с 30 днями
        m31 = (1, 3, 5, 7, 8, 10, 12)  # месяцы с 31 днём
        if number[2] % 4 != 0 or (number[2] % 100 == 0 and number[2] % 400 != 0):
            leap_year = False
        else:
            leap_year = True
        if number[1] > 12:
            return print('Неправильный ввод')
        else:
            if number[1] in m30:
                if number[0] >= 31:
                    return print('Неправильный ввод')
                else:
                    return print('Данные корректны')
            elif number[1] in m31:
                if number[0] >= 32:
                    return print('Неправильный ввод')
                else:
                    return print('Данные корректны')
            else:
                if number[0] >= 29 and not leap_year:
                    return print('Неправильный ввод')
                elif number[0] >= 30 and leap_year:
                    return print('Неправильный ввод')
                else:
                    return print('Данные корректны')


test = Data("29-2-2019")
Data.number()
test2 = Data("29-2-2020")
Data.number()
