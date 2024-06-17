#n = int(input())
#my_list = list(map(int, input().split()))

with open('input.txt', 'r') as file:
    n = int(file.readline())
    my_list = list(map(int, file.readline().split()))


my_dict = {}
counter = set()

for i in my_list:
    counter.add(i)
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

counter = sorted(counter)

if len(counter) == 1:
    print(0)
elif len(counter) == 2 and (counter[1] - counter[0]) > 1:
    print(min(my_dict.values()))
else:
    answer = 0
    for i in range(len(counter)-1):
        if (counter[i+1] - counter[i]) == 1:
            ans = my_dict[counter[i]] + my_dict[counter[i+1]]
            if ans > answer:
                answer = ans

    if max(my_dict.values()) > answer:
        answer = max(my_dict.values())
        
    print(n - answer)
