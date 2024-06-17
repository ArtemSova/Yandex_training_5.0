n, k = map(int, input().split())
my_list = list(map(int, input().split()))

max_value = 0

for i in range(n-1, 0, -1):
    for j in range(k, 0, -1):
        if (i-j) >= 0:
            if my_list[i] - my_list[i-j] > max_value:
                max_value = my_list[i] - my_list[i-j]

print(max_value)        
