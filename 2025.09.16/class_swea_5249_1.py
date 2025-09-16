# [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
import sys;sys.stdin = open("input.txt")
from heapq import heappop,heappush

def prim(start_node):
    pq = [(0,start_node)]
    MST = [0]*(V+1)
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V+1):
            if graph[node][next_node] == 0:
                continue
            if MST[next_node]:
                continue
            heappush(pq, (graph[node][next_node], next_node))

    return min_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        start, end, weight = map(int,input().split())
        graph[start][end] = weight
        graph[end][start] = weight

    result = prim(0)

    print(f'#{tc} {result}')
