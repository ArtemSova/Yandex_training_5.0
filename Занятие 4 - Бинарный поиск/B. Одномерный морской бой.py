n = int(input())

def func(k):
    length = k*(k+1)*(k+2)//6 # формула тетраэдрального числа
    space = (2+k-1)*k//2 - 1  # формула арифмет прогрессии - 1
    result = length + space

    return result

if n == 0:
    print(0)
else:
    left = 1
    right = n
    while right - left > 1:
        middle = (left + right)//2
        if func(middle) <= n:
            left = middle
        else:
            right = middle

    print(left)
