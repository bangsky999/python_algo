# 사다리 문제 설계
# 1. 밑에서부터 올라오자
# - 제일 아래줄에서 값이 2인 곳이 출발 지점
#       100 * 100 -> start_c = arr[99].index(2)
# - 출발지 좌표 : (99, start_c)

# 2. 반복하면서 올라오자
#   - 언제까지 반복? r좌표가 0일때 끝(횟수가 정해져 있지 않다) -> while문이 편하구나!
# - 올라오는 로직
#   - if 왼쪽으로 갈 수 있는 경우
#       - 왼쪽 끝까지 이동
#   - if 오른쪽으로 갈 수 있는 경우
#       - 오른쪽 끝까지 이동
#   - 위로 간다.

# 구체화 해보기
# r = 99
# while r != 0:
#   if 왼쪽으로 갈 수 있는 경우:(if 왼쪽이 있다면(벽이 아니라면) and 왼쪽이 1이라면)
#       while 왼쪽으로 더 이상 못갈 때까지 이동
#   if 오른쪽으로 갈 수 있는 경우:(if 오른쪽이 있다면(벽이 아니라면) and 오른쪽이 1이라면)
#       while 오른쪽으로 더 이상 못갈 때까지 이동

# 위로 간다 -> r -= 1

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 출발지 좌표 초기화
    r = 99
    c = ladder[99].index(2)

    while r != 0:
        # 좌측
        if c > 0 and ladder[r][c-1] == 1:
            while c > 0 and ladder[r][c-1] == 1:
                c -= 1

        # 우측
        elif c < 99 and ladder[r][c+1] == 1:
            while c < 99 and ladder[r][c+1] == 1:
                c += 1
    
        r -= 1
    print(f'#{tc} {c}')