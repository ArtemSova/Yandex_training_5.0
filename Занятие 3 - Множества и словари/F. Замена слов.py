my_dict = list(map(str, input().split()))
words = list(map(str, input().split()))
my_dict.sort(key = lambda t: len(t))  # остсорт по неубыван длины строки

for r in range(len(my_dict)-1, 0, -1):   # цикл идет с конца, чтобы не потерять индексы
    if my_dict[r].startswith(my_dict[r-1]):
        my_dict.pop(r)

new_dict = {}

for i in my_dict:  # хэш-таблица
    first = i[0]
    if first in new_dict:
        new_dict[first] += [i]
    else:
        new_dict[first] = [i]

for j in range(len(words)):
    start = words[j][0]
    if start in new_dict:
        for k in new_dict[start]:
            if words[j].startswith(k):
                words[j] = k
                break

print(*words)

