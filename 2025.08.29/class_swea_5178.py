### 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 ###
# # -------------복습 하자 -----------------------
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     heap = [0]*(N+1)
#     for _ in range(M):
#         n, x = map(int, input().split())
#         heap[n] = x
#         p = n // 2
#         while p > 0: # 엄청난 풀이인데???
#             heap[p] += x
#             p = p // 2

#     ans = tree[L]
#     print(f'#{tc} {ans}')



### 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 ###
# import sys; sys.stdin=open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N:5, M:3, L:2
    heap = [0] * (N+1) # [0,0,0,0,0,0]
    for i in range(M): # 0 1 2
        node_num, num = map(int, input().split()) # heap : [0,0,0,3,1,2]
        heap[node_num] = num
 
    if N % 2 == 1:
        for i in range(N,0,-2): # 5  3  1
            heap[i // 2] = heap[i]+heap[i-1] # i =5일때, heap[2] = heap[5] + heap[4], heap[1] =  heap[3] + heap[2]
    else:
        heap[N//2] = heap[N]
        for i in range((N//2)-1,0,-1):
            heap[i] = heap[2*i]+heap[2*i + 1]
    # 자식노드 합 저장 완료
    print(f'#{tc}', heap[L])