answer = []

with open('input.txt', 'r') as file:
    n = int(file.readline())
    my_list = list(map(int, file.readline().split()))
    my_list.sort()
    
    k = int(file.readline())
    for j in range(k):
        x, y = map(int, file.readline().split())

        ansx = None
        ansy = None
        
        left_x = 0
        right_x = n-1
        while right_x - left_x > 1:
            middle = (right_x + left_x)//2
            if my_list[middle] < x:
                left_x = middle
            else:
                right_x = middle

        if my_list[left_x] >= x:
            ansx = left_x
        else:
            ansx = right_x

        left_y = 0
        right_y = n-1
        while right_y - left_y > 1:
            middle = (right_y + left_y)//2
            if my_list[middle] <= y:
                left_y = middle
            else:
                right_y = middle
                
        if my_list[right_y] <= y:
            ansy = right_y
        else:
            ansy = left_y

        if x > my_list[ansy] or y < my_list[ansx]:
            answer.append(0)
        else:
            answer.append(ansy-ansx+1)

print(*answer)
            
