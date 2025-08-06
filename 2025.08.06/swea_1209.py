# import sys
# sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 가로 체크
    for r in range(100):
        s1 = 0
        for c in range(100):
            s1 += arr[r][c]
        if max_sum < s1:
            max_sum = s1
    # 세로 체크
    for r in range(100):
        s2 = 0
        for c in range(100):
            s2 += arr[c][r]
        if max_sum < s2:
            max_sum = s2
    # 대각 오른아래 체크
    s3 = 0
    for r in range(100):
        s3 += arr[r][r]
    if max_sum < s3:
        max_sum = s3
    # 대각 왼쪽아래 체크
    s4 = 0
    for r in range(100):
        s4 += arr[r][99-r]
    if max_sum < s4:
        max_sum = s4

    print(f'#{tc} {max_sum}')