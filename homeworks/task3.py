class Cell:
    def __init__(self, cell_count):
        self.__cell_count = cell_count

    @property
    def cell_count(self):
        return self.__cell_count

    def __add__(self, other):
        """Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток."""

        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        """ todo Вычитание. Участвуют две клетки.
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
        иначе выводить соответствующее сообщение.
        """
        new_cell = self.cell_count - other.cell_count
        if new_cell > 0:
            return Cell(new_cell)
        raise ValueError('The difference is less than or equal to zero')

    def __truediv__(self, other):
        """Деление. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как
        целочисленное деление количества ячеек этих двух клеток.
        """
        return self.__floordiv__(other)

    def __mul__(self, other):
        """Умножение. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        """
        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        # целочисленное деление
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, cells_in_lines: int):
        if not isinstance(cells_in_lines, int):
            raise TypeError('cells_in_lines int type only')
        temp = self.cell_count // cells_in_lines
        temp2 = self.cell_count % cells_in_lines
        result = '\n'.join(['*' * cells_in_lines + '*' * temp2 if idx + 1 == temp and temp2
                            else '*' * cells_in_lines
                            for idx in range(temp)]
                           )
        return result


if __name__ == '__main__':
    c1 = Cell(13)
    c2 = Cell(2)
    print(c1.make_order(2))
    print(1)
