import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split()) # n:가로픽셀, k: 횟수
    arr = [[1]*n for _ in range(4)]
    
    for i in range(2, k+1): # k횟수에 대한 범위(1,...,k까지)
        for r in range(4):
            for c in range(n): # 기준점 구하기
            
                if (r+c+1) % i == 0: # k의 배수라면
                    arr[r][c] = 1 - arr[r][c]

    cnt = 0 # k횟수의 시행이 모두 끝났을떄
    for r in range(4):
        for c in range(n):
            if arr[r][c] == 1: # 픽셀이 1이라면 cnt하겠다
                cnt += 1

    print(f'#{tc} {cnt}')

            