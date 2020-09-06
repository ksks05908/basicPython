# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division (a,b):
    return a/b
while True:
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    if divider == 0:
        print('Делитель не может равняться 0')
    else:
        break
result = division(dividend, divider)
print(f'Результат деления: {result:.3f}')