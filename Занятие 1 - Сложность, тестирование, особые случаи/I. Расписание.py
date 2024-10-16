n = int(input())
year = int(input())

holidays = []

for _ in range(n):
    d, m = map(str, input().split())
    holidays.append((int(d), m))

start = str(input())

days_week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_cnt = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}


if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    weeks = 366//7
    last_week = 366 - weeks * 7
    is_leap = 1
else:
    weeks = 365//7
    last_week = 365 - weeks * 7
    is_leap = 0

month = {'January': 31, 'February': 28+is_leap, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

for i in days:
    days_cnt[i] += weeks

start_week = days.index(start)

for j in range(start_week, last_week + start_week):
    if j < 7:
        days_cnt[days[j]] += 1
    else:
        j -= 7
        days_cnt[days[j]] += 1

for hday in holidays:
    date = 0
    for m in month:
        if hday[1] == m:
            date += hday[0]
            break
        else:
            date += month[m]

    marker = date%7
    new_start = days.index(start)
    day_ind = new_start + marker - 1
        
    if day_ind < 0:
        day_ind += 7
    if day_ind > 6:
        day_ind -= 7
            
    days_cnt[days[day_ind]] -= 1

print(max(days_cnt, key = days_cnt.get), min(days_cnt, key = days_cnt.get))





