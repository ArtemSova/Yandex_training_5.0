px = {} # перекрытие точек по иксу
py = {} # перекрытие точек по игрику

with open('F04.txt', 'r') as file:
    w, h, n = map(int, file.readline().split())
    for _ in range(n):
        x, y = map(int, file.readline().split())

        if x in px:
            px[x].add((x, y))
        else:
            px[x] = {(x, y)}

        if y in py:
            py[y].add((x, y))
        else:
            py[y] = {(x, y)}

def func(m):
    start = 1
    while start <= h-m+1:
        for_test = set()
        for q in range(start, start+m):
            if q in px:
                for_test.update(px[q])

        window = 1
        while window <= w-m+1:
            last_test = set(for_test)

            for y in range(window, window+m):
                if y in py:
                    last_test.update(py[y])
                        
            if len(last_test) == n:
                return True
            else:
                window += 1
        else:
            start += 1
    else:
        return False

answer = 3 * 10**10 +1

left = 1
right = n
while left < right:
    middle = (left + right)//2
    if func(middle):
        if middle < answer:
            answer = middle
        right = middle
    else:
        left = middle + 1

print(answer)
