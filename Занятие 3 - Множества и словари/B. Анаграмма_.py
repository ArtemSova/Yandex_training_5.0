first = str(input())
second = str(input())

dict_1 = {}
for i in first:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

dict_2 = {}
for j in second:
    if j in dict_2:
        dict_2[j] += 1
    else:
        dict_2[j] = 1

if dict_1 == dict_2:
    print('YES')
else:
    print('NO')
