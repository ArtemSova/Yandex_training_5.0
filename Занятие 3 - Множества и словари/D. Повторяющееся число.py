from collections import Counter

n, k = map(int, input().split())
my_list = list(map(int, input().split()))

my_dict = Counter(my_list[0:k+1])

if n == 1 or (n - k) < 0:
    print('NO')
elif len(my_dict) < k+1:
    print('YES')
else:
    for i in range(1, n-k):
        my_dict.pop(my_list[i-1])
        if my_list[i+k] in my_dict:
            print('YES')
            break
        else:
            my_dict[my_list[i+k]] = 1
    else:
        print('NO')

