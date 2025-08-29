# 최소힙을 구현하는 문제
# 부모 <= 자식의 대소관계를 만족하는 완전이진트리

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    heap = [0] * (N+1) # 완전이진트리 만들기

    nums = list(map(int, input().split())) # N개의 숫자를 입력받기
    # N개의 숫자를 주어진 순서대로 차례로 힙에 삽입
    # 힙에 삽입할 때는 주어진 숫자를 현재 완전이진트리의 마지막 원소 위치에 넣어준다.

    for i, num in enumerate(nums, start=1): # 완전이진트리에서는 index를 1번부터 사용할 것이므로
        heap[i] = num # 현재 완전이진트리의 가장 마지막 위치에 num을 삽입

        # 인덱스 i부터 시작해서 부모가 있다면, 부모와 비교해야 함
        child_idx = i # 현재 자식의 인덱스
        parent_idx = i//2 # 부모 노드의 인덱스
        # 최소힙은 모든 노드의 관계가 부모 <= 자식이어야 함(목표상태)
        # 부모 > 자식이라면 최소힙의 규칙에 위반된 상태
        while parent_idx >= 1 and heap[parent_idx] > heap[child_idx]: # 부모가 있고, 부모 > 자식이라면
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx] # 부모와 자식을 교환
            # 부모와 자식을 교환했다면, 부모(자식처럼 생각)와 부모의 부모도 비교해야 함.
            # => 반복을 이어나간다
            child_idx = parent_idx # 현재 부모를 다시 자식으로 간주하고
            parent_idx = parent_idx // 2 # 부모의 부모와 다시 비교
        
    # 모든 숫자의 삽입이 끝나면 최소힙이 완성된 상태
    # 마지막 노드부터 출발하여, 조상 노드의 합을 구하기
    ancestor_sum = 0
    child_idx = N
    parent_idx = child_idx // 2
    while parent_idx >= 1: # 부모가 있다면
        ancestor_sum += heap[parent_idx]
        parent_idx //= 2 # 그 부모의 부모로 가기

    print(f"#{tc} {ancestor_sum}")


