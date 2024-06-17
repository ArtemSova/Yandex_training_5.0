w = h = c = None

text = []
answer = []
right_up_dot = (0, 0)
stop_x = []
fragment_s = [(0, 0)]  # (y, x-старт фрагмента)

y = 0
next_y = h

f = open('j4.txt', 'r')
for line in f:
    if w == None:
        w, h, c = map(int, line.split())
    else:
        words = str(line)
        words = words[:-1]
        if words == '':
            text.append(words)
        else:
            if not text:
                text.append(words)
            else:
                text[-1] = text[-1] + ' ' + words

next_y = h
counter = 0

for strings in text:
    if counter != 0:
        y += next_y
        next_y = h
        right_up_dot = (0, y)
    commands = []
    word = ''
    picture = ''

    for string in range(len(strings)):
        if string == len(strings) - 1 and picture == '':
            word = word + strings[string]
            commands.append(word.strip())
            if word != '':
                word = ''
        elif strings[string] == '(':
            if word != '':
                commands.append(word.strip())
            word = ''
            picture = strings[string]
        elif strings[string] == ')':
            picture = picture + strings[string]
            picture = picture.replace(')', '')
            picture = picture.split()
            commands.append(picture)
            picture = ''
        elif strings[string] == ' ':
            if word == '' and  picture == '':
                pass
            elif word != '':
                commands.append(word.strip())
                word = ''
            elif picture != '':
                picture = picture + strings[string]
        else:
            if picture != '':
                picture = picture + strings[string]
            else:
                word = word + strings[string]

    for i in commands:
        start = right_up_dot[0]
        stop_x.sort(key=lambda t: t[1][0])
        for dot in range(len(stop_x)):
            if stop_x[dot][0] < y:
                stop_x.pop(dot)
                break

        if i[0] != '(image':
            length = len(i)*c
            did = False
            while did == False:
                start = right_up_dot[0]
                if not stop_x:
                    pass
                else:
                    for st in stop_x:
                        start = right_up_dot[0]

                        if y < st[0]:
                            if start == 0 or any(y < fr[0] and start == fr[1] for fr in fragment_s):
                                if start+length <= st[1][0]:
                                    right_up_dot = (start+length, y)

                                    did = True
                                    break
                                else:
                                    if start < st[1][1]:
                                        right_up_dot = (st[1][1], y)
                            else:
                                if start+length+c <= st[1][0]:
                                    right_up_dot = (start+length+c, y)
                                    did = True
                                    break
                                else:
                                    if start < st[1][1]:
                                        right_up_dot = (st[1][1], y)

                if did == False:
                    start = right_up_dot[0]
                    if start == 0 or any(y < fr[0] and start == fr[1] for fr in fragment_s):
                        if start + length <= w:
                            right_up_dot = (start+length, y)
                            did = True
                        else:
                            y += next_y
                            next_y = h
                            right_up_dot = (0, y)
                    else:
                        if c + start + length <= w:
                            right_up_dot = (c + start+length, y)
                            did = True
                        else:
                            y += next_y
                            next_y = h
                            right_up_dot = (0, y)
                
        else:
            did = False
            lay = ''
            width = 0
            height = 0
            dx = 0
            dy = 0
            
            for j in i:
                if j.startswith('layout='):
                    lay = str(j[7:])
                elif j.startswith('width='):
                    width = int(j[6:])
                elif j.startswith('height='):
                    height = int(j[7:])
                elif j.startswith('dx='):
                    dx = int(j[3:])
                elif j.startswith('dy='):
                    dy = int(j[3:])
                  
            while did == False:
                start = right_up_dot[0]

                if not stop_x:
                    pass
                else:
                    for st in stop_x:
                        start = right_up_dot[0]
                        if y < st[0]:
                            if lay == 'embedded':
                                if start == 0 or any(y < fr[0] and start == fr[1] for fr in fragment_s):
                                    if start+width <= st[1][0]:
                                        right_up_dot = (start + width, y)
                                        answer.append((start, y))
                                        if height > next_y:
                                            next_y = height
                                        did = True
                                        break
                                    else:
                                        if start < st[1][1]:
                                            right_up_dot = (st[1][1], y)
                                else:
                                    if start + c + width <= st[1][0]:
                                        right_up_dot = (start + c + width, y)
                                        answer.append((start + c, y))
                                        if height > next_y:
                                            next_y = height
                                        did = True
                                        break
                                    else:
                                        if start < st[1][1]:
                                            right_up_dot = (st[1][1], y)
                                                
                            elif lay == 'surrounded':
                                if start + width <= st[1][0]:
                                    stop_x.append((y + height, (start, start + width)))


                                    fragment_s.append((y+ height, start + width))
                                    right_up_dot = (start + width, y)
                                    answer.append((start, y))
                                    did = True
                                    break
                                else:
                                    if start < st[1][1]:
                                        right_up_dot = (st[1][1], y)
                            else:
                                start_x = right_up_dot[0] + dx

                                if start_x + width > w:
                                    start_x -= (start_x + width - w)
                                elif start_x < 0:
                                    start_x = 0

                                start_y = y + dy

                                answer.append((start_x, start_y))
                                did = True
                                break

                if did == False:
                    start = right_up_dot[0]
                    if lay == 'embedded':
                        if start == 0 or any(y < fr[0] and start == fr[1] for fr in fragment_s):
                            if start + width <= w:
                                right_up_dot = (start + width, y)
                                answer.append((start, y))
                                if height > next_y:
                                    next_y = height
                                did = True
                                break
                        else:      
                            if c + start + width <= w:
                                right_up_dot = (start + width + c, y)
                                answer.append((c + start, y))
                                if height > next_y:
                                    next_y = height
                                did = True
                                
                                break

                    elif lay == 'surrounded':
                        if start + width <= w:
                            stop_x.append((y + height, (start, start + width)))
                                            
                            fragment_s.append((y + height, start + width))
                            right_up_dot = (start + width, y)
                            answer.append((start, y))
                            did = True
                            break

                    else:
                        start_x = right_up_dot[0] + dx
                                        
                        if start_x + width > w:
                            start_x -= (start_x + width - w)
                        elif start_x < 0:
                            start_x = 0
                                            
                        start_y = y + dy
                                        
                        answer.append((start_x, start_y))
                        did = True
                        break

                if did == False:
                    y += next_y
                    right_up_dot = (0, y)
                    next_y = h

    counter += 1

for a in answer:
    print(*a)

            
        
