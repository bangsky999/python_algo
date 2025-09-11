# 노드의 거리
from collections import deque
import sys;sys.stdin=open("input.txt")
'''
입력을 받고 인접 노드를 저장
forward_li = [[] for _ in range()]
print해서 제대로 빈 리스트인지 확인 !
append로 집어넣기

DFS - 깊이 우선 탐색 사용
방문처리 배열 forward_li 개수만큼
시작점을 queue에 넣고 시작
pop해서 간선 지날때마다 cnt + 1? -> 좀더 검증 필요
간선을 q에 집어넣고 하나씩 꺼내서 출발하기(for문 순회)
q가 비워졌는데 못간다? 0 출력
'''
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # v: 노드 수, E: 간선 개수 # 6, 5
    forw_li = [[] for _ in range(V+1)] # [[], [], [], [], [], [], []]
    for i in range(E):
        start, end = map(int,input().split())
        forw_li[start].append(end)
        forw_li[end].append(start) # [[], [4, 3], [3, 5], [], [6], [], []]
    S, G = map(int,input().split()) # S(시작) : 1 , G(도착) : 6

    visited = [False]*(V+1)
    q = deque()
    q.append((S, 0)) # q= [1]
    visited[S] = True
    min_cnt = 9999

    while q:
        v, level = q.pop() # 1, 0
        if v == G:
            if min_cnt > level:
                min_cnt = level

        for w in forw_li[v]:
            if not visited[w]:
                visited[w] = True
                q.append((w, level + 1))
                
    if min_cnt == 9999:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {min_cnt}')