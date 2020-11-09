number = int(input('Введите трёхзначное целое положительное число: '))
print(number % 10 + number // 100 + (number // 10) % 10)
