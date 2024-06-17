board = [str(input()) for _ in range(8)]

deleted = []

counter=64

for i in range(8):
    for j in range(8):
        if board[i][j] == 'R':
            counter -= 1
            if j != 0:
                for z in range(j-1, -1, -1):
                    if board[i][z] == '*':
                        if (i, z) not in deleted:
                            counter -= 1
                            deleted.append((i, z))
                    else:
                        break
            if j != 7:
                for x in range(j+1, 8, 1):
                    if board[i][x] == '*':
                        if (i, x) not in deleted:
                            counter -= 1
                            deleted.append((i, x))
                    else:
                        break
            if i != 0:
                for c in range(i-1, -1, -1):
                    if board[c][j] == '*':
                        if (c, j) not in deleted:
                            counter -= 1
                            deleted.append((c, j))
                    else:
                        break
            if i!=7:
                for v in range(i+1, 8, 1):
                    if board[v][j] == '*':
                        if (v, j) not in deleted:
                            counter -= 1
                            deleted.append((v, j))
                    else:
                        break
                
        elif board[i][j] == 'B':
            counter -= 1
            if i != 0:
                if j != 0:
                    i_2 = i
                    j_2 = j
                    while i_2 > 0 and j_2 > 0:
                        i_2 -= 1
                        j_2 -= 1
                        if board[i_2][j_2] == '*':
                            if (i_2, j_2) not in deleted:
                                counter -= 1
                                deleted.append((i_2, j_2))
                        else:
                            break
                if j != 7:
                    i_2 = i
                    j_2 = j
                    while i_2 > 0 and j_2 < 7:
                        i_2 -= 1
                        j_2 += 1
                        if board[i_2][j_2] == '*':
                            if (i_2, j_2) not in deleted:
                                counter -= 1
                                deleted.append((i_2, j_2))
                        else:
                            break
            if i != 7:
                if j != 0:
                    i_2 = i
                    j_2 = j
                    while i_2 < 7 and j_2 > 0:
                        i_2 += 1
                        j_2 -= 1
                        if board[i_2][j_2] == '*':
                            if (i_2, j_2) not in deleted:
                                counter -= 1
                                deleted.append((i_2, j_2))
                        else:
                            break
                if j != 7:
                    i_2 = i
                    j_2 = j
                    while i_2 < 7 and j_2 < 7:
                        i_2 += 1
                        j_2 += 1
                        if board[i_2][j_2] == '*':
                            if (i_2, j_2) not in deleted:
                                counter -= 1
                                deleted.append((i_2, j_2))
                        else:
                            break
        else:
            pass

print(counter)
