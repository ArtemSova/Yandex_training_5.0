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

columns.sort()
column = int((columns[n//2] + columns[~(n//2)])/2)   # медиана, для подсчета оптимальной центральной колонны

side = 'left'
while side_queue:           # двигаем корабли к нужной колонне
    if side == 'left':
        i = side_queue.popleft()
        course = 0          # курс к ближайшей границе(верхней-нижней)
        side = 'right'
    else:
        i = side_queue.pop()
        course = n
        side = 'left'
    for j in range(column-1, 0, -1):  #обраб поля слева от колонны, справа-налево
        if field[i][j] == '#':
            marker = j
            cnt_j = 1
            
            while field[i][marker+cnt_j] == 0 and (marker+cnt_j) <= column: # ведем корабль до колонны
                cnt_j += 1
            else:
                answer += (cnt_j-1)
                field[i][marker] = 0
                field[i][marker + cnt_j - 1] = '#'

            if (marker+cnt_j-1) < column:    # если уперлись в корабль
                if course == n:  # ближайшая граница поля n(внизу, выше по индексуs)
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:  # ищем где ближе пустая ячейка (сверху или снизу)
                        if i+cnt_i_up <= n:
                            if field[i+cnt_i_up][marker+cnt_j] == 0: # двигаем корабли в колонне к ближайшей пустой ячейке
                                field[i+cnt_i_up][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                answer += (cnt_i_up+1)
                                break
                            else:
                                cnt_i_up += 1

                        elif i-cnt_i_down >= 1:
                            if field[i-cnt_i_down][marker+cnt_j] == 0: # двигаем корабли в колонне к ближайшей пустой ячейке
                                field[i-cnt_i_down][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                answer += (cnt_i_down+1)
                                break
                            else:
                                cnt_i_down += 1
                else:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i-cnt_i_down >= 1:
                            if field[i-cnt_i_down][marker+cnt_j] == 0:
                                field[i-cnt_i_down][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                answer += (cnt_i_down+1)
                                break
                            else:
                                cnt_i_down += 1

                        elif i+cnt_i_up <= n:
                            if field[i+cnt_i_up][marker+cnt_j] == 0:
                                field[i+cnt_i_up][marker+cnt_j] = '#'
                                field[i][marker + cnt_j - 1] = 0
                                answer += (cnt_i_up+1)
                                break
                            else:
                                cnt_i_up += 1
                        
    for j in range(column+1, n+1): # обраб поле справа от колонны, слева-направо
        if field[i][j] == '#':
            marker = j
            cnt_j = 1

            while field[i][marker-cnt_j] == 0 and (marker-cnt_j) >= column:
                cnt_j += 1
            else:
                answer += (cnt_j - 1)
                field[i][marker] = 0
                field[i][marker - cnt_j + 1] = '#'

            if (marker - cnt_j + 1) > column:
                if course == n:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i + cnt_i_up <= n:
                            if field[i + cnt_i_up][marker - cnt_j] == 0:
                                field[i + cnt_i_up][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                answer += (cnt_i_up + 1)
                                break
                            else:
                                cnt_i_up += 1

                        elif i - cnt_i_down >= 1:
                            if field[i - cnt_i_down][marker - cnt_j] == 0:
                                field[i - cnt_i_down][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                answer += (cnt_i_down + 1)
                                break
                            else:
                                cnt_i_down += 1
                else:
                    cnt_i_up = 1
                    cnt_i_down = 1
                    while True:
                        if i - cnt_i_down >= 1:
                            if field[i - cnt_i_down][marker - cnt_j] == 0:
                                field[i - cnt_i_down][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                answer += (cnt_i_down + 1)
                                break
                            else:
                                cnt_i_down += 1

                        elif i + cnt_i_up <= n:
                            if field[i + cnt_i_up][marker - cnt_j] == 0:
                                field[i + cnt_i_up][marker - cnt_j] = '#'
                                field[i][marker - cnt_j + 1] = 0
                                answer += (cnt_i_up + 1)
                                break
                            else:
                                cnt_i_up += 1

print(answer)

