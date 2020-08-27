# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_value = input('Введите число: ')
print(int(user_value)+int(user_value+user_value)+int(user_value+user_value+user_value))