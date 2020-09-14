# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
# толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
class Road():
    def __init__(self, length_road, width_road):
        self._length = length_road
        self._width = width_road
    def mass(self, mass_one, thickness):
        print(self._length * self._width * mass_one * thickness)
my_road = Road(5, 20)
my_road.mass(25, 5)
