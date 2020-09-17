# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        print(f'Full name of worker: {self.name + " " + self.surname}')
    def get_total_income(self):
        print(f'Income of worker: {self._income["wage"] + self._income["bonus"]} rubles')
name, surname, position, wage, bonus = 'Ioan','Petrov', 'programmer', 250000, 100000
new_worker = Position(name, surname, position, wage, bonus)
print(f'Position: {new_worker.position}')
new_worker.get_full_name()
new_worker.get_total_income()


