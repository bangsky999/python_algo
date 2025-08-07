# A = 1~12까지 집합이다, A의 부분집합이 N개 원소, 그 부분집합의 합이 K개인 부분집합 개수 구하기
# 일단 12일때 부분집합을 다 구하고 , 2*12 만들고 
# 부분집합 전체를 순회하면서 N개, 합이 K인거 찾기, 없으면 0출력
import sys
sys.stdin = open("input.txt")

A = list(range(1, 13))
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1<<12): # 1~2^12까지 모든 부분집합 나타냄
        arr = [] # 부분집합마다 리스트를 만들어서
        for j in range(12):
            if i & (1<<j): # j번째 비트가 1이라면 
                arr.append(A[j]) # arr에 비트가 1인 놈을 추가할게요

        if len(arr) == N and sum(arr) == K:
            cnt += 1
    print(f'#{tc} {cnt}')
