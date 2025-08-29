T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N: 6
    heap = [0]*(N+1) # heap이 뭐냐 일정한 흐름대로 유지되는 완전이진트리 # [0,0,0,0,0,0,0]
    nums = list(map(int, input().split())) # 7 2 5 3 4 6
    for i, num in enumerate(nums, start=1): # nums를 순회하며 heap에 순서대로 1부터 쓰겠다.
        heap[i] = num # [0,7,2,5,3,4,6]

    for i in range(1, N+1):
        child_idx = i
        parent_idx = i // 2

        while parent_idx >= 1 and heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            child_idx = parent_idx
            parent_idx = parent_idx // 2

    ancestor_sum = 0
    child_idx = N
    parent_idx = child_idx // 2
    while parent_idx >= 1:
        ancestor_sum += heap[parent_idx]
        parent_idx //= 2
    print(f'#{tc} {ancestor_sum}')