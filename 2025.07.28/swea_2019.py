N = int(input())
init = 1
lst = [1]
for i in range(1, N+1):
    init = init * 2
    lst.append(init)

for i in lst:
    print(i, end = ' ')