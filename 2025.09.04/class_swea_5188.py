### [파이썬 S/W 문제해결 구현] 2일차 - 최소합 ###

'''
몇개의 칸이 될지 모른다 -> 빈 list를 만들고 append, pop을 이용하자

* 재귀함수의 당위성을 잘 모르겠다, 하지만 풀어야한다면 방향 벡터 필요

완전 탐색을 하자 start = 0,0 -> N-1, N-1 까지
모든 경우를 탐색하고 가장 작은 경우의 sum을 출력하자
sum보다 크다면 가지치기
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 99999999

    def f(i, j, total): # 모든 경우를 탐색하고 합을 구하는 과정 (i, j) 좌표를 이용
        global min_sum
        
        # 종료 조건
        if i == N-1 and j == N-1:
            if total < min_sum:
                min_sum = total
            return

        # Todo 가지치기
        if total > min_sum:
            return

        if i+1<N:
            f(i+1, j, total+arr[i+1][j])
        if j+1<N:
            f(i, j+1, total+arr[i][j+1])

    f(0, 0, arr[0][0]) # 시작점
    print(f'#{tc} {min_sum}')