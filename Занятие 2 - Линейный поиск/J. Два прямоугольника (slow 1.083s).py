picture = []
answer = []

# создаем поле картины с пустотой в качестве рамки
n, m = map(int, input().split())
picture.append('.' * (m+2))
for _ in range(n):
    line = str(input())
    picture.append('.' + line + '.')
    answer.append(list(line))
picture.append('.' * (m+2))

used_coord = set()
a = False

for_answer = []

for i in range(1, n+1):
    start = (0, 0)
    right = (0, 0)
    finish = (0, 0)
    for j in range(1, m+1):
        if picture[i][j] == '#' and (i, j) not in used_coord:
            if not a:
                a = True
            else:
                a = False

            start = right = finish = (i, j)
            used_coord.add((i, j))

            if a:
                answer[i-1][j-1] = 'a'
            else:
                answer[i-1][j-1] = 'b'

            for t in range(i, n+1):
                if t - finish[0] <= 1:
                    for u in range(j, m+1):
                        if u - right[1] <= 1:
                            if picture[t][u] == '#':
                                if t == start[0] and picture[t][u] == '#' and t - right[0] <= 1 and (t, u) not in used_coord:
                                    right = finish = (t, u)
                                    used_coord.add((t, u))
                                    if a:
                                        answer[t-1][u-1] = 'a'
                                    else:
                                        answer[t-1][u-1] = 'b'
                                elif t != start[0]:
                                    if picture[t][start[1]] == '#' and picture[t][right[1]] == '#':
                                        if picture[t][start[1]-1] == '#' and picture[t][right[1]+1] == '#':
                                            break
                                        else:
                                            try_list = set()
                                            try_list.add((t, start[1]))
                                            try_list.add((t, right[1]))
                                            for z in range(start[1]+1, right[1]):
                                                if picture[t][z] == '#':
                                                    try_list.add((t, z))
                                                else:
                                                    break
                                            else:
                                                for tl in try_list:
                                                    used_coord.add((tl[0], tl[1]))
                                                    if a:
                                                        answer[tl[0]-1][tl[1]-1] = 'a'
                                                    else:
                                                        answer[tl[0]-1][tl[1]-1] = 'b'
                                                        
                                                finish = (t, right[1])
                                                
            if start != (0, 0) and finish != (0, 0):
                for_answer.append([start, finish])

length = len(for_answer)
if length == 1:
    if for_answer[0][0][0] == for_answer[0][1][0] or for_answer[0][0][1] == for_answer[0][1][1]:
        answer[for_answer[0][0][0]-1][for_answer[0][0][1]-1] = 'b'
    elif for_answer[0][0][0] != for_answer[0][1][0] or for_answer[0][0][1] != for_answer[0][1][1]:
        y = for_answer[0][0][0]-1
        for z in range(for_answer[0][0][1], for_answer[0][1][1]+1):
            answer[y][z-1] = 'b'

if length == 2:
    print('YES')
    for ans in answer:
        print(''.join(ans))
elif length == 1:
    if for_answer[0][0][0] == for_answer[0][1][0] and for_answer[0][0][1] == for_answer[0][1][1]:
        print('NO')
    else:
        print('YES')
        for ans in answer:
            print(''.join(ans))
else:
    print('NO')

