# [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
import sys;sys.stdin = open("input.txt")

'''
싸이클을 제거하고, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라한다.
'''
def find_set(x):
    if x == parents[x]:
        return x
    
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry: # 싸이클 발생
        return
    
    # 일정한 규칙으로 병합
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
    

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    edges = []

    for _ in range(E):
        start, end, weight = map(int,input().split())
        edges.append((start, end, weight)) # 간선들의 정보를 저장

    # 가중치 기준 오름차순 정렬
    edges.sort(key=lambda x:x[2])

    cnt = 0 # 현재까지 선택한 간선의 수
    result = 0 # 가중치의 합

    parents = [i for i in range(V+1)] # make_set

    for u, v, w in edges:
        # 사이클이 아니라면
        # - 연결
        # - cnt + 1
        # - cnt가 V-1이라면 종료
        if find_set(u) != find_set(v):
            union(u,v)
            cnt += 1
            result += w

            if cnt == V:
                break
    
    print(f'#{tc} {result}')


