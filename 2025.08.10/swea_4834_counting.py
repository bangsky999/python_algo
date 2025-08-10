import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    counts = [0]*10 #[0000000000]
    temp = [0]*len(arr)

    for i in range(len(arr)):
        counts[arr[i]] += 1
    for i in range(1,10):
        counts[i] += counts[i-1]

    for i in range(len(arr)-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]

    print(f'#{tc} {temp.index(max(counts))} {max(counts)}')

