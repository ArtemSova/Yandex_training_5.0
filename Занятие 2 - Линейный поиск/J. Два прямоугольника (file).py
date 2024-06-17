picture = []
answer = []

# создаем поле картины с пустотой в качестве рамки

with open('J117.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    
    picture.append('.' * (m+2))
    for _ in range(n):
        line = str(file.readline().strip())
        print(line)
        picture.append('.' + line + '.')
        answer.append(list(line))
    picture.append('.' * (m+2))
'''
n, m = map(int, input().split())
picture.append('.' * (m+2))
for _ in range(n):
    line = str(input())
    picture.append('.' + line + '.')
    answer.append(list(line))
picture.append('.' * (m+2))
'''
used_coord = set()
print('ANSWER START', answer)
for_answer = []

first = second = first_stop = second_stop = third = False

start_1 = right_1 = left_1 = left_2 = finish_1 = start_2 = right_2 = finish_2 = (0, 0)
for i in range(1, n+1):
    start = finish = 0
    if third == False:
        for j in range(1, m+1):
            print('--------------------------------')
            print('COORDINATE = ', (i, j))
            print('THIRD = ', third)
            print('FOR_ANSWER =', for_answer)
            print('START_1 =', start_1, 'RIGHT_1', right_1, 'LEFT_1', left_1, 'FINISH_1', finish_1)
            print('START_2 =', start_2, 'RIGHT_2', right_2, 'LEFT_2', left_2, 'FINISH_2', finish_2)
            if picture[i][j] == '#':
                if not first:
                    print('FIRST NEW')
                    start_1 = left_1 = right_1 = finish_1 = (i, j)
                    print('PRINT A 1')
                    answer[i-1][j-1] = 'a'
                    first = True
                elif first_stop and second_stop:
                    print('BOTH STOP')
                    third = True
                    break
                elif first and not first_stop:
                    print('SILL FIRST')
                    if i == start_1[0]:
                        if j - right_1[1] <= 1:
                            right_1 = finish_1 = (i, j)
                            print('PRINT A 2')
                            answer[i-1][j-1] = 'a'
                        elif not second:
                            print('SECOND NEW IN FIRST LINE')
                            second = True
                            start_2 = left_2 = right_2 = finish_2 = (i, j)
                            print('PRINT B 1')
                            answer[i-1][j-1] = 'b'
                        elif second and not second_stop:
                            print('STILL SECOND IN FIRST LINE')
                            if i == start_2[0]:
                                if j - right_1[1] <= 1:
                                    right_2 = finish_2 = (i, j)
                                    print('PRINT B 2')
                                    answer[i-1][j-1] = 'b'
                                else:
                                    if first and not first_stop:
                                        print('ERROR 1 FIRST_STOP')
                                        first_stop = True
                                        for_answer.append([start_1, finish_1])
                                    if second and not second_stop:
                                        print("ERROR 1 SECOND_STOP")
                                        second_stop = True
                                        for_answer.append([start_2, finish_2])
                                    third = True
                                    break
                    elif i != start_1[0]:
                        print('I != START_1')
                        if not first_stop:
                            if j == left_1[1]:
                                print('IF STILL FIRST')
                                if picture[i][right_1[1]] == "#":
                                    print('FIRST START AND FIRST STOP')
                                    if picture[i][j-1] == '.' or picture[i][right_1[1]+1] == '.' or picture[i][j-1] == '.' and picture[i][right_1[1]+1] == '.':
                                        print('GOOD')
                                        left_1 = (i, j)
                                        finish_1 = (i, right_1[1])
                                        print('PRINT A 3')
                                        answer[i-1][j-1] = 'a'
                                    elif picture[i][j-1] == '#' and picture[i][right_1[1]+1] == '#':
                                        print('FIRST_STOP ##')
                                        for_answer.append([start_1, finish_1])
                                        first_stop = True
                                        if not second:
                                            print('SECOND_NEW AFTER FIRST STOP')
                                            second = True
                                            start_2 = right_2 = left_2 = finish_2 = (i, j)
                                            print('PRINT B 32')
                                            answer[i-1][j-1] = 'b'
                                        else:
                                            print('HAVE SECOND')
                                            if j == start_2[1]:
                                                print('J = START_2 AFTER FIRST_STOP')
                                                if picture[i][right_2[1]] == "#":
                                                    print('SECOND START AND STOP')
                                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                        print('GOOD')
                                                        left_2 = (i, j)
                                                        finish_2 = (i, right_2[1])
                                                        print('PRINT B 41')
                                                        answer[i-1][j-1] = 'b'
                                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                        print('SECOND STOP 2')
                                                        for_answer.append([start_2, finish_2])
                                                        second_stop = True
                                            elif i == start_2[0] and j - right_2[1] <= 1:
                                                right_2 = finish_2 = (i, j)
                                                print('PRINT B 42')
                                                answer[i-1][j-1] = 'b'
                                            elif j < start_2[1]:
                                                print('J < START_2')
                                                if second and not second_stop:
                                                    print("SECOND_STOP 3")
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                            elif j > finish_2[1]:
                                                print('AFTER SECOND RIGHT')
                                                if second and not second_stop:
                                                    print("SECOND_STOP 4")
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                            elif i == left_2[0] and j > start_2[1] and j <= finish_2[1]:
                                                print('BETWEEN SECOND LEFT-RIGHT')
                                                print('PRINT B 42')
                                                answer[i-1][j-1] = 'b'
                                                
                                else:
                                    print('FIRST_STOPED NOT ENAUGH')
                                    for_answer.append([start_1, finish_1])
                                    first_stop = True
                                    if not second:
                                        print('SECOND_NEW NOT FIRST LINE')
                                        second = True
                                        start_2 = right_2 = left_2 = finish_2 = (i, j)
                                        print('PRINT B 3')
                                        answer[i-1][j-1] = 'b'
                                    else:
                                        if not second_stop:
                                            print('STILL SECOND NOT FIRST LINE HERE')
                                            if j == start_2[1]:
                                                print('J = START_2')
                                                if picture[i][right_2[1]] == "#":
                                                    print('SECOND START AND STOP')
                                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                        print('GOOD')
                                                        left_2 = (i, j)
                                                        finish_2 = (i, right_2[1])
                                                        print('PRINT B 4')
                                                        answer[i-1][j-1] = 'b'
                                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                        print('BREAK SECOND STOP')
                                                        for_answer.append([start_2, finish_2])
                                                        second_stop = True 
                                            else:
                                                print('J NOT STARTER')
                                                if i == start_2[0]:
                                                    if j - right_2[1] <= 1:
                                                        right_2 = finish_2 = (i, j)
                                                        print('PRINT B 41')
                                                        answer[i-1][j-1] = 'b'
                                                    else:
                                                        print('FIRST STOPED, NOT SECOND, NEW SCUARE')
                                                        if first and not first_stop:
                                                            print('ERROR 13 FIRST_STOP')
                                                            first_stop = True
                                                            for_answer.append([start_1, finish_1])
                                                        if second and not second_stop:
                                                            print("ERROR 13 SECOND_STOP")
                                                            second_stop = True
                                                            for_answer.append([start_2, finish_2])
                                                        third = True
                                                        break
                                                if start_2[1] < j:
                                                    print('J > START_2')
                                                    if j <= right_2[1]:
                                                        print('J < RIGHT_2')
                                                        print('PRINT B 5')
                                                        answer[i-1][j-1] = 'b'
                                                    else:
                                                        print('J > RIGHT_2, BREAK')
                                                        if first and not first_stop:
                                                            print('ERROR 2 FIRST_STOP')
                                                            first_stop = True
                                                            for_answer.append([start_1, finish_1])
                                                        if second and not second_stop:
                                                            print("ERROR 2 SECOND_STOP")
                                                            second_stop = True
                                                            for_answer.append([start_2, finish_2])
                                                        third = True
                                                        break 
                                        else:
                                            print('FIRST_LEFT NOT #, SECOND_STOP, BREAK')
                                            third = True
                                            break
                            elif j < left_1[1]:
                                if not second:
                                    print('SECOND_NEW NOT FIRST LINE BEFOR FIRS')
                                    second = True
                                    start_2 = right_2 = left_2 = finish_2 = (i, j)
                                    print('PRINT B 31')
                                    answer[i-1][j-1] = 'b'
                                else:
                                    if not second_stop:
                                        print('STILL SECOND NOT FIRST LINE THERE')
                                        if j == start_2[1]:
                                            print('J = START_2')
                                            if picture[i][right_2[1]] == "#":
                                                print('SECOND START AND STOP')
                                                if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                    print('GOOD')
                                                    left_2 = (i, j)
                                                    finish_2 = (i, right_2[1])
                                                    print('PRINT B 4')
                                                    answer[i-1][j-1] = 'b'
                                                elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                    print('BREAK SECOND STOP')
                                                    for_answer.append([start_2, finish_2])
                                                    second_stop = True
                                        else:
                                            print('J NOT STARTER')
                                            if i == start_2[0]:
                                                print('START_2 LINE')
                                                if j - right_2[1] <= 1:
                                                    print('MOVE RIGHT_2')
                                                    right_2 = finish_2 = (i, j)
                                                    print('PRINT B 45')
                                                    answer[i-1][j-1] = 'b'
                                            if start_2[1] < j:
                                                print('J > START_2')
                                                if j <= right_2[1]:
                                                    print('J < RIGHT_2')
                                                    print('PRINT B 51')
                                                    answer[i-1][j-1] = 'b'
                                                else:
                                                    print('J > RIGHT_2, BREAK')
                                                    if first and not first_stop:
                                                        print('ERROR 21 FIRST_STOP')
                                                        first_stop = True
                                                        for_answer.append([start_1, finish_1])
                                                    if second and not second_stop:
                                                        print("ERROR 21 SECOND_STOP")
                                                        second_stop = True
                                                        for_answer.append([start_2, finish_2])
                                                    third = True
                                                    break
                            elif left_1[1] <= j <= finish_1[1]:
                                print('J BETWEEN FIRST BOARDS')
                                print('PRINT A 414')
                                answer[i-1][j-1] = 'a'
                            elif j > right_1[1]:
                                if not second:
                                    print('SECOND NEW OUTSIDE FIRST')
                                    second = True
                                    start_2 = right_2 = left_2 = finish_2 = (i, j)
                                    print('PRINT B 41')
                                    answer[i-1][j-1] = 'b'
                                else:
                                    print('STILL SECOND')
                                    if not second_stop:
                                        print('STILL SECOND OUTSIDE FIRST')
                                        if i == start_2[0]:
                                            if j - right_2[1] <= 1:
                                                print('MOVE RIGHT_2')
                                                right_2 = finish_2 = (i, j)
                                                print('PRINT B 52')
                                                answer[i-1][j-1] = 'b'
                                        if j == start_2[1]:
                                            print('J = START_2')
                                            if picture[i][right_2[1]] == "#":
                                                print('SECOND START AND STOP')
                                                if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                    print('GOOD')
                                                    left_2 = (i, j)
                                                    finish_2 = (i, right_2[1])
                                                    print('PRINT B 42')
                                                    answer[i-1][j-1] = 'b'
                                                elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                    print('BREAK SECOND STOP ##')
                                                    for_answer.append([start_2, finish_2])
                                                    second_stop = True
                                        else:
                                            print('J NOT STARTER 2')
                                            if start_2[1] < j:
                                                print('J > START_2')
                                                if j <= right_2[1]:
                                                    print('J <= RIGHT_2')
                                                    print('PRINT B 53')
                                                    answer[i-1][j-1] = 'b'
                                                else:
                                                    print('J > RIGHT_2, BREAK')
                                                    if first and not first_stop:
                                                        print('ERROR 21 FIRST_STOP')
                                                        first_stop = True
                                                        for_answer.append([start_1, finish_1])
                                                    if second and not second_stop:
                                                        print("ERROR 21 SECOND_STOP")
                                                        second_stop = True
                                                        for_answer.append([start_2, finish_2])
                                                    third = True
                                                    break
                                    
                                    
                                
                        else:
                            if not second:
                                print('SECOND_NEW NOT FIRST LINE BEFOR FIRTS')
                                second = True
                                start_2 = right_2 = left_2 = finish_2 = (i, j)
                                print('PRINT B 31')
                                answer[i-1][j-1] = 'b'
                            else:
                                if not second_stop:
                                    print('STILL SECOND NOT FIRST LINE')
                                    if j == start_2[1]:
                                        print('J = START_2')
                                        if picture[i][right_2[1]] == "#":
                                            print('SECOND START AND STOP')
                                            if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.':
                                                print('GOOD')
                                                left_2 = (i, j)
                                                finish_2 = (i, right_2[1])
                                                print('PRINT B 4')
                                                answer[i-1][j-1] = 'b'
                                            elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                                print('BREAK SECOND STOP ##')
                                                for_answer.append([start_2, finish_2])
                                                second_stop = True
                                    else:
                                        print('J NOT STARTER')
                                        if start_2[1] < j:
                                            print('J > START_2')
                                            if j <= right_2[1]:
                                                print('J < RIGHT_2')
                                                print('PRINT B 51')
                                                answer[i-1][j-1] = 'b'
                                            else:
                                                print('J > RIGHT_2, BREAK')
                                                if first and not first_stop:
                                                    print('ERROR 21 FIRST_STOP')
                                                    first_stop = True
                                                    for_answer.append([start_1, finish_1])
                                                if second and not second_stop:
                                                    print("ERROR 21 SECOND_STOP")
                                                    second_stop = True
                                                    for_answer.append([start_2, finish_2])
                                                third = True
                                                break
                                
                elif first_stop:
                    print('FIRST_STOPED')
                    if second and not second_stop:
                        print('SECOND READY')
                        if i == start_2[0]:
                            print('I = START_2')
                            if j - right_2[1] <= 1:
                                print('J MOOVING RIGHT')
                                right_2 = finish_2 = (i, j)
                                print('PRINT B 6')
                                answer[i-1][j-1] = 'b'
                            else:
                                print('BREAK THIRD SQUARE')
                                if first and not first_stop:
                                    print('ERROR 3 FIRST_STOP')
                                    first_stop = True
                                    for_answer.append([start_1, finish_1])
                                if second and not second_stop:
                                    print("ERROR 3 SECOND_STOP")
                                    second_stop = True
                                    for_answer.append([start_2, finish_2])
                                third = True
                                break
                        else:
                            print('NOT SECOND START J')
                            if i == start_2[0]:
                                print('SECOND_START LINE')
                                if j - right_2[1] <= 1:
                                    print('MOVE RIGHT_2')
                                    right_2 = finish_2 = (i, j)
                                    print('PRINT B 61')
                                    answer[i-1][j-1] = 'b'
                            elif j == left_2[1]:
                                if picture[i][right_2[1]] == "#":
                                    if picture[i][j-1] == '.' or picture[i][right_2[1]+1] == '.' or picture[i][j-1] == '.' and picture[i][right_2[1]+1] == '.':
                                        left_2 = (i, j)
                                        finish_2 = (i, right_2[1])
                                        print('PRINT B 7')
                                        answer[i-1][j-1] = 'b'
                                    elif picture[i][j-1] == '#' and picture[i][right_2[1]+1] == '#':
                                        print('SECOND_STOP')
                                        for_answer.append([start_2, finish_2])
                                        second_stop = True
                            elif i == left_2[0]:
                                print('NEW SECOND LINE')
                                if j >left_2[1] and j <= finish_2[1]:
                                    print('PRINT B 71')
                                    answer[i-1][j-1] = 'b'
                            elif j < start_2[1] or j > right_2[0]:
                                third = True
                                break
                    elif not second:
                        print('SECOND_NEW AFTER FIRST STOPED')
                        second = True
                        start_2 = right_2 = left_2 = finish_2 = (i, j)
                        print('PRINT B 31')
                        answer[i-1][j-1] = 'b'
                        

            else:
                print('.', 'CHECK')
                if i == left_1[0] and j > left_1[1] and j < finish_1[1] and first and not first_stop:
                    print('FIRST_STOPED "."')
                    for_answer.append([start_1, finish_1])
                    first_stop = True
                    third = True
                    break
                elif i == left_2[0] and j > left_2[1] and j < finish_2[1] and second and not second_stop:
                    print('SECOND_STOPED "."')
                    for_answer.append([start_2, finish_2])
                    second_stop = True
                    third = True
                    break
                elif i != left_1[0] and j >= left_1[1] and j <= finish_1[1] and first and not first_stop:
                    print('FIRST STOPED')
                    first_stop = True
                    for_answer.append([start_1, finish_1])
                elif i == left_2[0] and j > left_2[1] and j < finish_2[1] and second and not second_stop:
                    print('SECOND STOPED')
                    second_stop = True
                    for_answer.append([start_2, finish_2])
                    
else:
    print('CYCLE STOP')
    print('THIRD = ', third)
    if first and not first_stop:
        print('FIRST_STOP')
        first_stop = True
        for_answer.append([start_1, finish_1])
    if second and not second_stop:
        print("SECOND_STOP")
        second_stop = True
        for_answer.append([start_2, finish_2])
                

print('+++++++++++++++++++++++++++++++++++++++++++++')
print(for_answer)
print('THIRD = ', third)
print('AMSWER = ', answer)

length = len(for_answer)
if length == 1:
    if for_answer[0][0][0] == for_answer[0][1][0] or for_answer[0][0][1] == for_answer[0][1][1]:
        answer[for_answer[0][0][0]-1][for_answer[0][0][1]-1] = 'b'
    elif for_answer[0][0][0] != for_answer[0][1][0] or for_answer[0][0][1] != for_answer[0][1][1]:
        y = for_answer[0][0][0]-1
        for z in range(for_answer[0][0][1], for_answer[0][1][1]+1):
            answer[y][z-1] = 'b'
            
#print('AMSWER AFTER ONE = ', answer)

if not third:
    if length == 2:
        print('YES2')
        for ans in answer:
            print(''.join(ans))
    elif length == 1:
        if for_answer[0][0][0] == for_answer[0][1][0] and for_answer[0][0][1] == for_answer[0][1][1]:
            print('NO1')
            for ans in answer:
                print(''.join(ans))
        else:
            print('YES1')
            for ans in answer:
                print(''.join(ans))
    else:
        print('NO2')
        for ans in answer:
            print(''.join(ans))
else:
    print('NO3')
    for ans in answer:
        print(''.join(ans))

