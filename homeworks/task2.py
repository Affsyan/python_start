# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

test = open('task1.txt', 'r')
strings = 0
word = 0

for i in test:
    strings += 1
    count = 0
    for j in i:
        if j != ' ' and count == 0:
            word += 1
            count = 1
        elif j == ' ':
            count = 0
print(f'В файле {strings} строк и {word} слов')
test.close()
