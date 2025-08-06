# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    s += arr[r][c]

            if max_fly < s:
                max_fly = s
    print(f'#{tc} {max_fly}')