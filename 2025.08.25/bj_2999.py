### 비밀 이메일 ###
'''
1. 글자를 입력받고, len을 통해서 글자수를 파악
2. 글자수: N이라하면 N의 약수를 집합안에 넣는다
    - 글자수가 홀수 -> 가운데 인덱스가 r,c값 -> N//2인덱스
    - 글자수가 짝수 -> 가운데 두개가 r,c값 -> N//2-1 ~ N//2까지

3. 그 배열대로 이차원 배열 for r, for c를 만들어서세로 우선순회로 값을 입력하고
4. 읽을 떄는 가로로 읽어서 출력
'''
word = list(input()) # 'koaski'
N = len(word) # N = 6

lst = []
for i in range(1,N+1):
    if N % i == 0:
        lst.append(i)

len_lst = len(lst)

if len_lst % 2 == 0: # 짝수면
    r, c = (len_lst//2)-1, len_lst//2
elif len_lst %2 == 1: # 홀수면
    r, c = len_lst//2, len_lst//2 

real_word = []
for i in range(lst[r]):
    for j in range(i,N,lst[r]): # 
        real_word.append(word[j])

print(''.join(real_word))
