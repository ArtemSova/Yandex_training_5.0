import math

dots = []

with open('G11.txt', 'r') as file:
    k = int(file.readline())
    for i in range(k):
        x, y = map(int, file.readline().split())
        dots.append((x, y))

length = len(dots)
done = False
answer = []

if length == 0:
    answer.append((0, 0))
    answer.append((1, 0))
    answer.append((0, 1))
    answer.append((1, 1))
    done = True
elif length == 1:
    answer.append((dots[0][0]+1, dots[0][1]))
    answer.append((dots[0][0], dots[0][1]+1))
    answer.append((dots[0][0]+1, dots[0][1]+1))
    done = True
elif length == 2:
    abx = abs(dots[1][0] - dots[0][0])
    aby = abs(dots[1][1] - dots[0][1])
    cx = dots[0][0] + aby
    cy = dots[0][1] + abx
    answer.append((cx, cy))
    dx = dots[1][0] + aby
    dy = dots[1][1] + abx
    answer.append((dx, dy))
    done = True
else:
    for i in range(length-2):
        a = dots[i]
        for j in range(i+1, length-1):
            b = dots[j]
            ab = math.hypot(b[0] - a[0], b[1] - a[1])  # длинна ab
            for k in range(j+1, length):
                c = dots[k]

                ac = math.hypot(c[0] - a[0], c[1] - a[1])
                bc = math.hypot(c[0] - b[0], c[1] - b[1])

                if ab == ac:
                    if int(math.degrees(math.acos(round((ab**2 + ac**2 - bc**2) / (2 * ab * ac), 10)))) == 90: # угол a
                        dx = b[0] + c[0] - a[0]
                        dy = b[1] + c[1] - a[1]
                        if (dx, dy) not in dots:
                            answer = [(dx, dy)]
                            done = True
                        else:
                            answer = []
                            done = True
                            break
                elif ab == bc:
                    if int(math.degrees(math.acos(round((ab**2 + bc**2 - ac**2) / (2 * ab * bc), 10)))) == 90:
                        dx = a[0] + c[0] - b[0]
                        dy = a[1] + c[1] - b[1]
                        if (dx, dy) not in dots:
                            answer = [(dx, dy)]
                            done = True
                        else:
                            answer = []
                            done = True
                            break
                elif bc == ac:
                    if int(math.degrees(math.acos(round((ac**2 + bc**2 - ab**2) / (2 * bc * ac), 10)))) == 90:
                        dx = a[0] + b[0] - c[0]
                        dy = a[1] + b[1] - c[1]
                        if (dx, dy) not in dots:
                            answer = [(dx, dy)]
                            done = True
                        else:
                            answer = []
                            done = True
                            break
            else:
                continue
            break
        else:
            continue
        break

if not done:
    abx = abs(dots[-1][0] - dots[-2][0])
    aby = abs(dots[-1][1] - dots[-2][1])
    cx = dots[-2][0] + aby
    cy = dots[-2][1] + abx
    answer.append((cx, cy))
    dx = dots[-1][0] + aby
    dy = dots[-1][1] + abx
    answer.append((dx, dy))

print(len(answer))
if len(answer) != 0:
    for i in answer:
        print(i[0], i[1])
