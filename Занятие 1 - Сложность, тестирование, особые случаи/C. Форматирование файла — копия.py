f = open('input.txt', 'r')

counter = 0

with open('input.txt', 'r') as file:
    n = int(file.readline())

    for _ in range(n):
        spaces = int(file.readline())
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

