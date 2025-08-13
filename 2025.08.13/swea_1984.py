### 중간 평균값 구하기 easy
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort() # 정렬
    arr_test = arr[1:9]
    res = 0
    for i in arr_test:
        res += i
    avg_res = res/8
    print(f'#{tc} {round(avg_res)}') # 반올림 함수 round(숫자,자리수)