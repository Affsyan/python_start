# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
list_month = ['Зима', 'Весна', 'Лето', 'Осень']
dict_month = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}
while True:
    month = input('Введите месяц: ')
    if month.isdigit() and 0 < int(month) <=12:
        month = int(month)
        break
    print('Введите целое число от 0 до 12')
if 3 <= month <= 5:
    print(list_month[1])
elif 6 <= month <= 8:
    print(list_month[2])
elif 9 <= month <= 11:
    print(list_month[3])
else:
    print(list_month[0])
print(dict_month.get(month))
