# import sys
# sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # [0] (10,10) 배열 만들기
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for a in range(r1, r2+1):
            for b in range(c1, c2+1):
                arr[a][b] += 1

    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')

