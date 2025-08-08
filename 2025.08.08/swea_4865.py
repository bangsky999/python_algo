'''
1. str1을 돌며 집합에 저장하고 리스트로 변환
2. 집합의 수만큼 lst를 만들어서 str1을 순회하며 str2 개수 카운트
3. max 뽑아내기
'''

import sys
sys.stdin = open("../input.txt")

T = int(input())
for tc in range(1, T+1):
    N = list(set(map(str, input())))
    M = list(map(str, input()))
    lst = [0]*len(N)
    for i in range(len(N)):
        for j in M:
            if N[i] == j:
                lst[i] += 1

    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i

    print(f'#{tc} {max_num}')