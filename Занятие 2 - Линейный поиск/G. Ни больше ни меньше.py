answer = []

with open('input.txt', 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        data = list(map(int, f.readline().split()))

        pre_ans = []
        for_ans = []
        min_ans = 0
            
        for i in data:
            if not for_ans:
                for_ans.append(i)
                min_ans = i
            else:
                length = len(for_ans)
                if min_ans >= length + 1:
                    if length + 1 <= i:
                        for_ans.append(i)
                        if min_ans > i:
                            min_ans = i
                    else:
                        pre_ans.append(length)
                        for_ans = [i]
                        min_ans = i
                else:
                    pre_ans.append(length)
                    for_ans = [i]
                    min_ans = i
        else:
            pre_ans.append(len(for_ans))
                
        answer.append((len(pre_ans), pre_ans))

for i in answer:
    print(i[0])
    print(*i[1])
   
