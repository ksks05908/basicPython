# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [1, 'two', 3.0, ('four', 'five'), {6: 7, 8: 9}, True]
for element in my_list:
    print(f'Элемент {element} является типом данных: {type(element)}')