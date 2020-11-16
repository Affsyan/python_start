# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
matrix_list1 = [1, 2, 3]
matrix_list2 = [4, 5, 6]
matrix_list3 = [7, 8, 9]

matrix_list4 = [9, 8, 7]
matrix_list5 = [6, 5, 4]
matrix_list6 = [3, 2, 1]


class Matrix:
    def __init__(self, *param):
        self.param = param

    def __str__(self):
        return '\n'.join(map(str, self.param))

    def __add__(self, other):
        sum_m = []
        for i in zip(self.param, other.param):
            numbers = []
            for j in zip(i[0], i[1]):
                numbers.append(sum(j))
            sum_m.append(numbers)
        return '\n'.join(map(str, sum_m))


m1 = Matrix(matrix_list1, matrix_list2, matrix_list3)
m2 = Matrix(matrix_list4, matrix_list5, matrix_list6)
print(f"Матрица №1\n{m1}\nМатрица №2\n{m2}")
print(f"Сумма матриц\n{m1 + m2}")

