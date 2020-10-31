# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def check(a,b):
    while True:
        try:
            a = int(a)
        except ValueError:
            print('Ошибка ввода')
            a = input(f'Введите {b}: ')
            continue
        break
    return a


def user_data(name, surname, year_of_birth, city, email, tel):
    print(f'Пользователь {name} {surname}. {year_of_birth} года рождения.\n'
          f'Проживает в городе {city} Имэйл: {email} Телефон: {tel}')


data_dict = {
    'ваше имя: ': 'name',
    'вашу фамилия: ': 'surname',
    'ваш год рождения: ': 'year_of_birth',
    'ваш город проживания: ': 'city',
    'ваш имэйл: ': 'email',
    'ваш телефон: ': 'tel'
}
user_dict = {}
for key in data_dict:
    if data_dict.get(key) == 'year_of_birth':
        user_dict[data_dict.get(key)] = input(f'Введите {key}')
        user_dict.update({data_dict.get(key): check(user_dict[data_dict.get(key)], key)})
        continue
    user_dict[data_dict.get(key)] = input(f'Введите {key}')
user_data(**user_dict)


