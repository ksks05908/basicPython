# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json
all_firms = []
average_profit = 0
dict_plus = {}
with open("task7.txt", encoding='utf-8') as f_obj:
    firms = f_obj.read().splitlines()
for firm in firms:
    firm = firm.split()
    dict_plus[firm[0]] = int(firm[2]) - int(firm[3])
    if dict_plus[firm[0]] > 0:
        average_profit += dict_plus[firm[0]]
    all_firms.append(dict_plus)
    firm_plus = {}
dict_plus['average_profit'] = average_profit
all_firms.append(dict_plus)
with open("task7.json", "w") as fjson_obj:
    json.dump(all_firms, fjson_obj)