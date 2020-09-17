# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter
    @abstractmethod
    def fabric_rate(self):
        pass

class Coat(Clothes):
    @property
    def fabric_rate(self):
        return f'{self.parameter/6.5 + 0.5:.2f}'

class Costume(Clothes):
    @property
    def fabric_rate(self):
        return f'{self.parameter*2 + 0.3:.2f}'

my_coat = Coat(46)
print(f'На человека с размером {my_coat.parameter} для пошива пальто необходимо {my_coat.fabric_rate} единиц ткани')
my_costume = Costume(175)
print(f'На человека ростом {my_costume.parameter} для пошива пальто необходимо {my_costume.fabric_rate} единиц ткани')










