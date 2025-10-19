'''
n, m을 리스트 안에서 이진 검색으로 찾자
sort 하고
start = 시작점, end = 끝점 
middle = (start+ end) // 2 까지 포함
밑에 있다면 middle -= 1
위에 있다면 middle += 1
'''
def binary_search(target, arr): # a는 찾아야할 숫자, L은 리스트
    # 정렬된 숫자에서
    start = 0
    end = len(arr) - 1
    
    while start <= end: # 아직 탐색할 구간이 남았다면
        mid = (start+end)//2 # 현재 구간의 중앙 인덱스

        if arr[mid] == target: # 중앙값이 목표면 찾음
            return 1
        
        elif arr[mid] < target: # 목표가 더 크면 오른쪽 탐색
            start = mid + 1
        else: # 목표가 더 작으면 왼쪽탐색
            end = mid - 1 
        
    return 0


N = int(input())
N_nums = list(map(int,input().split()))
N_nums.sort()

M = int(input())
M_nums = list(map(int,input().split()))

for num in M_nums:
    print(binary_search(num, N_nums))

