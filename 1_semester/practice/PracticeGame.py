# n - число словарных слов
# first - первое слово искомой цепочки
# last - последнее слово искомой цепочки
# words - список словарных слов (без первого)
# result - список слов искомой цепочки
# now - текущий список слов
# word - последнее слово в текущем списке слов
# cnt - число различных букв в словах на одинаковых позициях

# Функция, перебирающая все возможные цепочки слов и выбирающая наименьшую подходящую
def words_search(word):
    # Переданное слово - последнее слово искомой цепочки
    if (word == last):
        # Текущая последовательность наименьшая из найденных ранее или первая
        if (len(now) < len(result) or len(result) == 0):
            result[:] = now[:]
    else:
        # Проверяем все словарные слова
        for w in words:
            # Такого слова еще нет в текущем списке и оно подходит
            if (w not in now) and (is_next(word, w)):
                now.append(w)  # Добавляем слово в текущий список
                words_search(w)  # Перебор всех возможных цепочек с новым словом в конце
                now.remove(w)  # Удаление слова из текущего списка после всех переборов

# Функция, проверяющая может ли второе переданное слово следовать после первого слова
def is_next(first, second):
    cnt = 0
    # Перебор всех букв в словах
    for j in range(len(first)):
        # Две буквы на одной позиции различны
        if first[j] != second[j]:
            cnt += 1
        # В словах не более одной различной буквы на одинаковых позициях
        if cnt <= 1:
            pass
        else:
            break

    # Второе слово может следовать после первого
    if cnt == 1:
        return True
    # Второе слово не может следовать после первого
    else:
        return False


n = int(input())
first = input()
words = []
# Считываем n - 1 словарное слово
for i in range(n - 1):
    words.append(input())
last = words[0]

result = []
# Любая цепочка начинается с первого слова искомой
now = [first]
# Перебор всех возможных цепочек, начинающихся с первого слова искомой цепочки, и выбор минимальной
words_search(first)

print(len(result))  # Вывод длины искомой цепочки
# Вывод слов искомой цепочки
for x in result:
    print(x)
