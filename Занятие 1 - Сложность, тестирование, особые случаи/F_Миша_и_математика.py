def main():
    n = int(input())
    my_list = list(map(int, input().split()))

    print(func(n, my_list))


def func(n, my_list):
    counter_1 = 0
    counter_2 = 0
    new_list = []

    for i in my_list:
        if i%2 == 0:
            counter_2 += 1
            new_list.append(2)
        else:
            counter_1 += 1
            new_list.append(1)

    answer = ''
    
    if counter_1%2 != 0:
        answer += '+'*(n-1)
    elif counter_2 == 0:
        answer += 'x'*(n-1)
    else:
        for j in range(n):
            if j == 0:
                if new_list[j] == 2:
                    counter_2 -= 1
                else:
                    counter_1 -= 1
            elif new_list[j] == 2:
                counter_2 -= 1
                answer += '+'
            else:
                counter_1 -= 1
                if counter_1 == 0:
                    answer += 'x'
                    answer += '+'*(counter_2)
                    break
                else:
                    answer += '+'

    return answer

if __name__ == '__main__':
    main()
