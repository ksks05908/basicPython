# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import copy

class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        output_matrix = ''
        for element in self.elements:
            output_matrix += ' '.join(map(str, element)) + '\n'
        return f'{output_matrix}'

    def __add__(self, other):
        try:
            new_list = copy.copy(self.elements)
            for i in range(0, len(new_list)):
                for y in range(0, len(self.elements[i])):
                    new_list[i][y] += other.elements[i][y]
            return (Matrix(new_list))
        except IndexError:
            return None

mt_1 = Matrix([[1, 2], [1, 1]])
mt_2 = Matrix([[1, 1], [1, 1]])
mt_3 = mt_1 + mt_2
print(mt_3)



