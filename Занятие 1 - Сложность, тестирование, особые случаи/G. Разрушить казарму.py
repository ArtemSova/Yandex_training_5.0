def main():
    x = int(input())
    y = int(input())
    p = int(input())

    print(func(x, y, p))

def func(x, y, p):
    y -= x
    units = 0
    counter = 1

    if x != p:
        z = int((1.61803399 * x - p)) # золотое сечение
        if z > x:  # костыль
            z = x
        
        if 1 < z < y:
            a = (((y - z))//(x - p)) + 1
            y -= a*(x-p)
            counter += a

    if y > 0:
        units += p

    y_s = y
    units_s = units
    counter_s = counter
    x_s = x

    while units > 0:
        if x < 1:
            counter = -1
            break

        x_2 = x - y
        y = 0
        units -= x_2
        x -= units
        counter += 1

    counter_ans = counter

    if (y_s + (x_s - p)) > 0 and (counter_s - 1) > 0:
        counter = counter_s - 1
        x = x_s
        y = y_s + (x - p)
        units = units_s
        
        while units > 0:
            if x < 1:
                counter = -1
                break

            x_2 = x - y
            y = 0
            units -= x_2
            x -= units
            counter += 1

    if 0 < counter < counter_ans:
            counter_ans = counter

    if (counter_s + 1) > 0:
        counter = counter_s + 1
        x = x_s
        y = y_s - (x - p)
        units = units_s
        
        while units > 0:
            if x < 1:
                counter = -1
                break

            x_2 = x - y
            y = 0
            units -= x_2
            x -= units
            counter += 1

    if 0 < counter < counter_ans:
            counter_ans = counter

    return counter_ans


if __name__ == "__main__":
    main()
