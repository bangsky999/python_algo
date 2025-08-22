### 이진탐색 ###
'''
VLR 탐색
완전 이진트리를 만들면 편하다???
root를 1로 하고, N이 주어질때 이진트리의 루트값, N//2노드값 출력


1~N까지 숫자를 VLR로 만들자
그리고 LVR로 탐색하며 숫자를 1씩 증가시켜 넣자
두개의 리스트가 필요하겠네??
그리고 조건에 맞는 값을 출력
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    l_child = [0]*(N+1) # l_child 무작정 많이 만들기
    r_child = [0]*(N+1)
    node_num = [0]*(N+1) # 노드번호마다 lvr로 갔을때 num 저장 [0,0,0,0,0,0,0]

    for i in range(1, N//2+1):
        l_child[i] = i*2
        r_child[i] = i*2+1
    if N % 2 == 0:
        r_child[N//2] = 0
        

    # print(l_child)
    # print(r_child)
    ## l, r child 만듬


    num = 1 #lvr순회하며 저장할 num값
    def f(root):
        global num
        if l_child[root] != 0:
            f(l_child[root]) # 얘는 탐색만하고


        node_num[root] = num # 값저장과 출력은 사실 여기서 함 LVR이든 VLR이든
        num += 1

        if r_child[root] != 0:
            f(r_child[root])

    f(1)
    print(f'#{tc} {node_num[1]} {node_num[N//2]}')