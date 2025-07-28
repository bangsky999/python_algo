## 가보자 ## 
month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

N = int(input())
for i in range(1, N+1):
    year = input()[0:4]
    month = input()[4:6]
    day = input()[6:]

    if 1 <= int(month) <=12 and 1 <= int(day) <= month_day[int(month)]:
        print(f'#{i} {year}/{month}/{day}')
    else:
        print(f'#{i} -1')