n = int(input())

berries_up = []
up_len = 0
berries_down = []
down_len = 0

for i in range(n):
    x, y = map(int, input().split())
    if x - y > 0:
        up_len += 1
        
        if not berries_up:
            berries_up.append((i+1, (x, x - y, y)))
        else:
            if y > berries_up[-1][1][2]:
                berries_up.append((i+1, (x, x - y, y)))
            else:
                berries_up.insert(-2, (i+1, (x, x - y, y)))
    else:
        down_len += 1
        
        if not berries_down:
            berries_down.append((i+1, (x, x - y, y)))
        else:
            if x > berries_down[0][1][0]:
                berries_down.insert(0, (i+1, (x, x - y, y)))
            else:
                berries_down.append((i+1, (x, x - y, y)))
        
result = 0
answer = []

if up_len > 0:
    for i in range(up_len):
        answer.append(berries_up[i][0])
        if i < (up_len - 1):
            result += berries_up[i][1][1]
        else:
            result += berries_up[i][1][0]

if down_len > 0 :
    if up_len > 0:
        if berries_up[-1][1][2] < berries_down[0][1][0]:
            result = result - berries_up[-1][1][2] + berries_down[0][1][0]
    else:
        result += berries_down[0][1][0]

    for j in range(down_len):
        answer.append(berries_down[j][0])

print(result)
print(*answer)
