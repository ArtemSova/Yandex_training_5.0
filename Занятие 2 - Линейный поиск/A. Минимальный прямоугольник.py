k = int(input())

x_list = set()
y_list = set()

for _ in range(k):
    x, y = map(int, input().split())
    
    x_list.add(x)
    y_list.add(y)

print(min(x_list), min(y_list), max(x_list), max(y_list))

