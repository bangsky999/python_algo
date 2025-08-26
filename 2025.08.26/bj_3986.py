### 흑백요리사 ###
'''
L의 수를 입력받고(롤케익 수)
총 인원수 N
N명을 순회하며 1,2,3번 사람 넘버링해서 기록(i로 순회)
가장 숫자가 큰사람이 예상 사람 - i번 사람
실제로는 그 list에 가장 많이 입력했을때 i가 가장 많은 사람이 승자
'''
# import sys; sys.stdin = open("input.txt")

L = int(input())
cake_li = [0]*(L+1) # 0번부터 10번까지 입력할 리스트 만들기
N = int(input())
max_cake = 0
expect = 0
for i in range(1, N+1):
    P, K = map(int, input().split())
    if K- P + 1 > max_cake:
        max_cake = K - P + 1
        expect = i
    for j in range(P, K+1):
        if cake_li[j] == 0:
            cake_li[j] = i
    
N_li = [0]*(N+1) # 0 0 0
for i in cake_li:
    if i != 0:
        N_li[i]+= 1
real = N_li.index(max(N_li))
    
    
print(expect)
print(real)
    