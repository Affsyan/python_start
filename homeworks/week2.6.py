a, b, c = int(input('Введите число A: ')), int(input('Введите число B: ')), int(input('Введите число C: '))
if b > c:
    (b, c) = (c, b)
if a > c:
    (a, c) = (c, a)
if a > b:
    (a, b) = (b, a)
print(a, b, c)