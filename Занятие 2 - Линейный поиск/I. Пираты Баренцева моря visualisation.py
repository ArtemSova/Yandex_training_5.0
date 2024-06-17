from collections import deque
n = int(input())

field = [] # игровое поле
columns = [] #колонны с кораблями
side_queue = deque() # двусторон очередь для распределения ходов (сверху-снизу-сверху и т.д.)

answer = 0

for i in range(1, (n+1)):   # заполняем двустороннюю очередь
    side_queue.append(i)

for f in range(n+2):      # заполняем поле (n+2)*(n+2), границы поля +, пустые яч-ки 0
    if f == 0 or f == n+1:
        field.append(['+']*(n+2))
    else:
        field.append(['+'] + [0]*n + ['+'])

for _ in range(n):      # наносим на поле корабли как #
    x, y = map(int, input().split())
    columns.append(y)
    field[x][y] = '#'

for f in field:
    print(f)

columns.sort()
column = int((columns[n//2] + columns[~(n//2)])/2)   # медиана, для подсчета оптимальной центральной колонны
print('COLUMN = ', column)
side = 'left'
while side_queue:           # двигаем корабли к нужной колонне
    if side == 'left':
        print('POPLEFT')
        i = side_queue.popleft()
        course = 0
        print(i)
        side = 'right'
    else:
        print('POP')
        i = side_queue.pop()
        course = n
        print(i)
        side = 'left'
    print('I =', i, '++++++++++++++++++++++++++++++++')
    for j in range(column-1, 0, -1):  #обраб поля слева от колонны, справа-налево
        print('-------------------------------------------------')
        print('LEFTSIDE', (i, j), 'ANSWER = ', answer)
        for f in field:
            print(f)
        if field[i][j] == '#':
            marker = j
            cnt_j = 1
            

            print('STEPS', 'MARKER = ', marker, 'CNT_J =', cnt_j)
            while field[i][marker+cnt_j] == 0 and (marker+cnt_j) <= column: # ведем корабль до колонны
                print('STEP_1')

                cnt_j += 1
            else:
                print('ANSWER = ', answer, '+', (cnt_j-1))
                answer += (cnt_j-1)
                print(field[i][marker], (i, marker), '==>', field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1))
                field[i][marker] = 0
                field[i][marker + cnt_j - 1] = '#'
                print(field[i][marker], (i, marker), '==>', field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1))

            print('STEP_2')
            if (marker+cnt_j-1) < column:    # если уперлись в корабль
                if course == n:  # ближайшая граница поля n(внизу, выше по индексуs)
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:  # ищем где ближе пустая ячейка (сверху или снизу)
                        if i+cnt_i_up <= n:
                            print('HERE')
                            if field[i+cnt_i_up][marker+cnt_j] == 0: # двигаем корабли в колонне к ближайшей пустой ячейке
                                print('HERE_2')
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i+cnt_i_up][marker+cnt_j], (i+cnt_i_up, marker+cnt_j))
                                field[i+cnt_i_up][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i+cnt_i_up][marker+cnt_j], (i+cnt_i_up, marker+cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i+1)
                                answer += (cnt_i_up+1)
                                break
                            else:
                                cnt_i_up += 1

                        elif i-cnt_i_down >= 1:
                            print('THERE')
                            if field[i-cnt_i_down][marker+cnt_j] == 0: # двигаем корабли в колонне к ближайшей пустой ячейке
                                print('THERE_2')
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i-cnt_i_down][marker+cnt_j], (i-cnt_i, marker+cnt_j))
                                field[i-cnt_i_down][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i-cnt_i_down][marker+cnt_j], (i-cnt_i, marker+cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i+1)
                                answer += (cnt_i_down+1)
                                break
                            else:
                                cnt_i_down += 1
                else:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i-cnt_i_down >= 1:
                            print('THERE')
                            if field[i-cnt_i_down][marker+cnt_j] == 0:
                                print('THERE_2')
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i-cnt_i_down][marker+cnt_j], (i-cnt_i_down, marker+cnt_j))
                                field[i-cnt_i_down][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i-cnt_i_down][marker+cnt_j], (i-cnt_i_down, marker+cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_down+1)
                                answer += (cnt_i_down+1)
                                break
                            else:
                                cnt_i_down += 1

                        elif i+cnt_i_up <= n:
                            print('HERE')
                            if field[i+cnt_i_up][marker+cnt_j] == 0:
                                print('HERE_2')
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i+cnt_i_up][marker+cnt_j], (i+cnt_i_up, marker+cnt_j))
                                field[i+cnt_i_up][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                print(field[i][marker + cnt_j - 1], (i, marker + cnt_j - 1), '==>', field[i+cnt_i_up][marker+cnt_j], (i+cnt_i_up, marker+cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_up+1)
                                answer += (cnt_i_up+1)
                                break
                            else:
                                cnt_i_up += 1
                        



    for j in range(column+1, n+1): # обраб поле справа от колонны, слева-направо
        print('-------------------------------------------------')
        print('RIGHTSIDE', (i, j), 'ANSWER = ', answer)
        for f in field:
            print(f)
        print('FIELD -', field[i][j])
        if field[i][j] == '#':
            marker = j
            cnt_j = 1

            print('STEPS', 'MARKER = ', marker, 'CNT_J =', cnt_j)
            while field[i][marker-cnt_j] == 0 and (marker-cnt_j) >= column:
                print('STEP_1')

                cnt_j += 1
            else:
                print('ANSWER = ', answer, '+', (cnt_j - 1))
                answer += (cnt_j - 1)
                print(field[i][marker], (i, marker), '==>', field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1))
                field[i][marker] = 0
                field[i][marker - cnt_j + 1] = '#'
                print(field[i][marker], (i, marker), '==>', field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1))

            if (marker - cnt_j + 1) > column:
                print('STEP_2')
                if course == n:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i + cnt_i_up <= n:
                            print('HERE')
                            if field[i + cnt_i_up][marker - cnt_j] == 0:
                                print('HERE_2')
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i + cnt_i_up][marker - cnt_j], (i + cnt_i_up, marker - cnt_j))
                                field[i + cnt_i_up][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                print(field[i][marker - cnt_j + 1], (i, marker + cnt_j - 1), '==>', field[i + cnt_i_up][marker - cnt_j], (i + cnt_i_up, marker - cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_up + 1)
                                answer += (cnt_i_up + 1)
                                break
                            else:
                                cnt_i_up += 1

                        elif i - cnt_i_down >= 1:
                            print('THERE')
                            if field[i - cnt_i_down][marker - cnt_j] == 0:
                                print('THERE_2')
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i - cnt_i_down][marker - cnt_j], (i - cnt_i_down, marker - cnt_j))
                                field[i - cnt_i_down][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i - cnt_i_down][marker - cnt_j], (i - cnt_i_down, marker - cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_down + 1)
                                answer += (cnt_i_down + 1)
                                break
                            else:
                                cnt_i_down += 1
                else:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i - cnt_i_down >= 1:
                            print('THERE')
                            if field[i - cnt_i_down][marker - cnt_j] == 0:
                                print('THERE_2')
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i - cnt_i_down][marker - cnt_j], (i - cnt_i_down, marker - cnt_j))
                                field[i - cnt_i_down][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i - cnt_i_down][marker - cnt_j], (i - cnt_i_down, marker - cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_down + 1)
                                answer += (cnt_i_down + 1)
                                break
                            else:
                                cnt_i_down += 1

                        elif i + cnt_i_up <= n:
                            print('HERE')
                            if field[i + cnt_i_up][marker - cnt_j] == 0:
                                print('HERE_2')
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i + cnt_i_up][marker - cnt_j], (i + cnt_i_up, marker - cnt_j))
                                field[i + cnt_i_up][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                print(field[i][marker - cnt_j + 1], (i, marker - cnt_j + 1), '==>', field[i + cnt_i_up][marker - cnt_j], (i + cnt_i_up, marker - cnt_j))
                                print('ANSWER = ', answer, '+', cnt_i_up + 1)
                                answer += (cnt_i_up + 1)
                                break
                            else:
                                cnt_i_up += 1



print('ANSWER ==', answer)

for f in field:
    print(f)

