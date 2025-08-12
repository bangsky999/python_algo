'''
1. 딕셔너리를 만들자 dictionary = {')':'(', '}': '{', ']': '['}
2. 입력받기 : s , stack = [] : 만들기, 초기 val = 1
3. 문자열 s를 순회하자 for i
4. if i in ['(', '{', '['] 있다면,, stack에 append하자
5. elif i in [')', '}', ']']라면
6. dict의 i 값체크
    if dict[i] == stack[-1]이라면 
        stack.pop(-1) 마지막걸 뽑겟다
    else:
        val = 0 
        break
7. ))) 이렇게 되면 stack = []인데 29번줄이 걸림
'''
import sys; sys.stdin = open("input.txt")

dictionary = {')':'(', '}': '{', ']': '['}

T = int(input())
for tc in range(1, T+1):
    stack = []
    val = 1

    s = input()
    if val == 1:
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif s[i] in [')', '}', ']']:
                if stack: # 스택이 있나
                    if dictionary[s[i]] == stack[-1]: # 딕셔너리 value가 stack의 마지막이라면
                        stack.pop() # pop!
                    else: # 값이 다르네??? 바로 탈출
                        val = 0
                        break
                else: # stack이 비었다면,,
                    val = 0
                    break
            if i == len(s) - 1: # i가 마지막에 있을때
                if len(stack): # stack이 남았다면 0이 아니라면
                    val = 0 # val값 0으로

    print(f'#{tc} {val}')