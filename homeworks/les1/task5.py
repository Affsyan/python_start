# # 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if proceeds > costs:
    print("Ваша фирма приносит прибыль")
    print("Рентабельность выручки",((proceeds-costs)/proceeds))
    worker = int(input("Укажите количество сотрудников фирмы: "))
    print("Прибыль фирмы в расчёте на одного сотрудника:",((proceeds-costs)/worker))
else:
    print("Ваша фирма терпит убытки")
