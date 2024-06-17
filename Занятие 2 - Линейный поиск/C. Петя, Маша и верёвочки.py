n = int(input())
my_list = list(map(int, input().split()))

full = max(my_list)
my_list.remove(full)

if full > sum(my_list):
    print(full - sum(my_list))
else:
    print(full + sum(my_list))
