import sys; sys.stdin = open("input.txt")
T = 10
for tc in range(1, T+1):
    N = int(input()) # 5
    heap = [0]*(N+1) # [0,0,0,0,0,0]
    l_child = [0]*(N+1)
    r_child = [0]*(N+1)
    for i in range(1, N+1):
        info = list(input().split())
        if len(info) == 4:
            heap[int(info[0])] = info[1]
            l_child[int(info[0])] = int(info[2])
            r_child[int(info[0])] = int(info[3])
        elif len(info) == 2:
            heap[int(info[0])] = info[1]

    for i in range(N+1):
        if heap[i] not in ['+','-','*','/']:
            heap[i] = int(heap[i])

    for i in range(N, -1, -1):
        if heap[i]  == '+':
            heap[i] = heap[l_child[i]] + heap[r_child[i]]
        elif heap[i]  == '-':
            heap[i] = heap[l_child[i]] - heap[r_child[i]]
        elif heap[i]  == '*':
            heap[i] = heap[l_child[i]] * heap[r_child[i]]
        elif heap[i]  == '/':
            heap[i] = heap[l_child[i]] // heap[r_child[i]]
    # print(heap)
    # print(l_child)
    # print(r_child)
    print(f'#{tc} {heap[1]}')