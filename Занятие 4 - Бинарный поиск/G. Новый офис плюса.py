field = []
max_length = 0

with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    for j in range(n):
        line = list(file.readline().strip())
        pre_list = []
        for i in range(m):
            if i != 0:
                if line[i] == '#':
                    pre_list.append(1 + pre_list[i-1])
                    if (1 + pre_list[i-1]) > max_length:
                        max_length = 1 + pre_list[i-1]
                else:
                    pre_list.append(0)
            else:
                if line[i] == '#':
                    pre_list.append(1)
                else:
                    pre_list.append(0)
                
        field.append(pre_list)

def func(mid):
    ystart = mid*2 - 1
    x = mid
    y = mid*2 - 1
    while x + mid*2 - 1 <= n-1 and y + mid <= m-1:
        if field[x][y+mid] >= mid*3 and field[x-mid][y] >= mid and field[x+mid*2-1][y] >= mid and field[x+mid][y] >= mid:
            if mid == 1:
                return True
            else:
                for j in range(mid-1, 0, -1):
                    if field[x-j][y] >= mid and field[x+mid+j][y] >= mid and field[x+j][y+mid] >= mid*3:
                        pass
                    else:
                        if y + 1 + mid <= m-1:
                            y += 1
                        else:
                            y = ystart
                            x += 1
                        break
                else:
                    return True
        else:
            if y + 1 + mid <= m-1:
                y += 1
            else:
                y = ystart
                x += 1

    return False

answer = 0

left = 0
right = max_length//3*2
while left < right:
    middle = (left + right)//2
    if func(middle):
        if middle > answer:
            answer = middle
        left = middle+1
    else:
        right = middle

print(answer)
