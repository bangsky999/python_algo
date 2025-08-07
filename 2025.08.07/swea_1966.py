import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬 사용
    for i in range(N-1): # 맨 뒤는 정렬안해도 자동으로 된다
        min_idx = i # 맨앞 i 인덱스를 최소라 가정 
        for j in range(i+1, N): # i 다음부터 N 끝까지 탐색
            if arr[min_idx] > arr[j]:
                min_idx = j # 탐색하면서 최소 j 값을 찾아서 min_idx에 쓰겠다

        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 연산 줄이기 위해 빼기
    print(f'#{tc}', end = ' ')
    for i in arr:
        print(i, end = ' ')
    print()