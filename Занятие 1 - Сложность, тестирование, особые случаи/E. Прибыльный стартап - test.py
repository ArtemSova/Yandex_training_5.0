#n, k, d = map(int, input().split())

#n, k, d = 21, 108, 1    # 216
#n, k, d = 5, 12, 4     # -1
#n, k, d = 8, 13, 5     # -1
#n, k, d = 93915286, 67082347, 59876  # -1
#n, k, d = 2, 3, 5  # 210000
#n, k, d = 29420920, 98069736, 69929 #пиздец какое число
#n, k, d = 100, 13, 9  # 100100000000
#n, k, d = 2, 1, 3   #2000
#n, k, d = 49160624, 70229462, 90569   #-1
#n, k, d = 1, 20, 3   # -1
#n, k, d = 75593505, 62994587, 78831  # -1

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

