### 중간 평균값 구하기 easy
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    arr.sort() # 정렬
    res = 0
    for i in arr[1:9]:
        res += i
    avg_res = res//8
    print(f'#{tc} {avg_res}')