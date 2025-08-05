T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = str(input())
    counts = [0]*10
    
    for i in arr:
        counts[int(i)] += 1 

    # counts = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    for i in range(len(counts)): # i = 0~10
        if counts[i] == max(counts):
            many_num = max(counts)
            max_num = i
    print(f'#{tc} {max_num} {many_num}')