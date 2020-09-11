#  Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
data = ['string', 'not interesting string', 'normal string', 'very important string']
with open("task2.txt", 'a+', encoding='utf-8') as f_obj:
    for el in data:
        f_obj.write(el + '\n')
    f_obj.seek(0)
    rows = f_obj.read().splitlines()
for el in rows:
    print(f'Строка "{el}", слов: {len(el.split())}')
print(f'Всего строк: {len(rows)}')