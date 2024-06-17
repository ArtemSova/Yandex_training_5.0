persons = []
max_pers = {}

last_max = 0

with open('H128.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    for i in range(n):
        data = list(map(int, file.readline().split()))
        persons.append(data)
        
        for j in range(len(data)):
            if data[j] > last_max:
                last_max = data[j]
                max_pers[data[j]] = [(i,j)]
print('last_max = ', last_max)

x = max_pers[last_max][0][0]
y = max_pers[last_max][0][1]
print('x =', x, 'y =', y)

marker_1 = 0
marker_1_ans = 0
answer_1_y = 0

marker_2 = 0
marker_2_ans = 0
answer_2_x = 0

# Вычеркнули столбец X
for i in range(n):
    if i != x:
        for j in range(m):
            if persons[i][j] > marker_1:
                marker_1 = persons[i][j]
                answer_1_y = j

print('marker_1 = ', marker_1)
print('answer_1_y =', answer_1_y)

for a in range(n):
    if a != x:
        for b in range(m):
            if b != answer_1_y:
                if persons[a][b] > marker_1_ans:
                    marker_1_ans = persons[a][b]


# Вычеркнули строку Y
for j in range(m):
    if j != y:
        for i in range(n):
            if persons[i][j] > marker_2:
                marker_2 = persons[i][j]
                answer_2_x = i

print('marker_2 =', marker_2)
print('answer_2_x =', answer_2_x)

for a in range(n):
    if a != answer_2_x:
        for b in range(m):
            if b != y:
                print(persons[a][b])
                if persons[a][b] > marker_2_ans:
                    marker_2_ans = persons[a][b]


print('marker_1_ans =', marker_1_ans)
print('marker_2_ans =', marker_2_ans)


                
print('MARKERS_ANS', marker_1_ans, marker_2_ans)
if marker_1_ans > marker_2_ans:
    print(answer_2_x+1, y+1)
else:
    print(x+1, answer_1_y+1)

