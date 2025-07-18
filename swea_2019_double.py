n = int(input())
chart = [1]
for _ in range(1,n+1):
    new = chart[-1]*2
    chart.append(new)
    
for num in chart:
    print(num, end=' ')