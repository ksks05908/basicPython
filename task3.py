# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse = True)
    print(f'Сумма наибольших двух аргументов: {my_list[0]} + {my_list[1]} = {my_list[0]+my_list[1]}')

arg_1 = float(input('Введите значение: '))
arg_2 = float(input('Введите значение: '))
arg_3 = float(input('Введите значение: '))
my_func(arg_1, arg_2, arg_3)