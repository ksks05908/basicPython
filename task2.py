# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def output_user_info(name, surname, birthday, city, telephone, email):
    print(f'Имя: {name},фамилия: {surname}, дата рождения: {birthday}, город {city}, почта {email}, телефон {telephone}')

user_name = input('Введите имя: ')
surname_user = input('Введите фамилию: ')
birthday_user = input('Введите дату рождения: ')
city_user = input('Введите город проживания: ')
email_user = input('Введите почту: ')
telephone_user = input('Введите телефон: ')
output_user_info(name=user_name, surname=surname_user, birthday=birthday_user, city=city_user, email=email_user, telephone=telephone_user)