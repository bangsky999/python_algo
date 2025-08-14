### Magnetic ###
'''
문제의 핵심
- (1,2)의 경우에만 교착이 발생 !
    ex) 1,1,2,2 -> 1개의 교착으로 판단(1,2)
    ex) 2,2,2,1,1,1 -> 0개의 교착으로 판단
- 주어진 배열을 세로 순회하며, 각 순회마다 0을 뺴고 리스트로 만들고,
  (1,2)의 갯수를 count하면 끝!
'''
import sys; sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 순회할 떄마다 리스트에 추가(0은 버리기)
    cnt  = 0 # (1,2) 개수 cnt
    for c in range(N):
        check_list = []
        for r in range(N):
            if arr[r][c] != 0:
                check_list.append(arr[r][c])
        # 각 행순회가 끝나면,,,check_list의 길이만큼 순회하면서 (1,2)몇개?
        
        for i in range(len(check_list)-1): # 
            if check_list[i] == 1 and (check_list[i+1]) == 2:
                cnt += 1
            
    print(f'#{tc} {cnt}')

