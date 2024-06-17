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
for_answer = []

first = second = first_stop = second_stop = third = False

start_1 = right_1 = left_1 = left_2 = finish_1 = start_2 = right_2 = finish_2 = (0, 0)
for i in range(1, n+1):
    start = finish = 0
    if third == False:
        for j in range(1, m+1):
            if picture[i][j] == '#':
                if not first:
                    start_1 = left_1 = right_1 = finish_1 = (i, j)
                    answer[i-1][j-1] = 'a'
                    first = True
                elif first_stop and second_stop:
                    third = True
                    break
                elif first and not first_stop:
                    if i == start_1[0]:
                        if j - right_1[1] <= 1:
                            right_1 = finish_1 = (i, j)
                            answer[i-1][j-1] = 'a'
                        elif not second:
                            second = True
                            start_2 = left_2 = right_2 = finish_2 = (i, j)
                            answer[i-1][j-1] = 'b'
                        elif second and not second_stop:
                            if i == start_2[0]:
                                if j - right_1[1] <= 1:
                                    right_2 = finish_2 = (i, j)
                                    answer[i-1][j-1] = 'b'
                                else:
                                    if first and not first_stop:
                                        first_stop = True
                                        for_answer.append([start_1, finish_1])
                                    if second and not second_stop:
                                        second_stop = True
                                        for_answer.append([start_2, finish_2])
                                    third = True
                                    break
                    elif i != start_1[0]:
                        if not first_stop:
                            if j == left_1[1]:
                                if picture[i][right_1[1]] == "#":
                                    if picture[i][j-1] == '.' or picture[i][right_1[1]+1] == '.' or picture[i][j-1] == '.' and picture[i][right_1[1]+1] == '.':
                                        left_1 = (i, j)
                                        finish_1 = (i, right_1[1])
                                        answer[i-1][j-1] = 'a'
                                    elif picture[i][j-1] == '#' and picture[i][right_1[1]+1] == '#':
                                        for_answer.append([start_1, finish_1])
                                        first_stop = True
                                        if not second:
                                            second = True
                                            start_2 = right_2 = left_2 = finish_2 = (i, j)
                                            answer[i-1][j-1] = 'b'
                                        else:
                                            if j == start_2[1]:
                                                if picture[i][right_2[1]] == "#":
                                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                        left_2 = (i, j)
                                                        finish_2 = (i, right_2[1])
                                                        answer[i-1][j-1] = 'b'
                                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                        for_answer.append([start_2, finish_2])
                                                        second_stop = True
                                            elif i == start_2[0] and j - right_2[1] <= 1:
                                                right_2 = finish_2 = (i, j)
                                                answer[i-1][j-1] = 'b'
                                            elif j < start_2[1]:
                                                if second and not second_stop:
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                            elif j > finish_2[1]:
                                                if second and not second_stop:
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                            elif i == left_2[0] and j > start_2[1] and j <= finish_2[1]:
                                                answer[i-1][j-1] = 'b'
                                                
                                else:
                                    for_answer.append([start_1, finish_1])
                                    first_stop = True
                                    if not second:
                                        second = True
                                        start_2 = right_2 = left_2 = finish_2 = (i, j)
                                        answer[i-1][j-1] = 'b'
                                    else:
                                        if not second_stop:
                                            if j == start_2[1]:
                                                if picture[i][right_2[1]] == "#":
                                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                        left_2 = (i, j)
                                                        finish_2 = (i, right_2[1])
                                                        answer[i-1][j-1] = 'b'
                                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                        for_answer.append([start_2, finish_2])
                                                        second_stop = True 
                                            else:
                                                if i == start_2[0]:
                                                    if j - right_2[1] <= 1:
                                                        right_2 = finish_2 = (i, j)
                                                        answer[i-1][j-1] = 'b'
                                                    else:
                                                        if first and not first_stop:
                                                            first_stop = True
                                                            for_answer.append([start_1, finish_1])
                                                        if second and not second_stop:
                                                            second_stop = True
                                                            for_answer.append([start_2, finish_2])
                                                        third = True
                                                        break
                                                if start_2[1] < j:
                                                    if j <= right_2[1]:
                                                        answer[i-1][j-1] = 'b'
                                                    else:
                                                        if first and not first_stop:
                                                            first_stop = True
                                                            for_answer.append([start_1, finish_1])
                                                        if second and not second_stop:
                                                            second_stop = True
                                                            for_answer.append([start_2, finish_2])
                                                        third = True
                                                        break 
                                        else:
                                            third = True
                                            break
                            elif j < left_1[1]:
                                if not second:
                                    second = True
                                    start_2 = right_2 = left_2 = finish_2 = (i, j)
                                    answer[i-1][j-1] = 'b'
                                else:
                                    if not second_stop:
                                        if j == start_2[1]:
                                            if picture[i][right_2[1]] == "#":
                                                if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                    left_2 = (i, j)
                                                    finish_2 = (i, right_2[1])
                                                    answer[i-1][j-1] = 'b'
                                                elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                    for_answer.append([start_2, finish_2])
                                                    second_stop = True
                                        else:
                                            if i == start_2[0]:
                                                if j - right_2[1] <= 1:
                                                    right_2 = finish_2 = (i, j)
                                                    answer[i-1][j-1] = 'b'
                                            if start_2[1] < j:
                                                if j <= right_2[1]:
                                                    answer[i-1][j-1] = 'b'
                                                else:
                                                    if first and not first_stop:
                                                        first_stop = True
                                                        for_answer.append([start_1, finish_1])
                                                    if second and not second_stop:
                                                        second_stop = True
                                                        for_answer.append([start_2, finish_2])
                                                    third = True
                                                    break
                            elif left_1[1] <= j <= finish_1[1]:
                                answer[i-1][j-1] = 'a'
                            elif j > right_1[1]:
                                if not second:
                                    second = True
                                    start_2 = right_2 = left_2 = finish_2 = (i, j)
                                    answer[i-1][j-1] = 'b'
                                else:
                                    if not second_stop:
                                        if i == start_2[0]:
                                            if j - right_2[1] <= 1:
                                                right_2 = finish_2 = (i, j)
                                                answer[i-1][j-1] = 'b'
                                        if j == start_2[1]:
                                            if picture[i][right_2[1]] == "#":
                                                if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                    left_2 = (i, j)
                                                    finish_2 = (i, right_2[1])
                                                    answer[i-1][j-1] = 'b'
                                                elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                    for_answer.append([start_2, finish_2])
                                                    second_stop = True
                                        else:
                                            if start_2[1] < j:
                                                if j <= right_2[1]:
                                                    answer[i-1][j-1] = 'b'
                                                else:
                                                    if first and not first_stop:
                                                        first_stop = True
                                                        for_answer.append([start_1, finish_1])
                                                    if second and not second_stop:
                                                        second_stop = True
                                                        for_answer.append([start_2, finish_2])
                                                    third = True
                                                    break
                        else:
                            if not second:
                                second = True
                                start_2 = right_2 = left_2 = finish_2 = (i, j)
                                answer[i-1][j-1] = 'b'
                            else:
                                if not second_stop:
                                    if j == start_2[1]:
                                        if picture[i][right_2[1]] == "#":
                                            if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                left_2 = (i, j)
                                                finish_2 = (i, right_2[1])
                                                answer[i-1][j-1] = 'b'
                                            elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                for_answer.append([start_2, finish_2])
                                                second_stop = True
                                    else:
                                        if start_2[1] < j:
                                            if j <= right_2[1]:
                                                answer[i-1][j-1] = 'b'
                                            else:
                                                if first and not first_stop:
                                                    first_stop = True
                                                    for_answer.append([start_1, finish_1])
                                                if second and not second_stop:
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                                third = True
                                                break
                                
                elif first_stop:
                    if second and not second_stop:
                        if i == start_2[0]:
                            if j - right_2[1] <= 1:
                                right_2 = finish_2 = (i, j)
                                answer[i-1][j-1] = 'b'
                            else:
                                if first and not first_stop:
                                    first_stop = True
                                    for_answer.append([start_1, finish_1])
                                if second and not second_stop:
                                    second_stop = True
                                    for_answer.append([start_2, finish_2])
                                third = True
                                break
                        else:
                            if i == start_2[0]:
                                if j - right_2[1] <= 1:
                                    right_2 = finish_2 = (i, j)
                                    answer[i-1][j-1] = 'b'
                            elif j == left_2[1]:
                                if picture[i][right_2[1]] == "#":
                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.' or picture[i][j-1] == '.' and picture[i][right_2[1]+1] == '.':
                                        left_2 = (i, j)
                                        finish_2 = (i, right_2[1])
                                        answer[i-1][j-1] = 'b'
                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                        for_answer.append([start_2, finish_2])
                                        second_stop = True
                            elif i == left_2[0]:
                                if j >left_2[1] and j <= finish_2[1]:
                                    answer[i-1][j-1] = 'b'
                            elif j < start_2[1] or j > right_2[0]:
                                third = True
                                break
                    elif not second:
                        second = True
                        start_2 = right_2 = left_2 = finish_2 = (i, j)
                        answer[i-1][j-1] = 'b'
                        

            else:
                if i == left_1[0] and j > left_1[1] and j < finish_1[1] and first and not first_stop:
                    for_answer.append([start_1, finish_1])
                    first_stop = True
                    third = True
                    break
                elif i == left_2[0] and j > left_2[1] and j < finish_2[1] and second and not second_stop:
                    for_answer.append([start_2, finish_2])
                    second_stop = True
                    third = True
                    break
                elif i != left_1[0] and j >= left_1[1] and j <= finish_1[1] and first and not first_stop:
                    first_stop = True
                    for_answer.append([start_1, finish_1])
                elif i == left_2[0] and j > left_2[1] and j < finish_2[1] and second and not second_stop:
                    second_stop = True
                    for_answer.append([start_2, finish_2])
                    
else:
    if first and not first_stop:
        first_stop = True
        for_answer.append([start_1, finish_1])
    if second and not second_stop:
        second_stop = True
        for_answer.append([start_2, finish_2])

length = len(for_answer)
if length == 1:
    if for_answer[0][0][0] == for_answer[0][1][0] or for_answer[0][0][1] == for_answer[0][1][1]:
        answer[for_answer[0][0][0]-1][for_answer[0][0][1]-1] = 'b'
    elif for_answer[0][0][0] != for_answer[0][1][0] or for_answer[0][0][1] != for_answer[0][1][1]:
        y = for_answer[0][0][0]-1
        for z in range(for_answer[0][0][1], for_answer[0][1][1]+1):
            answer[y][z-1] = 'b'

if not third:
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
else:
    print('NO')
