# [모의 SW 역량테스트] 탈주범 검거
import sys;sys.stdin=open("input.txt")
from collections import deque
'''
최초의 위치를받고
4방 탐색해서 이동

이동 못하는 조건
- 이미 방문했다
- 지금의 출구가 막혔다
- 다음의 입구가 막혔다
- 범위 밖이다

visited에 누적 시간 작성
'''
types = {
    1:[1,1,1,1],
    2:[1,1,0,0],
    3:[0,0,1,1],
    4:[1,0,0,1],
    5:[0,1,0,1],
    6:[0,1,1,0],
    7:[1,0,1,0],
}
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    q = deque([(R,C)])
    visited[R][C] = 1

    while q:
        now_r, now_c = q.popleft()
        dirs = types[arr[now_r][now_c]]
        for d in range(4):
            next_r, next_c = now_r +dr[d], now_c+dc[d]

            if dirs[d] == 0:
                continue

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            
            if arr[next_r][next_c] == 0:
                continue

            if visited[next_r][next_c]:
                continue

            if d == 0 and types[arr[next_r][next_c]][1] == 0:
                continue
            elif d == 1 and types[arr[next_r][next_c]][0] == 0:
                continue
            elif d == 2 and types[arr[next_r][next_c]][3] == 0:
                continue
            elif d == 3 and types[arr[next_r][next_c]][2] == 0:
                continue

            if visited[now_r][now_c] + 1 > L:
                continue

            visited[next_r][next_c] = visited[now_r][now_c] + 1
            q.append((next_r, next_c))
    cnt = 0
    # L 시간 이하로 방문한 모든 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')
