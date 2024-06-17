first = tuple(map(int, input().split(':')))
second = tuple(map(int, input().split(':')))
terr = int(input())

team_1 = first[0] + second[0]
team_2 = first[1] + second[1]

if team_1 > team_2:
    print(0)
elif team_1 == team_2:
    if terr == 1:
        if second[0] > first[1]:
            print(0)
        else:
            print(1)
    else:
        if first[0] > second[1]:
            print(0)
        else:
            print(1)
else:
    if terr == 1:
        if first[1] < second[0] + (team_2 - team_1):
            print(team_2 - team_1)
        else:
            print(team_2 - team_1 + 1)
    else:
        if second[1] < first[0]:
            print(team_2 - team_1)
        else:
            print(team_2 - team_1 + 1)

    

