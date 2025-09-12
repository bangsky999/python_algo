# [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
import sys;sys.stdin = open("input.txt")

T = int(input())

def f(idx, cnt, battery):
    global min_cnt

    # 이미 최솟값 이상이면 가지치기
    if cnt >= min_cnt:
        return

    # 종점 도착: 정류장 번호가 N이면 완료
    if idx == N:
        if cnt < min_cnt:
            min_cnt = cnt
        return


    # 1) 교체하지 않고 한 칸 이동 (배터리 남아있을 때만)
    if battery > 0:
        f(idx + 1, cnt, battery - 1)

    # 2) 현재 정류장에서 교체 후 한 칸 이동
    #    (종점 N에서는 교체 불가이므로 idx < N 조건)
    if idx < N:
        f(idx + 1, cnt + 1, station[idx] - 1)

for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    N = li[0]                 # 정류장 수 (목표 정류장 번호 = N)
    station = [0] + li[1:]    # station[1] ~ station[N-1] 충전량, station[N]은 없음
    min_cnt = float('inf')

    # 1번 정류장에서 출발, 교체 0회, 시작 배터리는 station[1]
    f(1, 0, station[1])

    print(f'#{tc} {min_cnt}')
