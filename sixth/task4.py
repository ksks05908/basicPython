# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(self.color, self.name)
    def go(self):
        print('Go')
    def stop(self):
        print('Stop')
    def turn(self, direction):
        print(f'Turn {direction}')
    def show_speed(self):
        print(f'Speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('You are going to fast!')
        else:
            print(f'Speed: {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('You are going to fast!')
        else:
            print(f'Speed: {self.speed}')

class PoliceCar(Car):
    pass
print('Move of town car: ')
town_car = TownCar(80, 'black', 'Toyota Rav 4', False)
town_car.show_speed()
town_car.go()

print('\nMove of police car: ')
police_car = PoliceCar(0, 'white', 'Lada Kalina', True)
police_car.show_speed()
police_car.stop()

print('\nMove of work car: ')
work_car = PoliceCar(25, 'Red', 'Jeep', True)
work_car.show_speed()
town_car.turn('right')

