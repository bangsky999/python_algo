### 숫자 배열 회전 ###
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 리스트 l1
    l1 = []
    for c in range(N):
        for r in range(N-1, -1, -1):
            l1.append(arr[r][c])
    # print(l1)

    # 180도 리스트 l2
    l2 = []
    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            l2.append(arr[r][c])
    # print(l2)

    # 270도 리스트 l3
    l3 = []
    for c in range(N-1, -1, -1):
        for r in range(N):
            l3.append(arr[r][c])
    # print(l3)
    print(f'#{tc}')
    for i in range(N):
        print(f"{''.join(map(str, l1[i*N:(i+1)*N]))} {''.join(map(str, l2[i*N:(i+1)*N]))} {''.join(map(str, l3[i*N:(i+1)*N]))}")
    # print(f"{''.join(map(str, l1[N:2*N]))} {''.join(map(str, l2[N:2*N]))} {''.join(map(str, l3[N:2*N]))}")0
    # print(f"{''.join(map(str, l1[2*N:3*N]))} {''.join(map(str, l2[2*N:3*N]))} {''.join(map(str, l3[2*N:3*N]))}")