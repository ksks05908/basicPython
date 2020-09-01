# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользоват
goods = []
specific = {'наименование': None, 'цена': None, 'количество': None, 'единицы измерения': None}
number_of_goods = 1
charact = [[],[],[],[]]
while True:
    new_input = input('Вы хотите ввести товар? (да/нет) ')
    if new_input != 'да':
        break
    i = 0
    new_good = {}
    to_tuple = []
    for key in specific:
        new_char = input(f'Введите следующую характеристику товара: {key} ')
        charact[i].append(new_char)
        i += 1
        new_good[key] = new_char
    to_tuple.append(number_of_goods)
    to_tuple.append(new_good)
    goods.append(tuple(to_tuple))
    number_of_goods += 1
i = 0
for key in specific:
    specific[key] = charact[i]
    i += 1
print(f'Стуктура данных:\n{goods}')
print(f'Аналитика:\n{specific}')
