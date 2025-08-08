'''
- 가로, 세로 검사를 어떻게 할 것이냐
- 글자 수가 짝수, 홀수일 떄 어떡할 것이냐
0. 범위를 설정하자
1. 가로 검사와 세로 검사를 구분하자
    - arr[r][c]를 순회하며 새 리스트 lst에 저장
    - lst를 반으로 나눠(슬라이싱) l1, l2에 저장
    - if l1 == l1(거꾸로)이면 break
    - 출력
2. 나온 list를 붙여서 출력 -> join
'''
import sys
sys.stdin = open("../input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    val = 0


    ### 가로 검사
    for i in range(N):
        if val == 1:
            break

        for j in range(N-M+1):
            each_word = []
            for k in range(j, j+M):
                each_word.append(arr[i][k])
            # 검사 만들기
            if M % 2 ==0: # 길이가 짝수다
                lst1 = each_word[:M//2]
                lst2 = each_word[M:(M//2)-1:-1]
            else: # 길이가 홀수다
                lst1 = each_word[:M//2]
                lst2 = each_word[M:M//2:-1]
            if lst1 == lst2:
                val = 1
                break

    ### 세로 검사
    if val == 0:
        for i in range(N-M+1):
            if val == 1:
                break
            for j in range(N):
                each_word = []
                for k in range(i, i+M):
                    each_word.append(arr[k][j])
                # 검사 만들기
                if M % 2 == 0:  # 길이가 짝수다
                    lst1 = each_word[:M // 2]
                    lst2 = each_word[M:(M // 2) - 1:-1]
                else:  # 길이가 홀수다
                    lst1 = each_word[:M // 2]
                    lst2 = each_word[M:M // 2:-1]
                if lst1 == lst2:
                    val = 1
                    break

    print(f'#{tc}', end = ' ')
    print(''.join(each_word))