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
        if  31 < number[0] < 1



test = Data("15-11-2020")
Data.number()
