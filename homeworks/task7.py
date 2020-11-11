# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
import os
firm_list = []
firm_dict = {}
firm_profit = {}
task7 = os.path.join(os.path.dirname(__file__), 'task7')
with open(task7, 'r', encoding='UTF-8') as test:
    for line in test:
        key, *value = line.split(' ')
        firm_dict[key] = value
profit = 0
firm_list.append(firm_dict)
for key in firm_dict:
    firm_dict[key] = int(firm_dict[key][1]) - int(firm_dict[key][2])
    if firm_dict[key] > 0:
        profit += int(firm_dict[key])
firm_list.append({"average_profit": profit})
print(firm_list)
with open("task7.json", "w") as file:
    json.dump(firm_list, file)
