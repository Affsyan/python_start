number = int(input('Введите колличество коров: '))

if (10 < number < 20) or (number % 10 in [0, 5, 6, 7, 8, 9]):
    print(number, "korov")
elif number % 10 == 1:
    print(number, "korova")
else:
    print(number, "korovy")
