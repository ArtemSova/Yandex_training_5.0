first = {}
second = {}

with open('input.txt', 'r') as file:
    n = int(file.readline())
    for i in range(n):
        line = list(map(int, file.readline().split()))
        if (line[0] == line[2] and line[1] < line[3]) or (line[0] < line[2] and line[1] == line[3]) or (line[0] < line[2] and line[1] < line[3]) or (line[0] < line[2] and line[1] > line[3]):
            line = tuple(line)
        else:
            line = (line[2], line[3], line[0], line[1])

        first[i] = line

    for j in range(n):
        line = list(map(int, file.readline().split()))
        if (line[0] == line[2] and line[1] < line[3]) or (line[0] < line[2] and line[1] == line[3]) or (line[0] < line[2] and line[1] < line[3]) or (line[0] < line[2] and line[1] > line[3]):
            line = tuple(line)
        else:
            line = (line[2], line[3], line[0], line[1])

        second[j] = line

counter = {}
cnt = {}
for i in first:
    for j in second:  # подсчет смещения спичек (расположение начала спички А и начала списки В, а так же концов)
        a = (second[j][0] - first[i][0], second[j][1] - first[i][1])
        b = (second[j][2] - first[i][2], second[j][3] - first[i][3])
        if a == b:
            cnt[(i, j)] = a
            if a not in counter:
                counter[a] = 1
            else:
                counter[a] += 1
                
if counter:
    result = max(counter.values())
else:
    result = 0

answer = n - result

print(answer)
