n = int(input())

#x_list = {1: [1, 2, 3, 4, 5, 6, 7, 8], 2: [8], 3: [1, 2, 3, 4, 5, 6, 7, 8], 4: [8], 5: [1, 2, 3, 4, 5, 6, 7, 8], 6: [8], 7: [1, 2, 3, 4, 5, 6, 7, 8], 8: [8]}
#y_list = {1: [1, 3, 5, 7], 2: [1, 3, 5, 7], 3: [1, 3, 5, 7], 4: [1, 3, 5, 7], 5: [1, 3, 5, 7], 6: [1, 3, 5, 7], 7: [1, 3, 5, 7], 8: [1, 2, 3, 4, 5, 6, 7, 8]}

x_list = {}
y_list = {}

for _ in range(n):
    x, y = map(int, input().split())
    
    if x in x_list:
        xy = list(x_list[x]) + [y]
        x_list[x] = xy
    else:
        x_list[x] = [y]

    if y in y_list:
        xy = list(y_list[y]) +[x]
        y_list[y] = xy
    else:
        y_list[y] = [x]

answer = 0

for i in x_list:
    counter = 2
    
    for j in range(1, len(x_list[i])):
        try:
            if x_list[i][j] - x_list[i][j-1] != 1:
                counter += 2
        except:
            pass

    answer += counter

for i in y_list:
    counter = 2
    
    for j in range(1, len(y_list[i])):
        try:
            if y_list[i][j] - y_list[i][j-1] != 1:
                counter += 2
        except:
            pass

    answer += counter

print(answer)     
        

        
