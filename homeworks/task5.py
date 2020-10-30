# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2, 1, 8, 3, 11, 9, 3, 3]
print(rating)
while True:
    rating_elem = input('Введите новый элемент рейтинга: ')
    if rating_elem.isdigit():
        rating_elem = int(rating_elem)
        break
    print('Введите целое натуральное число')
repeat_elem = []
if rating_elem in rating:
    for i in range(len(rating)):
        if rating_elem in rating[i:i+1]:
            repeat_elem.append(rating.index(rating_elem, i,))
else:
    rating.append(rating_elem)
count = 0
if len(repeat_elem) > 0:
    for i in repeat_elem:
        rating.insert(i + count, rating_elem)
        count += 1
print(rating)
