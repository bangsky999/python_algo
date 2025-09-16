# [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    paper = list(map(int,input().split()))

    # 1. 각 집합을 만들어주는 함수
    def make_set(n):
        # 1 ~ n까지의 원소가 "각자 자기 자신이 대표자라고 설정"
        parents = [i for i in range(n+1)]
        ranks = [0]*(n+1)
        return parents, ranks
    
    # 2. 집합의 대표자를 찾는 함수
    def find_set(x):
        # 자신 == 부모 -> 해당 집합의 대표자
        if x == parents[x]:
            return x
        
        # x의 부모 노드를 기준으로 다시 부모를 검색
        return find_set(parents[x])
    
    # 3. 두 집합을 합치는 함수
    def union(x, y):
        rep_x = find_set(x)
        rep_y = find_set(y)

        # 만약 이미 같은 집합
        if rep_x == rep_y:
            return # 같은 집합 까리는 합칠 필요가 없다
        
        # 덩치가 더 작은 집합(=rank가 더 낮은 집합)이 더 큰 집합 밑으로
        if ranks[rep_x] < ranks[rep_y]:
            parents[rep_x] = rep_y
        elif ranks[rep_x] > ranks[rep_y]:
            parents[rep_y] = rep_x
        else: 
            # ranks가 동일하다면 한쪽으로 병합하고, 대표자 ranks + 1
            parents[rep_y] = rep_x
            ranks[rep_x] += 1   

    parents, ranks = make_set(N)
    for i in range(0,len(paper),2):
        union(paper[i],paper[i+1])

    count = set()
    for i in range(1,N+1):
        count.add(find_set(parents[i]))

    print(f'#{tc} {len(count)}')