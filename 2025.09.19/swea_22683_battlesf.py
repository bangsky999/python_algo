# 22683. 나무 베기
import sys;sys.stdin = open("input.txt")
from collections import deque
# 상, 우, 하, 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

N, K = map(int,input().split())
field = [list(input() for _ in range(N))]

# 시작, 끝 찾기
for r in range(N):
    for c in range(N):
        if field[r][c] == 'X':
            sr, sc = r, c
        if field[r][c] == 'Y':
            er, ec = r, c
q = deque()
visited = [[0]*N for _ in range(N)]
for d in range(4):
    q.append((sr, sc, 0, 0, d)) # r, c, dir, move_cnt, dir