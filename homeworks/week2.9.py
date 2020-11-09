a1, b1, c1 = int(input('Введите стороны 1вой коробки')), int(input('Введите стороны 1вой коробки')), \
             int(input('Введите стороны 1вой коробки'))
a2, b2, c2 = int(input('Введите стороны 2ро коробки')), int(input('Введите стороны 2ро коробки')), \
             int(input('Введите стороны 2ро коробки'))
if a1 > b1:
    a1, b1 = b1, a1
if a1 > c1:
    a1, c1 = c1, a1
if b1 > c1:
    b1, c1 = c1, b1
if a2 > b2:
    a2, b2 = b2, a2
if a2 > c2:
    a2, c2 = c2, a2
if b2 > c2:
    b2, c2 = c2, b2
a = (a1 - a2)
b = (b1 - b2)
c = (c1 - c2)
if a == b == c == 0:
    print('Boxes are equal')
elif a <= 0 and b <= 0 and c <= 0:
    print('The first box is smaller than the second one')
elif a >= 0 and b >= 0 and c >= 0:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
