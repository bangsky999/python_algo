N = int(input())
arr = list(range(1, N+1))
for i in range(len(arr)):
    cnt = 0
    for j in str(arr[i]):
        if int(j) == 3:
            cnt += 1
        if int(j) == 6:
            cnt += 1
        if int(j) == 9:
            cnt += 1
        else:
            pass
    if cnt != 0:
        arr[i] = '-'*cnt
    else:
        arr[i] = str(arr[i])
for i in arr:
    print(i, end = ' ')