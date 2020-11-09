a = int(input('Введите ширину кирпича: '))
b = int(input('Введите высоту кирпича: '))
c = int(input('Введите глубину кирпича: '))
d = int(input('Введите высоту отверстия: '))
e = int(input('Введите ширину отверстия: '))
if (a <= e and b <= d) or (a <= d and b <= e):
    print('YES')
elif (c <= e and b <= d) or (c <= d and b <= e):
    print('YES')
else:
    print('NO')
