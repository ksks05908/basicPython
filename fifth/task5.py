# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
with open("task5.txt", 'w+', encoding='utf-8') as f_obj:
    for _ in range(0, 5):
        f_obj.write(str(random.randint(0, 10)) + ' ')
    f_obj.seek(0)
    numbers = f_obj.read()
new_numbers = [int(num) for num in numbers.split()]
'''Здесь есть вопрос, можно ли написать numbers = [int(num) for num in numbers]?
Появилась мысль, что я изменяю область памяти, при этом используя еще неизмененные значения.
Нет ли здесь противоречий? И правильно ли я понимаю что происходит в этом случае?'''
print(f'Sum of elements {sum(new_numbers)}')