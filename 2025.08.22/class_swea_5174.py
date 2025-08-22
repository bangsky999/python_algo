### subtree ### 

import sys; sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    lft_child = [0] * (E+2)
    rgt_child = [0] * (E+2)

    for i in range(E):
        parent, child = arr[2*i], arr[2*i+1]
        if lft_child[parent] == 0:
            lft_child[parent] = child
        else:
            rgt_child[parent] = child

    print(lft_child)
    print(rgt_child)
    cnt = 1
    def f(root):
        global cnt
        if lft_child[root] != 0:
            f(lft_child[root])
            cnt += 1

        if rgt_child[root] != 0:
            f(rgt_child[root])
            cnt += 1



    f(N)
    print(f'#{tc} {cnt}')

