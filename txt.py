'''
최소신장트리를 만들기위해 kruskal 알고리즘을 사용하자
인접 리스트를 사용해 저장하고
cnt == V- 1이면 종료
result 출력

입력받은 간선을 하나씩 꺼내서 union하자
'''
import sys;sys.stdin = open("input.txt")
def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())

    # 간선을 weight 기준 오름차순으로 정렬
    edges = [] # 0 ~ V 까지니까 V+1

    for _ in range(E):
        start, end, weight = map(int,input().split())
        edges.append((start, end, weight))

    edges.sort(key=lambda x: x[2])

    cnt = 0 # 간선을 지날때마다 + 1
    result = 0 # 무게 합

    # make_set
    parents = [i for i in range(V+1)]
    # u와 v를 find_set해서 같지 않으면 -> 싸이클이 생기지 않는다
    # 그럼 둘을 union하고, cnt + 1, result += w
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u,v)
            cnt += 1
            result += w

            if cnt == V:
                break

    print(f'#{tc} {weight}')