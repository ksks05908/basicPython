# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
user_list = []
while True:
    new_el =  input('Введите элемент списка. Для окончания ввода введите out: ')
    if new_el == 'out':
        break
    user_list.append(new_el)
i = 0
print(f'Список до обмена: {user_list}')
try:
    for el in user_list[0::2]:
        user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
        i += 2
except IndexError:
    print('В списке нечетное кол-во элементов, последний элемент останется на прежнем месте')
print(user_list)

