# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
income = 0
with open("task3.txt", encoding='utf-8') as f_obj:
    rows = f_obj.read().splitlines()
print('Сотрудники с зарплатой < 20:')
for row in rows:
    salary = int(row.split(':')[1])
    income += salary
    if salary < 20:
        print(row)
print(f'Средний доход всех сотрудников: {income/len(rows):.1f}')
