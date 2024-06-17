with open('input.txt', 'r') as file:
    w, n, m = map(int, file.readline().split())
    first = list(map(int, file.readline().split()))
    second = list(map(int, file.readline().split()))

def func(m):
    left_size = m
    right_size = w - m
    counter_1 = 0
    counter_2 = 0
    answer_1 = 0
    answer_2 = 0
    
    for i in first:
        if answer_1 == 0:
            if i <= left_size:
                counter_1 += 1
                answer_1 = i
            else:                # Расширяем колонку
                return 10**11, 0 # В колонку не влезает даже одно слово
        else:
            if answer_1 == left_size:
                if i <= left_size:
                    counter_1 += 1
                    answer_1 = i
                else:
                    return 10**11, 0
            else:
                if answer_1 + i + 1 <= left_size:
                    answer_1 += (i+1)
                else:
                    if i <= left_size:
                        counter_1 += 1
                        answer_1 = i
                    else:
                        return 10**11, 0

    for j in second:
        if answer_2 == 0:
            if j <= right_size:
                counter_2 += 1
                answer_2 = j
            else:
                return 0, 10**11
        else:
            if answer_2 == right_size:
                if j <= right_size:
                    counter_2 += 1
                    answer_2 = j
                else:
                    return 0, 10**11
            else:
                if answer_2 + j + 1 <= right_size:
                    answer_2 += (j+1)
                else:
                    if j <= right_size:
                        counter_2 += 1
                        answer_2 = j
                    else:
                        return 0, 10**11

    return counter_1, counter_2



left = 1
right = w
answer = 10**11
while left < right:
    middle = (left + right)//2
    c_1, c_2 = func(middle)
    ans = max(c_1, c_2)
    
    if ans < answer: # записываем максимально подходящий ответ
        answer = ans
        
    if c_1 >= c_2:  # Если левая колонка длиннее правой, мы ее расширяем
        left = middle+1
    else:
        right = middle

print(answer)
