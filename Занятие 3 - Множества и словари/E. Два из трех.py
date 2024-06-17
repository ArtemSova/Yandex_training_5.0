from collections import Counter

n_1 = int(input())
list_1 = set(map(int, input().split()))
n_2 = int(input())
list_2 = set(map(int, input().split()))
n_3 = int(input())
list_3 = set(map(int, input().split()))

my_dict = Counter(list_1)

for i in list_2:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

for j in list_3:
    if j in my_dict:
        my_dict[j] += 1

answer = []
for d in my_dict:
    if my_dict[d] > 1:
        answer.append(d)

answer.sort()

print(*answer)

