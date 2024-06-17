def check(m):
    marker = 0
    pmx = -10**9
    pmn = 10**9
    for j in range(n):
        while marker < n and x[marker] < x[j] + m:
            marker += 1

        mx = pmx
        mn = pmn

        if marker != n:
            mx = max(mx, sufmax[marker])
            mn = min(mn, sufmin[marker])

        if mx - mn < m:
            return True
        
        pmx = prefmax[j]
        pmn = prefmin[j]
    return False

with open('input.txt', 'r') as file:
    w, h, n = map(int, file.readline().split())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, file.readline().split())))

a.sort()  # [(1, 1), (1, 3), (4, 1), (4, 3)]
x = []  # [1, 1, 4, 4]  Список всех иксов
y = []  # [1, 3, 1, 3]  Список всех игриков
for now in a:
    x.append(now[0])
    y.append(now[1])

prefmin = [y[0]] * n  # Префиксы(y) для иксов   [1, 1, 1, 1]
prefmax = [y[0]] * n  # [1, 3, 3, 3]
sufmin = [y[-1]] * n  # Суффиксы(y) для иксов  [1, 1, 1, 3]
sufmax = [y[-1]] * n  # [3, 3, 3, 3]

for i in range(1, n):
    prefmin[i] = min(prefmin[i-1], y[i])
    prefmax[i] = max(prefmax[i-1], y[i])

for i in range(n-2, -1, -1):
    sufmin[i] = min(sufmin[i+1], y[i])
    sufmax[i] = max(sufmax[i+1], y[i])

left = 0
right = min(w, h)
while left < right:
    middle = (left + right)//2
    if check(middle):
        right = middle
    else:
        left = middle + 1

print(left)
