def main():
    n = int(input())
    sektors = list(map(int, input().split()))     # через while работает медленно
    a, b, k = map(int, input().split())
            
    print(func(n, sektors, a, b, k))

def func(n, sektors, a, b, k):
    
    answer = 0

    if (b - a) >= n*k:
        answer = max(sektors)
    else:
        y = n*k
        if a > y:
            x = a - a%y
            a -= x
            b-=x
 
        if a > k and k > 2:
            x = k/2
            a = int(a//x)
            b = int(b//x)
            k = 2

        if a < k and k > 2:
            x = a/2
            b = int(b//x)
            k = int(k//x)
            a = 2
        
        for i in range(a, b+1):
            position = i//k
            if i%k == 0:
                position -= 1

            if position >= n:
                position -= n

            if sektors[position] > answer:
                answer = sektors[position]

            if sektors[-position] > answer:
                answer = sektors[-position]

    return answer

if __name__ == '__main__':
    main()
