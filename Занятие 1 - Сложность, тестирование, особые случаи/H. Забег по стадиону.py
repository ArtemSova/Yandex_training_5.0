stadium, x1, v1, x2, v2 = map(int, input().split())

answer = 10**30

for rotation in range(2):
    delta_x = (x2 -  x1 + stadium) % stadium
    delta_v = v1 - v2
        
    if delta_v < 0:
        delta_v = -delta_v
        delta_x = (-delta_x) % stadium
            
    if delta_x == 0:
        answer = 0

    if delta_v != 0:
        answer = min(answer, delta_x/delta_v)

    x2 = (-x2) % stadium
    v2 = -v2

if answer == 10**30:
    print('NO')
else:
    print('YES')
    print(answer)

