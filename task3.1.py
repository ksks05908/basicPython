# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
# dict
calendar = {
    'зима': (12, 1, 2),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11),
}
number_of_month = int(input('Введите номер месяца: '))
for key in calendar:
    for val in calendar[key]:
        if val == number_of_month:
            print(key)
            break