# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
# list
calendar = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), 'зима', 'весна', 'лето', 'осень',]
number_of_month = int(input('Введите номер месяца: '))
i = 4
for tup in calendar[0:4]:
    for val in tup:
        if val == number_of_month:
            print(calendar[i])
    i += 1
