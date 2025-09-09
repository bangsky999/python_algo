# 회전
'''
큐로 문제 풀기
'''
from collections import deque
import sys;sys.stdin=open("input.txt")
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    q = deque(list(map(int,input().split())))
    for _ in range(M):
        out = q.popleft()
        q.append(out)
    print(f'#{tc} {q[0]}')