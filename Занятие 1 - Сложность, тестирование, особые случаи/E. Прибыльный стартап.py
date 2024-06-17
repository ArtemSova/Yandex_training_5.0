n, k, d = map(int, input().split())

answer = n

if d > 1:
    for _ in range(1, 3):
        if answer == -1:
            break
        for i in range(0, 10):
            if answer == -1:
                break
            if (answer*10+i)%k == 0:
                answer = answer*10+i
                break
            else:
                if i != 9:
                    pass
                else:
                    answer = -1

    if answer != -1:
        answer = str(answer)
        answer = answer + answer[-1]*(d-2)
    
else:
    for i in range(0, 10):
        if (answer*10+i)%k == 0:
            answer = answer*10+i
            break
        else:
            if i != 9:
                pass
            else:
                answer = -1

print(str(answer))
'''
Могут быть слишком большие числа, в лоб нельзя, переводим в строку
'''
