# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} start drawing')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} start drawing')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} start drawing')

dr_pen = Pen('Blue pen')
dr_pen.draw()
dr_pencil = Pencil('Green pencil')
dr_pencil.draw()
dr_handle = Handle('Yellow pen')
dr_handle.draw()
# При решении данной задачи не было необходимости использовать функцию super(),
# так как в данных классах переопределяются методы draw(), и родительский метод для них как будто "невидимый"
# При решении с использованием этой функции получалось, что дочерние методы дополняют
# родительский метод, а не переопределяет его, я правильно понимаю?


