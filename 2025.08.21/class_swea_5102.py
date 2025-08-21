'''
BFS를 써서 이거는 level을 반환하면 되는구나 !
'''
import sys; sys.stdin = open("input.txt")
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V:노드의 개수, E: E개의 간선정보
    forward_lst = [[] for _ in range(V+1)]
    visited = [False]*(V+1)

    for _ in range(E):
        start, end = map(int, input().split())
        forward_lst[start].append(end)
        forward_lst[end].append(start)

    S, G = map(int, input().split())

    q = deque()
    q.append((S, 0))
    visited[S] = True
    result = 0

    while q:
        v, level = q.popleft()
        if v == G:
            result = level
            break

        for w in forward_lst[v]:
            if not visited[w]:
                visited[w] = True
                # 할일 
                q.append((w, level + 1))

    print(f'#{tc} {result}')