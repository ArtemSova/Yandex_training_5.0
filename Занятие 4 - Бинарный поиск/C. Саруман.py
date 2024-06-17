for_answer = [] # словарь для префиксных сумм

def func(m, x):
    a = for_answer[m+x-1]
    if m == 0:
        b = 0
    else:
        b = for_answer[m-1]

    result = a - b
    return result    

with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    my_list = list(map(int, file.readline().split()))

    for i in range(len(my_list)): # заполняем префиксные суммы
        if i == 0:
            for_answer.append(my_list[0])
        else:
            for_answer.append(my_list[i] + for_answer[i-1])

    for _ in range(m):
        x, y = map(int, file.readline().split())

        left = 0
        right = n-x
        while left < right:
            middle = (left + right)//2
            if func(middle, x) >= y:
                right = middle
            else:
                left = middle + 1

        if func(left, x) == y:
            print(left+1)
        else:
            print(-1)
