### 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 ###
'''
K: 충전으로 최대 이동 정류장 수, N: 0번부터 N번까지 정류장, M: 충전기 설치된 정류장 수
- 현 위치에서 K만큼 범위 내에서 최대로 갈 수 있는 정류장으로 이동
    - 또 현위치에서 이동,,
    - 못가면(K이내에 이동 정류장이 없다면) 0을 출력하고 다음 test case로
- 마지막에 도착하면 개수 출력
- while 써야할 듯(언제 끝날지 모르니까)
'''
import sys; sys.stdin = open("input.txt")
T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split()) # K: 3, N: 10, M: 5
    stations = list(map(int, input().split())) + [N] # [1,3,5,7,9,10]

    val = 1
    cnt = 0
    idx = 0 # 현재 위치
    while True:
        if idx == stations[-1]:
            print(f'#{tc} {cnt-1}')
            break
        to_go = []
        for i in stations: # [1,3,5,7,9,10]
            if idx < i <= idx + K: # to_go = [1,3]
                to_go.append(i)
        if len(to_go) == 0: # to_go가 없다면 0 출력하자
            cnt = 0
            print(f'#{tc} {cnt}')
            break
        idx = to_go[-1] # idx = 3
        cnt += 1
