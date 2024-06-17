dots_set = set()

with open('input.txt', 'r') as file:
    k = int(file.readline())
    for i in range(k):
        x, y = map(int, file.readline().split())
        dots_set.add((x, y))

dots = list(dots_set)
length = len(dots)
answer = []

if length == 0:
    answer.append((0, 0))
    answer.append((1, 0))
    answer.append((0, 1))
    answer.append((1, 1))
elif length == 1:
    answer.append((dots[0][0]+1, dots[0][1]))
    answer.append((dots[0][0], dots[0][1]+1))
    answer.append((dots[0][0]+1, dots[0][1]+1))
elif length == 2:
    a = dots[0]
    b = dots[1]
    
    if (a[0] < b[0] and a[1] == b[1]) or (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1]) or (a[0] == b[0] and a[1] < b[1]):
        abx = abs(b[0] - a[0])
        aby = abs(b[1] - a[1])
        cx = a[0] + aby
        cy = a[1] + abx
        c = (cx, cy)
        dx = b[0] + aby
        dy = b[1] + abx
        d = (dx, dy)
        answer = [c, d]
    else:
        abx = abs(a[0] - b[0])
        aby = abs(a[1] - b[1])
        cx = a[0] + aby
        cy = a[1] - abx
        c = (cx, cy)
        dx = b[0] + aby
        dy = b[1] - abx
        d = (dx, dy)
        answer = [c, d]
elif length > 2:
    for i in range(length-1):
        a = dots[i]
        for j in range(i+1, length):
            b = dots[j]

            if (a[0] < b[0] and a[1] == b[1]) or (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1]) or (a[0] == b[0] and a[1] < b[1]):
                abx = abs(b[0] - a[0])
                aby = abs(b[1] - a[1])
                cx = a[0] + aby
                cy = a[1] + abx
                c1 = (cx, cy)
                dx = b[0] + aby
                dy = b[1] + abx
                d1 = (dx, dy)
                cx = a[0] - aby
                cy = a[1] - abx
                c2 = (cx, cy)
                dx = b[0] - aby
                dy = b[1] - abx
                d2 = (dx, dy)
            else:
                abx = abs(a[0] - b[0])
                aby = abs(a[1] - b[1])
                cx = a[0] + aby
                cy = a[1] - abx
                c1 = (cx, cy)
                dx = b[0] + aby
                dy = b[1] - abx
                d1 = (dx, dy)
                cx = a[0] - aby
                cy = a[1] + abx
                c2 = (cx, cy)
                dx = b[0] - aby
                dy = b[1] + abx
                d2 = (dx, dy)

            if c1 in dots_set and d1 in dots_set:
                answer = []
                break
            elif c2 in dots_set and d2 in dots_set:
                answer = []
                break
            elif c1 in dots_set:
                answer = [d1]
            elif c2 in dots_set:
                answer = [d2]
            elif d1 in dots_set:
                answer = [c1]
            elif d2 in dots_set:
                answer = [c2]
            else:
                if len(answer) == 0:
                    answer = [c1, d1]
        else:
            continue
        break

print(len(answer))
if len(answer) != 0:
    for i in answer:
        print(i[0], i[1])
