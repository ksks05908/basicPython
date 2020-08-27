# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
user_value = int(input('Введите число: '))
max = 0
while user_value > 0:
    if max < user_value % 10:
        max = user_value % 10
    user_value = user_value // 10
print(max)
