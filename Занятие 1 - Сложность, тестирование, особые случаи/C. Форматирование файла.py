n = int(input())

counter = 0

for _ in range(n):
    spaces = int(input())
    if spaces == 1 or spaces == 4:
        counter += 1
    elif spaces == 0:
        pass
    elif spaces== 2 or spaces == 3:
        counter += 2
    elif spaces%4 == 0:
        counter += spaces//4
    elif spaces%4 == 2:
        counter += spaces//4 + 2
    elif spaces%4 == 1:
        counter += spaces//4 + 1
    elif spaces%4 == 3:
        counter += spaces//4 + 2

print(int(counter))

