import sys;sys.stdin=open("input.txt")
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
# 상하좌우로
turnel = {
    1:[1,1,1,1],
    2:[1,1,0,0],
    3:[0,0,1,1],
    4:[1,0,0,1],
    5:[0,1,0,1],
    6:[0,1,1,0],
    7:[1,0,1,0],
}
T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    q = deque()
    q.append((R,C))
    visited[R][C] = 1

    while q:
        r,c = q.popleft()

        for d in range(4):
            if turnel[arr[r][c]][d] == 1:
                nr, nc = r + dr[d], c + dc[d]

                # 범위 밖이면 다시
                if 0 > nr or nr >= N or 0 > nc or nc >=M:
                    continue

                # 0이면 다시
                if arr[nr][nc] == 0:
                    continue

                if visited[nr][nc]:
                    continue

                # 안에서도 뚫려있고 밖에서도 뚫려야함
                if d == 0 and turnel[arr[nr][nc]][1] != 1:
                    continue
                elif d == 1 and turnel[arr[nr][nc]][0] != 1:
                    continue
                elif d == 2 and turnel[arr[nr][nc]][3] != 1:
                    continue
                elif d == 3 and turnel[arr[nr][nc]][2] != 1:
                    continue

                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if 0 < visited[r][c] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')