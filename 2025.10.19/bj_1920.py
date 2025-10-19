'''
M개의 수들이 N개의 정수 list에 존재하면 1 else 0
이진검색을 통해 시간을 줄이자(정렬해야함)
for문을 통해 순차적으로 탐색해 출력하고
이진검색은 함수화
- start, end, middle로 탐색
'''
def binary_search(target, arr):
    start = 0
    end = len(arr)-1 # 인덱스이니까 -1

    while start <= end: # 찾을때까지 반복문 돌리기, 탈출 조건은 start > end 일때
        mid = (start+end)//2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target: # 중앙값이 target보다 크다면
            end = mid - 1
        else: # 중앙값이 target보다 작다면
            start = mid + 1

    return 0

N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort() # 정렬

M = int(input())
M_arr = list(map(int, input().split()))

for num in M_arr:
    print(binary_search(num, N_arr)) # target, arr 넘기기
