n = int(input())
my_dict = []
meloman = 2*(10**6)
meloman_num = 0

for i in range(n):
    k = int(input())
    playlist = set(map(str, input().split()))
    my_dict.append(playlist)
    if k < meloman:
        meloman = k
        meloman_num = i

if n == 1:
    print(len(my_dict[0]))
    print(*sorted(my_dict[0]))
else:
    answer = []
    for track in my_dict[meloman_num]:
        for i in range(n):
            if i == meloman_num:
                pass
            elif track in my_dict[i]:
                my_dict[i].remove(track)
                continue
            else:
                break
        else:
            answer.append(track)

    print(len(answer))
    if len(answer) > 0:
        print(*sorted(answer))


