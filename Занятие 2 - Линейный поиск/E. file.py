import os

f = open('input.txt', 'r')
n = 0
berries_up = []
up_len = 0
berries_down = []
down_len = 0
counter = 1
for line in f:
    if n == 0:
        n = int(line)
    else:
        x, y = map(int, line.split())
        if x - y > 0:
            up_len += 1
            if not berries_up:
                berries_up.append((counter, (x, x - y, y)))
            else:
                if y > berries_up[-1][1][2]:
                    berries_up.append((counter, (x, x - y, y)))
                else:
                    berries_up.insert(-2, (counter, (x, x - y, y)))
            counter += 1
        else:
            down_len += 1
            if not berries_down:
                berries_down.append((counter, (x, x - y, y)))
            else:
                if x > berries_down[0][1][0]:
                    berries_down.insert(0, (counter, (x, x - y, y)))
                else:
                    berries_down.append((counter, (x, x - y, y)))
            counter += 1

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

