# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def check(a):
    while True:
        for el in a:
            print(el)
            if not el.isalpha() or not el.isalnum():
                print('Ошибка ввода')
                a = input('Слова через пробел в нижнем регистре: ').split(' ')
            continue
        break
    return a


def word_upper(words):
    for i in range(len(words)):
        words[i] = list(words[i])
        words[i][0] = words[i][0].upper()
        words[i] = ''.join(words[i])
    print(' '.join(words))


user_word = input('Слова через пробел в нижнем регистре:  ').split(' ')
user_word = check(user_word)
word_upper(user_word)
