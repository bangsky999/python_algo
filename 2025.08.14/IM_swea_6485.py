### 삼성시의 버스노선 ###

import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N: 버스 개수
    bus_station = [0] * 5001 # 0~5000까지 버정 만들기
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_station[i] += 1
    P = int(input())
    p_lst = [int(input()) for _ in range(P)] # 확인할 정류장 리스트
    
    # p리스트를 순회하며 i 번 리스트를 받아오고
    # 이걸 바로 bus_station에서 가져오자
    print(f'#{tc}', end = ' ')
    for i in p_lst: # [1, 2, 3, 4, 5]
        print(bus_station[i], end = ' ')
    print()